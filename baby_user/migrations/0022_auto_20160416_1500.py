# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-16 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby_user', '0021_header_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_bonne',
            name='baby_count_record',
            field=models.CharField(blank=True, default='', max_length=5, null=True),
        ),
    ]
