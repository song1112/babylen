# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby_user', '0008_auto_20160314_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_normal',
            name='img',
            field=models.ImageField(upload_to='image/personal'),
        ),
    ]
