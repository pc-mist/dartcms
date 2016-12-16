# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 02:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='users',
            field=models.ManyToManyField(related_name='user_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]