# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 01:30
from __future__ import unicode_literals

import baby_user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0003_auto_20160320_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='discuss_message',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=baby_user.models.PathAndRename('image/discuss_message1/')),
        ),
        migrations.AddField(
            model_name='discuss_message',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to=baby_user.models.PathAndRename('image/discuss_message2/')),
        ),
    ]
