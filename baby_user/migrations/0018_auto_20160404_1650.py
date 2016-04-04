# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 08:50
from __future__ import unicode_literals

import baby_user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby_user', '0017_auto_20160404_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_normal',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user_normal',
            name='img',
            field=models.ImageField(blank=True, upload_to=baby_user.models.PathAndRename('image/user_normal/')),
        ),
    ]
