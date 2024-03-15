
import json
from django.apps import apps
from typing import Any
from django.conf import settings
from django.db import transaction, models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms
from .exceptions import JsonResponseException
from .serializer import serialize


import slth


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
        if name not in ('Endpoint', 'ChildEndpoint') and 'ChildEndpoint' not in [cls.__name__ for cls in bases]:
            slth.ENDPOINTS[cls.__name__.lower()] = cls
        return cls


class Endpoint(metaclass=EnpointMetaclass):
    fieldsets = None
    source = None
    form_class = None

    def __init__(self, request, *args):
        self.request = request
        self.parse()
        if self.fieldsets and self.source:
            self.form_class = forms.modelform_factory(type(self.source),form=forms.ModelForm, fields='__all__')
        
    def load(self):
        pass

    def parse(self):
        content_type = self.request.META.get('CONTENT_TYPE')
        method = self.request.method.lower()
        if content_type and content_type.lower() == 'application/json':
            if method == 'get' or method == 'post':
                d1 = json.loads(self.request.body.decode()) if self.request.body else {}
                d2 = self.request.GET if method == 'get' else self.request.POST
                d2._mutable = True
                d2.clear()
                for k, v in d1.items():
                    if isinstance(v, list):
                        for i, item in enumerate(v):
                            prefix = f'{k}__{i}'
                            d2[prefix] = item.get('id')
                            for k1, v1 in item.items():
                                d2[f'{prefix}__{k1}'] = v1
                    else:
                        d2[k] = v
                d2._mutable = False

    def objects(self, model):
        return apps.get_model(model).objects

    def get_form(self, data):
        form = None
        if self.form_class:
            if issubclass(self.form_class, forms.DjangoModelForm):
                form = self.form_class(data=data, instance=self.source, endpoint=self)
            elif issubclass(self.form_class, forms.DjangoForm):
                form = self.form_class(data=data, endpoint=self)
        return form
        
    def get(self):
        try:
            form = self.get_form(self.request.GET)
            return forms.serialize(form, self.request) if form else serialize(self.source or {})
        except JsonResponseException as e:
            return e.data
    
    def post(self):
        data = {}
        errors = {}
        form = self.get_form(self.request.POST)
        inline_fields = {name: field for name, field in form.fields.items() if isinstance(field, forms.InlineFormField) or isinstance(field, forms.InlineModelField)}
        if form:
            form.is_valid()
            errors.update(form.errors)
            for inline_field_name, inline_field in inline_fields.items():
                data[inline_field_name] = []
                for i in range(0, inline_field.max):
                    prefix = f'{inline_field_name}__{i}'
                    if prefix in form.data:
                        inline_form_data = {}
                        pk = form.data.get(prefix)
                        for name in inline_field.form.base_fields:
                            inline_form_field_name = f'{inline_field_name}__{i}__{name}'
                            inline_form_data[name] = form.data.get(inline_form_field_name)
                        instance = inline_field.form._meta.model.objects.get(pk=pk) if pk else None
                        inline_form = inline_field.form(data=inline_form_data, instance=instance)
                        if inline_form.is_valid():
                            if isinstance(inline_form, forms.DjangoModelForm):
                                data[inline_field_name].append(inline_form.instance)
                            else:
                                data[inline_field_name].append(inline_form.cleaned_data)
                        else:
                            errors.update({f'{inline_field_name}__{i}__{name}': error for name, error in inline_form.errors.items()})
            data.update({field_name: form.cleaned_data.get(field_name) for field_name in form.fields if field_name not in inline_fields}) 
        if errors:
            return dict(message='Please correct the errors.', errors=errors)
        else:
            with transaction.atomic():
                form.cleaned_data = data
                if isinstance(form, forms.DjangoModelForm):
                    form.save()
                    for inline_field_name in inline_fields:
                        relation = getattr(form.instance, inline_field_name)
                        for obj in form.cleaned_data[inline_field_name]:
                            obj.save()
                            relation.add(obj)
                    dict(message='Action successfully performed.')
                else:
                    return form.submit()
    
    def save(self, data):
        pass
    
    def check_permission(self):
        return True
    
    def to_response(self):
        method = self.request.method.lower()
        if method == 'get':
            data = self.get()
        elif method == 'post':
            data = self.post()
        else:
            data = {}
        return ApiResponse(serialize(data), safe=False)
    
    @classmethod
    def get_api_name(cls):
        name = []
        for c in cls.__name__:
            if name and c.isupper():
                name.append('-')
            name.append(c.lower())
        return ''.join(name)
    
    @classmethod
    def get_api_url(cls, *args):
        url = '/api/{}/'.format(cls.get_api_name())
        for arg in args:
            url = '{}{}/'.format(url, arg)
        return url
        

class ChildEndpoint(Endpoint):
    def __init__(self, request, parent, *args):
        self.parent = parent
        super().__init__(request, *args)

class Login(Endpoint):
    form_class = forms.LoginForm

