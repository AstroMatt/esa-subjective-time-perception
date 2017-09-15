import hashlib
from django.db import models
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import GenericIPAddressField
from django.db.models import PositiveSmallIntegerField
from django.db.models import TextField
from django.utils.translation import ugettext_lazy as _


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_sha1(text):
    return hashlib.sha1(bytes(text, encoding='utf-8')).hexdigest()


class HTTPRequest(models.Model):
    METHOD_GET = 'GET'
    METHOD_POST = 'POST'
    METHOD_PATCH = 'PATCH'
    METHOD_PUT = 'PUT'
    METHOD_HEAD = 'HEAD'

    METHOD_CHOICES = [
        (METHOD_GET, _('GET')),
        (METHOD_POST, _('POST')),
        (METHOD_PATCH, _('PATCH')),
        (METHOD_PUT, _('PUT')),
        (METHOD_HEAD, _('HEAD')),
    ]

    datetime = DateTimeField(verbose_name=_('Datetime'), auto_now_add=True)
    modified = DateTimeField(verbose_name=_('Datetime'), auto_now=True)
    ip = GenericIPAddressField(verbose_name=_('IP'))
    method = CharField(verbose_name=_('Method'), max_length=10, choices=METHOD_CHOICES, default=METHOD_GET)
    api_version = PositiveSmallIntegerField(verbose_name=_('API version'))
    data = TextField(verbose_name=_('Data'), null=True, blank=True)
    sha1 = CharField(verbose_name=_('SHA1'), max_length=40, unique=True, null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        self.sha1 = get_sha1(self.data)
        super().save(*args, **kwargs)

    @staticmethod
    def add(request, api_version):
        return HTTPRequest.objects.create(
            ip=get_client_ip(request),
            api_version=api_version,
            method=request.method,
            data=request.body,
            sha1=get_sha1(request.body),
        )

    def __str__(self):
        return f'[{self.datetime}] ({self.sha1:.7}) {self.method} - {self.ip}'

    class Meta:
        verbose_name = _('HTTP Request')
        verbose_name_plural = _('HTTP Requests')
