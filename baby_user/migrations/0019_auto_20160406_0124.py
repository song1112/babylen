# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby_user', '0018_auto_20160404_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_bonne',
            name='baby_count_record',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='user_normal',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
