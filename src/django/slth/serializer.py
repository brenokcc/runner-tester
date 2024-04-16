import os
import slth
import json
import types
from decimal import Decimal
from datetime import date, datetime
from django.template.loader import render_to_string
from django.db.models import Model, QuerySet, Manager
from django.utils.text import slugify
from .exceptions import JsonResponseException
from .utils import absolute_url, build_url
from .components import Image, FileLink, FileViewer
from django.db.models.fields.files import ImageFieldFile, FieldFile


def to_snake_case(name):
    return slugify(name).replace('-', '_')


def serialize(obj, primitive=False, request=None):
    if obj is None:
        return None
    elif isinstance(obj, dict):
        if request:
            if isinstance(obj, Image):
                if isinstance(obj['src'], ImageFieldFile):
                    obj['src'] = build_url(request, obj['src'].url) if obj['src'] else None
            elif isinstance(obj, FileLink) or isinstance(obj, FileViewer):
                if isinstance(obj['url'], FieldFile):
                    obj['url'] = build_url(request, obj['url'].url) if obj['url'] else None
        return obj
    elif isinstance(obj, date):
        return obj.strftime('%d/%m/%Y')
    elif isinstance(obj, datetime):
        return obj.strftime('%d/%m/%Y %H:%M:%S')
    elif isinstance(obj, bool):
        return obj
    if isinstance(obj, Decimal) or isinstance(obj, float):
        return str(obj).replace('.', ',')
    elif isinstance(obj, list):
        return [serialize(obj) for obj in obj]
    elif isinstance(obj, Model):
        return str(obj) if primitive else dict(pk=obj.pk, str=str(obj))
    elif isinstance(obj, QuerySet) or isinstance(obj, Manager) or type(obj).__name__ == 'ManyRelatedManager':
        return [str(obj) for obj in obj.filter()] if primitive else obj.serialize()
    elif isinstance(obj, ImageFieldFile):
        return str(obj)
    elif hasattr(obj, 'serialize'):
        return obj.serialize()
    return str(obj)

def getfield(obj, name_or_names, request=None):
    if isinstance(name_or_names, str):
        attr = getattr(obj, name_or_names)
        if type(attr) == types.MethodType:
            value = attr()
            label = getattr(attr, 'verbose_name', name_or_names)
        elif name_or_names.startswith('get_') and name_or_names.endswith('_display'):
            value = attr()
            label = getattr(type(obj), name_or_names[4:-8]).field.verbose_name
        else:
            value = attr
            label = getattr(type(obj), name_or_names).field.verbose_name
        label = label.title() if label and label.islower() else label
        field = dict(type='field', name=name_or_names, label=label, value=serialize(value, primitive=True, request=request))
        return field
    elif isinstance(name_or_names, LinkField):
        value = getattr(obj, name_or_names.name) if obj else None
        field = dict(type='field', name=name_or_names.name, value=serialize(value, primitive=True))
        if value:
            if name_or_names.endpoint(value.id).contextualize(request).check_permission():
                field.update(url=name_or_names.endpoint.get_api_url(value.id))
        return field
    else:
        fields = []
        for name in name_or_names:
            fields.append(getfield(obj, name, request))
        return fields

class LinkField:
    def __init__(self, name, endpoint):
        self.name = name
        self.endpoint = endpoint

class Serializer:
    def __init__(self, obj=None, request=None, serializer=None, type='object', title=None):
        self.path = serializer.path.copy() if serializer else []
        self.obj = obj
        self.lazy = False
        self.ignore_only = False
        self.request = request
        self.metadata = dict(actions=[], content=[], allow=[])
        self.serializer:Serializer = serializer
        self.type = type
        if title:
            self.title = title
            self.path.append(to_snake_case(title))
        else:
            self.title = str(obj) if obj else None

    def actions(self, *actions):
        self.metadata['actions'].extend(actions)
        self.metadata['allow'].extend(actions)
        return self
        
    def fields(self, *names):
        self.metadata['content'].append(('fields', None, dict(names=names)))
        return self
    
    def fieldset(self, title, fields=(), actions=(), attr=None):
        self.metadata['allow'].extend(actions)
        self.metadata['content'].append(('fieldset', to_snake_case(title), dict(title=title, names=fields, attr=attr, actions=actions)))
        return self
        
    def queryset(self, title, name, actions=(), related_field=None):
        self.metadata['content'].append(('queryset', name, dict(title=title, actions=actions, related_field=related_field)))
        return self
    
    def endpoint(self, title, cls, wrap=True):
        if isinstance(cls, str):
            cls = slth.ENDPOINTS[cls]
        self.metadata['content'].append(('endpoint', to_snake_case(title), dict(title=title, cls=cls, wrap=wrap)))
        return self
    
    def append(self, title, component):
        self.metadata['content'].append(('component', to_snake_case(title), dict(title=title, component=component)))
    
    def section(self, title):
        return Serializer(obj=self.obj, request=self.request, serializer=self, type='section', title=title)
    
    def group(self, title):
        return Serializer(obj=self.obj, request=self.request, serializer=self, type='group', title=title)

    def parent(self):
        self.serializer.metadata['content'].append(('serializer', to_snake_case(self.title), dict(serializer=self)))
        return self.serializer
    
    def contextualize(self, request):
        self.request = request
        return self
    
    def serialize(self, debug=False, forward_exception=False):
        try:
            return self.to_dict(debug=debug)
        except JsonResponseException as e:
            if self.serializer or forward_exception:
                raise e
            if debug:
                print(json.dumps(e.data, indent=2, ensure_ascii=False))
            return e.data
        
    def __str__(self):
        return f'{self.title} / {self.type}'


    def to_dict(self, debug=False):
        base_url = absolute_url(self.request)
        if self.ignore_only:
            only = []
        else:
            only = self.request and self.request.GET.get('only', None)
            if only:
                only = only.split('__')

        if self.request and 'action' in self.request.GET:
            cls = slth.ENDPOINTS[self.request.GET.get('action')]
            if cls and cls.get_api_name() in self.metadata['allow']:
                endpoint = cls.instantiate(self.request, self.obj)
                if endpoint.check_permission():
                    raise JsonResponseException(endpoint.serialize())

        if not self.metadata['content'] and self.obj:
            self.fields(*[field.name for field in type(self.obj)._meta.fields])
            for m2m in type(self.obj)._meta.many_to_many:
                self.queryset(m2m.verbose_name, m2m.name)
        
        items = []
        if not self.lazy:
            for i, (datatype, key, item) in enumerate(self.metadata['content']):
                leaf = only and only[-1] == key
                lazy = i and self.type == 'group' and not leaf
                data = None
                if datatype == 'fields':
                    data = []
                    if not lazy:
                        for name in item['names']:
                            if key is None or not only or name in only:
                                data.append(getfield(self.obj, name, self.request))
                        if only and only[-1] == name: raise JsonResponseException(data)
                elif datatype == 'fieldset':
                    title = item['title']
                    names = item['names']
                    attr = item['attr']
                    if not only or key in only:
                        actions=[]
                        fields=[]
                        title = title.title() if title and title.islower() else title
                        url = absolute_url(self.request, '?only={}'.format('__'.join(self.path + [key])))
                        if lazy:
                            data = dict(type='fieldset', title=title, key=key, url=url)
                        else:
                            obj = getattr(self.obj, attr) if attr else self.obj
                            if obj:
                                for name in names:
                                    fields.append(getfield(obj, name, self.request))
                            if not only:
                                for qualified_name in item['actions']:
                                    cls = slth.ENDPOINTS[qualified_name]
                                    if cls.instantiate(self.request, self.obj).check_permission():
                                        actions.append(cls.get_api_metadata(self.request, base_url, self.obj.pk))
                            
                            data = dict(type='fieldset', title=title, key=key, url=url, actions=actions, data=fields)
                        if leaf: raise JsonResponseException(data)
                elif datatype == 'queryset':
                    title = item['title']
                    if not only or key in only:
                        attr = getattr(self.obj, key)
                        if type(attr) == types.MethodType:
                            value = attr().filter()
                        else:
                            value = attr.filter()
                        
                        if item['actions']:
                            value = value.actions(*item['actions'])
                        if item['related_field']:
                            value = value.relation(item['related_field'], self.obj.id)
                        
                        if lazy:
                            data = dict(type='queryset', title=title, key=key)
                        else:
                            data = value.title(title).attrname(key).contextualize(self.request).serialize(debug=False)
                        path = self.path + [key]
                        data['url'] = absolute_url(self.request, '?only={}'.format('__'.join(path)))
                        if leaf: raise JsonResponseException(data)
                elif datatype == 'endpoint':
                    data = {}
                    title = item['title']
                    cls = item['cls']
                    wrap = item['wrap']
                    if not only or key in only:
                        returned = {}
                        endpoint = cls.instantiate(self.request, self.obj)
                        if endpoint.check_permission():
                            if not lazy:
                                returned = endpoint.getdata()
                            path = self.path + [key]
                            if wrap:
                                data = dict(type='fieldset', key=key, title=title, url=None, data=serialize(returned))
                            else:
                                data = serialize(returned)
                                data['title'] = title
                            if isinstance(data, dict):
                                data['url'] = absolute_url(self.request, '?only={}'.format('__'.join(path)))
                            if leaf: raise JsonResponseException(data)
                elif datatype == 'component':
                    title = item['title']
                    component = item['component']
                    data = {}
                    if not only or key in only:
                        data = serialize(component)
                    path = self.path + [key]
                    data['url'] = absolute_url(self.request, '?only={}'.format('__'.join(path)))
                    if leaf: raise JsonResponseException(data)
                elif datatype == 'serializer':
                    serializer = item['serializer']
                    serializer.lazy = lazy
                    if not only or key in only:
                        serializer.ignore_only = self.ignore_only or leaf
                        data = serializer.to_dict()
                        if leaf: raise JsonResponseException(data)
                if data:
                    items.extend(data) if datatype == 'fields' else items.append(data)

        actions = []
        if not only and not self.lazy:
            for qualified_name in self.metadata['actions']:
                cls = slth.ENDPOINTS[qualified_name]
                if cls.instantiate(self.request, self.obj).check_permission():
                    actions.append(cls.get_api_metadata(self.request, base_url, self.obj.pk))
        
        output = dict(type=self.type, title=self.title)
        if self.serializer:
            datatype = to_snake_case(self.title)
            output.update(key=datatype)
        if self.path:
            url = absolute_url(self.request, '?only={}'.format('__'.join(self.path)))
        else:
            url = absolute_url(self.request)
        output.update(url=url)
        if not self.lazy:
            output.update(actions=actions, data=items)
        if debug:
            print(json.dumps(output, indent=2, ensure_ascii=False))
        return output
