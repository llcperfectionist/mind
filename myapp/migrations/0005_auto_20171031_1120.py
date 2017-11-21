# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-31 11:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_delete_instamojo_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.course'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
