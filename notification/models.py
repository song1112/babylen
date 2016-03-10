# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from baby_user.models import user
class notification_apns(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    useragent = models.CharField(blank=False, max_length=100)   # 推播裝置用戶代理
    deviceid = models.CharField(blank=False, max_length=200)    # 推播裝置ID
    user_id = models.ForeignKey(user)

class notification_gcm(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    useragent = models.CharField(blank=False, max_length=100)   # 推播裝置用戶代理
    deviceid = models.CharField(blank=False, max_length=200)    # 推播裝置ID
    user_id = models.ForeignKey(user)
