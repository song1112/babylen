# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby_user', '0009_auto_20160316_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_normal',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='image/personal'),
        ),
    ]
