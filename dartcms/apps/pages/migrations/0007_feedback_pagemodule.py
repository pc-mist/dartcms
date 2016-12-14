# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-06 06:54
from __future__ import unicode_literals

from django.db import migrations
from django.utils import translation
from django.utils.translation import gettext_lazy as _


def insert_module(apps, schema):
    from django.conf import settings
    translation.activate(settings.LANGUAGE_CODE)

    PageModule = apps.get_model('pages', 'PageModule')

    PageModule.objects.create(slug='feedback', name=_('Feedback'), related_model='feedback.FormType'),

    translation.deactivate()


def drop_module(apps, schema):
    PageModule = apps.get_model('pages', 'PageModule')

    PageModule.objects.get(slug='feedback').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('pages', '0006_auto_20160711_1627'),
    ]

    operations = [
        migrations.RunPython(insert_module, drop_module)
    ]
