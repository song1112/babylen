# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby', '0002_auto_20160314_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='image/baby'),
        ),
        migrations.AlterField(
            model_name='baby_picture',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='image/baby'),
        ),
    ]
