# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby_user', '0014_auto_20160316_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_bonne',
            name='user_id_daycarecenter',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
