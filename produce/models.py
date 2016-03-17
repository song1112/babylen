# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from baby_user.models import user, PathAndRename

class produce_type(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    name = models.CharField(blank=False, max_length=20)

class produce(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    name = models.CharField(blank=False, max_length=20)
    price = models.IntegerField()
    img = models.ImageField(upload_to=PathAndRename('image/produce/'), blank=True, null=True)
    produce_type_id = models.IntegerField() # models.ForeignKey(produce_type)

class produce_trade(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    money = models.IntegerField()
    trade_data = models.TextField(blank=True, null=True)
    allpay_data = models.TextField(blank=True, null=True)
    user_id = models.IntegerField() # models.ForeignKey(user)

