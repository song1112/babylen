# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from baby_user.models import user, user_daycarecenter, PathAndRename

class center_picture(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to=PathAndRename('image/center_picture/'), blank=True, null=True)
    user_id = models.IntegerField() # models.ForeignKey(user)


class center_visit(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField() # models.ForeignKey(user)
    user_id_daycarecenter = models.IntegerField() # models.ForeignKey(user_daycarecenter)

