# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0002_auto_20160315_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discuss',
            name='discuss_type_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='discuss_message',
            name='discuss_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
