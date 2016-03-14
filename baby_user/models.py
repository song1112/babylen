# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class user(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    account = models.CharField(blank=False, max_length=20, unique=True)
    password = models.CharField(blank=False, max_length=20)
    auth_parents = models.IntegerField()
    auth_bonne = models.IntegerField()
    auth_daycarecenter = models.IntegerField()

class user_normal(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=20)
    birthday = models.DateField(blank=True, null=True)
    sex = models.CharField(blank=True, null=True, max_length=1)    
    tips = models.TextField(blank=True, null=True)
    img = models.URLField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=20)
    address = models.TextField(blank=True, null=True)
    user_id = models.IntegerField(unique=True) # models.ForeignKey(user) 

class user_daycarecenter(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    setuptime = models.DateField(blank=True, null=True)             # 托育中心成立時間
    business_philosophy = models.TextField(blank=True, null=True)   # 托育中心經營理念
    diet_plan = models.TextField(blank=True, null=True)             # 托育中心飲食規劃
    learn_plan = models.TextField(blank=True, null=True)            # 托育中心學習規劃
    about_us = models.TextField(blank=True, null=True)              # 托育中心關於我們
    user_id =  models.IntegerField(unique=True) # models.ForeignKey(user)

class user_bonne(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    seniority = models.CharField(blank=True, null=True, max_length=3)   # 保姆年資
    specialty = models.TextField(blank=True, null=True)                 # 保姆專長
    experience = models.TextField(blank=True, null=True)                # 保姆專長
    baby_count_record = models.IntegerField(blank=True, null=True)      # 保姆曾照育寶寶數
    user_id = models.IntegerField(unique=True) # models.ForeignKey(user)
    user_id_daycarecenter = models.IntegerField() # models.ForeignKey(user_daycarecenter)
