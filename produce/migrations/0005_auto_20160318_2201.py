# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 14:01
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('produce', '0004_auto_20160317_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produce_trade',
            name='allpay_data',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produce_trade',
            name='trade_data',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
