import json
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


class RequestLogger(models.Model):
    datetime = DateTimeField(verbose_name=_('Datetime'), auto_now_add=True)
    ip = GenericIPAddressField(verbose_name=_('IP'))
    method = CharField(verbose_name=_('Method'), max_length=10)
    api_version = PositiveSmallIntegerField(verbose_name=_('API version'))
    data = TextField(verbose_name=_('Data'), null=True, blank=True)

    @staticmethod
    def add(request, api_version):
        return RequestLogger.objects.create(
            ip=get_client_ip(request),
            api_version=api_version,
            method=request.method,
            data=request.body)

    def __str__(self):
        return f'[{self.datetime}] {self.method} - {self.ip}'

    class Meta:
        ordering = ['-datetime']
        verbose_name = _('Request')
        verbose_name_plural = _('Requests')
