# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby_user', '0022_auto_20160416_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_bonne',
            name='baby_auth_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user_daycarecenter',
            name='baby_auth_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]