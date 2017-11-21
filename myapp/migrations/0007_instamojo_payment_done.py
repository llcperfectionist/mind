# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-13 14:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0006_instamojo_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='instamojo_payment_done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.CharField(max_length=100)),
                ('item_name', models.CharField(max_length=100)),
                ('payment_request_id', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=500)),
                ('payment_id', models.CharField(max_length=500)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'instamojo_payment_done',
            },
        ),
    ]