from __future__ import unicode_literals

from django.db import models
from baby_user.models import user 

class discuss_type(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    name = models.CharField(blank=False, max_length=20)

class discuss(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    title = models.CharField(blank=False, max_length=30)
    content = models.TextField()
    discuss_type_id = models.IntegerField() # models.ForeignKey(discuss_type)
    user_id = models.IntegerField() # models.ForeignKey(user)

class discuss_message(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    content = models.TextField()
    discuss_id = models.IntegerField() # models.ForeignKey(discuss)
    user_id = models.IntegerField() # models.ForeignKey(user) 
