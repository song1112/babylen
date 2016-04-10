# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from baby_user.models import user, PathAndRename 
from babylen  import settings

class baby(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    name = models.CharField(blank=False, max_length=20, default="")
    birthday = models.DateField(null=True)
    sex = models.CharField(blank=True, null=True, max_length=2, default=0) 
    tips = models.TextField(blank=True, null=True, default="")
    img = models.ImageField(upload_to=PathAndRename('image/baby/'), blank=True, null=True)
    height = models.CharField(blank=True, null=True, max_length=10, default="")
    weight = models.CharField(blank=True, null=True, max_length=10, default="")
    nickname = models.CharField(blank=True, max_length=20, default="")
    user_id = models.IntegerField(blank=True, null=True)
    user_id_father = models.IntegerField(blank=True, null=True)
    user_id_mother = models.IntegerField(blank=True, null=True)
    user_id_bonne = models.IntegerField(blank=True, null=True)
    user_id_daycarecenter = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name


# 寶寶掃條碼紀錄
class baby_barcode(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField()
    identify = models.CharField(blank=True, null=True, max_length=1)    # 條碼的使用者身份別
    baby_id = models.IntegerField() # models.ForeignKey(baby)

# 寶寶日誌之餵奶
class baby_breastfeeding(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    content = models.CharField(blank=True, null=True, max_length=30, default="")    # 餵奶內容 
    baby_id = models.IntegerField() # models.IntegerField(unique=True) # models.ForeignKey(baby)

# 寶寶聊天記錄
class baby_chat(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    identify = models.CharField(blank=True, null=True, max_length=1)    # 聊天使用者身份別
    message = models.CharField(max_length=500)
    user_id = models.IntegerField() # models.ForeignKey(user)
    baby_id = models.IntegerField() # models.ForeignKey(baby)

# 寶寶日誌之排便
class baby_defecation(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    content = models.CharField(blank=True, null=True, max_length=30, default="")
    baby_id = models.IntegerField() # models.ForeignKey(baby)

#  寶寶日誌之點心水果
class baby_dessertfruit(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    content = models.CharField(blank=True, null=True, max_length=30, default="")
    baby_id = models.IntegerField() # models.ForeignKey(baby)

#  寶寶日誌之尿布
class baby_diaper(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    content = models.CharField(blank=True, null=True, max_length=30, default="")
    baby_id = models.IntegerField() # models.ForeignKey(baby)

# 寶寶日誌之副食品
class baby_grocery(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    content = models.CharField(blank=True, null=True, max_length=30, default="")
    baby_id = models.IntegerField() # models.ForeignKey(baby)

class baby_picture(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to=PathAndRename('image/baby_picture/'), blank=True, null=True)
    baby_id = models.IntegerField() # models.ForeignKey(baby)

# 寶寶親戚(寶寶聊天室可看但不能發言者)
class baby_relatives(models.Model):
    id = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    baby_id = models.IntegerField() # models.ForeignKey(baby)
    user_id = models.IntegerField() # models.ForeignKey(user)

