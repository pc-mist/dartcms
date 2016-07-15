# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 13:54
from __future__ import unicode_literals

import dartcms.utils.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_auto_20160714_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='Fullname')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('shipping_address', models.TextField(blank=True, null=True, verbose_name='Shipping address')),
                ('shipping_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cost')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Is paid')),
                ('paid_sum', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Paid sum')),
                ('discount_percent', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Discount')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
                'abstract': False,
                'verbose_name': 'order status',
                'verbose_name_plural': 'order statuses',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, verbose_name='Code')),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Price')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='shop.Order', verbose_name='Order')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
                'verbose_name': 'order_datil',
                'verbose_name_plural': 'order_datils',
            },
        ),
        migrations.CreateModel(
            name='OrderPaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', dartcms.utils.fields.RteField(blank=True, default=b'', verbose_name='Description')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is enabled')),
                ('sort', models.IntegerField(default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['sort'],
                'abstract': False,
                'verbose_name': 'payment type',
                'verbose_name_plural': 'payment types',
            },
        ),
        migrations.CreateModel(
            name='OrderShippingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', dartcms.utils.fields.RteField(blank=True, default=b'', verbose_name='Description')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cost')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is enabled')),
                ('sort', models.IntegerField(default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['sort'],
                'abstract': False,
                'verbose_name': 'shipping type',
                'verbose_name_plural': 'shipping types',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', dartcms.utils.fields.RteField(blank=True, default=b'', verbose_name='Description')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is enabled')),
                ('sort', models.IntegerField(default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['sort'],
                'abstract': False,
                'verbose_name': 'order status',
                'verbose_name_plural': 'order statuses',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer_products', to='shop.ProductManufacturer', verbose_name='Manufacturer'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.OrderPaymentType', verbose_name='Payment type'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.OrderShippingType', verbose_name='Shipping type'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.OrderStatus', verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
