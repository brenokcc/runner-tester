
from typing import TypeVar, Generic
import inspect
from django.apps import apps
from django.core.cache import cache
from django.conf import settings
from django.utils.text import slugify
from django.db import transaction, models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm, ModelForm, Form, FormFactory
from .serializer import serialize, Serializer
from .components import Application as Application_, Navbar, Footer, Response, Boxes, IconSet
from .exceptions import JsonResponseException
from .utils import build_url, append_url
from slth import APPLICATON, ENDPOINTS


import slth


T = TypeVar("T")

class ApiResponse(JsonResponse):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["Access-Control-Allow-Origin"] = "*"
        self["Access-Control-Allow-Headers"] = "*"
        self["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE, PATCH";
        self["Access-Control-Max-Age"] = "600"


class EnpointMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if name not in ('Endpoint', 'ChildEndpoint') and '_ChildEndpoint' not in [cls.__name__ for cls in bases]:
            ENDPOINTS[cls.__name__.lower()] = cls
        return cls


class Endpoint(metaclass=EnpointMetaclass):
    cache = cache

    def __init__(self):
        self.request = None
        self.source = None
        self.instantiator = None
        super().__init__()

    def configure(self, source, instantiator=None):
        self.source = source
        self.instantiator = instantiator
        return self

    def contextualize(self, request):
        self.request = request
        return self

    def objects(self, model):
        return apps.get_model(model).objects
        
    def get(self):
        return {}
    
    def post(self):
        data = self.get()
        if isinstance(data, FormFactory):
            data = data.form(self.request).post()
        if isinstance(data, Form) or isinstance(data, ModelForm):
            data = data.post()
        return data
    
    def save(self, data):
        pass
    
    def check_permission(self):
        return True
    
    def redirect(self, url):
        raise JsonResponseException(dict(type='redirect', url=url))
    
    def getdata(self):
        if self.request.method == 'GET':
            data = self.get()
        elif self.request.method == 'POST':
            data = self.post()
        else:
            data = {}
       
        if isinstance(data, models.QuerySet):
            data = data.contextualize(self.request)
        elif isinstance(data, Serializer):
            data = data.contextualize(self.request)
        elif isinstance(data, FormFactory):
            data = data.form(self.request)
        return data
    
    def serialize(self):
        return serialize(self.getdata())
    
    def to_response(self):
        return ApiResponse(self.serialize(), safe=False)
    
    def formfactory(self, instance, delete=False) -> FormFactory:
        return FormFactory(instance, delete=delete)
    
    def serializer(self, instance) -> Serializer:
        return instance.serializer().contextualize(self.request)
    
    @classmethod
    def is_child(cls):
        return False
    
    @classmethod
    def get_api_name(cls):
        return cls.__name__.lower()
    
    @classmethod
    def get_api_url(cls, arg=None):
        if arg:
            return f'/api/{cls.get_api_name()}/{arg}/'  
        return f'/api/{cls.get_api_name()}/'    
    
    @classmethod
    def get_pretty_name(cls):
        name = []
        for c in cls.__name__:
            if name and c.isupper():
                name.append(' ')
            name.append(c)
        return ''.join(name)
    
    @classmethod
    def get_qualified_name(cls):
        return '{}.{}'.format(cls.__module__, cls.__name__).lower()
    
    @classmethod
    def instantiate(cls, request, source):
        args = ()
        if cls.is_child():
            args = (source,) if cls.has_args() else ()
        else:
            args = (source.pk,) if cls.has_args() else ()
        return cls(*args).configure(source).contextualize(request)
    
    @classmethod
    def has_args(cls):
        return len(inspect.getfullargspec(cls.__init__).args) > 1
    
    @classmethod
    def get_api_url_pattern(cls):
        args = inspect.getfullargspec(cls.__init__).args[1:]
        pattern = '{}/'.format(cls.get_api_name())
        for arg in args:
            pattern = '{}{}/'.format(pattern, '<int:{}>'.format(arg))
        return pattern
    
    @classmethod
    def get_api_metadata(cls, request, base_url, pk=None):
        action_name = cls.get_metadata('verbose_name')
        if cls.is_child():
            url = append_url(base_url, f'action={cls.get_api_name()}')
            url = f'{url}&id={pk}' if pk else url
        else:
            url = build_url(request, f'/api/{cls.get_api_name()}/')
            url = f'{url}{pk}/' if pk else url
        return dict(type='action', title=action_name, name=action_name, url=url, key=cls.get_api_name())
    
    @classmethod
    def get_metadata(cls, key, default=None):
        value = None
        metaclass = getattr(cls, 'Meta', None)
        if metaclass:
            value = getattr(metaclass, key, None)
        if value is None and key == 'verbose_name':
            value = cls.get_pretty_name()
        return value or default

class ModelEndpoint(Endpoint):
    def __init__(self):
        self.model = self.__orig_bases__[0].__args__[0]
        if isinstance(self.model, str):
            self.model = self.objects(self.model).get(pk=self.pk)
        super().__init__()

class AdminEndpoint(Generic[T], ModelEndpoint):
    def get(self):
        actions = ['add', 'view', 'edit', 'delete']
        return self.model.objects.all().actions(*actions)
    
class ListEndpoint(Generic[T], ModelEndpoint):
    def get(self):
        return self.model.objects.all()

class AddEndpoint(Generic[T], ModelEndpoint):
    def get(self):
        return self.formfactory(self.model())

class ModelInstanceEndpoint(ModelEndpoint):
    def __init__(self, pk):
        self.pk = pk
        super().__init__()

    def get_instance(self):
        return self.model.objects.get(pk=self.pk)

class InstanceEndpoint(Generic[T], ModelInstanceEndpoint):
    pass

class ViewEndpoint(Generic[T], ModelInstanceEndpoint):
    def get(self) -> Serializer:
        return self.serializer(self.get_instance())
        
class EditEndpoint(Generic[T], ModelInstanceEndpoint):
    def get(self) -> FormFactory:
        return self.formfactory(self.get_instance())
    
class DeleteEndpoint(Generic[T], ModelInstanceEndpoint):
    def get(self) -> FormFactory:
        return self.formfactory(self.get_instance(), delete=True)
    

class FormEndpoint(Generic[T], Endpoint):

    def get_form_cls(self):
        return self.__orig_bases__[0].__args__[0]

    def get(self):
        return self.get_form_cls()(request=self.request)
    
class InstanceFormEndpoint(Generic[T], Endpoint):
    def __init__(self, pk):
        self.pk = pk
        super().__init__()

    def get_form_cls(self):
        return self.__orig_bases__[0].__args__[0]

    def get_instance(self):
        return self.get_form_cls().Meta.model.objects.get(pk=self.pk)

    def get(self):
        return self.get_form_cls()(self.get_instance(), request=self.request)
    
class ChildEndpoint(Endpoint):

    @classmethod
    def is_child(cls):
        return True

class Add(ChildEndpoint):
    def get(self):
        return self.formfactory(self.source.model())
    
class ChildInstanceEndpoint(ChildEndpoint):
    def __init__(self, instance):
        self.instance = instance
        super().__init__()

    def get_instance(self):
        return self.instance

class View(ChildInstanceEndpoint):
    
    def get(self):
        return self.serializer(self.get_instance())

class Edit(ChildInstanceEndpoint):

    def get(self):
        return self.formfactory(self.get_instance())
    
class Delete(ChildInstanceEndpoint):

    def get(self):
        return self.formfactory(self.get_instance(), delete=True)

class Login(Endpoint):
    def get(self):
        return LoginForm(request=self.request)

class Logout(Endpoint):
    def get(self):
        return Response(message='Logout realizado com sucesso.', redirect='/api/login/', store=dict(token=None))


class Icons(Endpoint):
    class Meta:
        modal = True
        verbose_name = 'Icons'

    def get(self):
        return IconSet()


class Search(Endpoint):
    def get(self):
        key = '_options_'
        options = self.cache.get(key)
        term = self.request.GET.get('term')
        if options is None:
            options = []
            for endpoint in APPLICATON['dashboard']['search']:
                cls = ENDPOINTS[endpoint]
                url = build_url(self.request, cls.get_api_url())
                verbose_name = cls.get_metadata('verbose_name')
                options.append(dict(id=url, value=verbose_name))
            self.cache.set(key, options)
        if term:
            result = []
            for option in options:
                if slugify(term.lower()) in slugify(option['value'].lower()):
                    result.append(option)
        else:
            result = options
        return result[0:10]
    
class Dashboard(Endpoint):
    def get(self):
        if 1 or self.request.user.is_authenticated:
            serializer = Serializer(request=self.request)
            if APPLICATON['dashboard']['boxes']:
                boxes = Boxes('Acesso Rápido')
                for endpoint in APPLICATON['dashboard']['boxes']:
                    cls = ENDPOINTS[endpoint]
                    if cls().contextualize(self.request).check_permission():
                        icon = cls.get_metadata('icon', 'check')
                        label = cls.get_metadata('verbose_name')
                        url = build_url(self.request, cls.get_api_url())
                        boxes.append(icon, label, url)
                serializer.append('Acesso Rápido', boxes)
            if APPLICATON['dashboard']['top']:
                group = serializer.group('Teste')
                for endpoint in APPLICATON['dashboard']['top']:
                    cls = ENDPOINTS[endpoint]
                    group.endpoint(cls.get_metadata('verbose_name'), cls, wrap=False)
                group.parent()
            for endpoint in APPLICATON['dashboard']['center']:
                cls = ENDPOINTS[endpoint]
                serializer.endpoint(cls.get_metadata('verbose_name'), cls, wrap=False)
            return serializer
        else:
            self.redirect('/api/login/')
    
class Application(Endpoint):
    def get(self):
        navbar = None
        if self.request.user.is_authenticated:
            navbar = Navbar(
                title=APPLICATON['title'], subtitle=APPLICATON['subtitle'],
                logo=APPLICATON['logo'], user=self.request.user.username
            )
            for endpoint in APPLICATON['dashboard']['usermenu']:
                cls = ENDPOINTS[endpoint]
                if cls().contextualize(self.request).check_permission():
                    label = cls.get_metadata('verbose_name')
                    url = build_url(self.request, cls.get_api_url())
                    modal = cls.get_metadata('modal', False)
                    navbar.add_action(label, url, modal)
        footer = Footer(APPLICATON['version'])
        return Application_(navbar=navbar, footer=footer)
