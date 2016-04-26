# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.conf import settings

@deconstructible
class PathAndRename(object):
    def __init__(self, path):
        self.sub_path = path
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)

class header_pic(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to=PathAndRename('image/header_pic/'), blank=True)

class user(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    account = models.CharField(blank=False, max_length=20, unique=True)
    password = models.CharField(blank=False, max_length=20)
    auth_parents = models.IntegerField()
    auth_bonne = models.IntegerField()
    auth_daycarecenter = models.IntegerField()

    def __unicode__(self):
        return self.account

class user_normal(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=20, default="")
    birthday = models.DateField(null=True)
    sex = models.CharField(blank=True, null=True, max_length=1, default="")    
    tips = models.TextField(blank=True, null=True, default="")
    img = models.ImageField(upload_to=PathAndRename('image/user_normal/'), blank=True)
    phone = models.CharField(blank=True, null=True, max_length=20, default="")
    address = models.TextField(blank=True, null=True, default="")
    user_id = models.IntegerField(unique=True) # models.ForeignKey(user) 

class user_daycarecenter(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    setuptime = models.DateField(blank=True, null=True)             # 托育中心成立時間
    business_philosophy = models.TextField(blank=True, null=True, default="")   # 托育中心經營理念
    diet_plan = models.TextField(blank=True, null=True, default="")             # 托育中心飲食規劃
    learn_plan = models.TextField(blank=True, null=True, default="")            # 托育中心學習規劃
    about_us = models.TextField(blank=True, null=True, default="")              # 托育中心關於我們
    user_id =  models.IntegerField(unique=True) # models.ForeignKey(user)
    baby_auth = models.IntegerField(blank=True, null=True, default=0)

class user_bonne(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    seniority = models.CharField(blank=True, null=True, max_length=3, default="")   # 保姆年資
    specialty = models.TextField(blank=True, null=True, default="")                 # 保姆專長
    experience = models.TextField(blank=True, null=True, default="")                # 保姆專長
    baby_count_record = models.CharField(blank=True, null=True, max_length=5, default="")     # 保姆曾照育寶寶數
    user_id =  models.IntegerField(unique=True) # models.ForeignKey(user)
    user_id_daycarecenter = models.IntegerField(blank=True, null=True) # models.ForeignKey(user_daycarecenter)
    baby_auth = models.IntegerField(blank=True, null=True, default=0)


