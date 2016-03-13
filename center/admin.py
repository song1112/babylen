from django.contrib import admin
from center.models import *

class center_pictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'img', 'user_id')

class center_visitAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'user_id', 'user_id_daycarecenter')

admin.site.register(center_picture, center_pictureAdmin)
admin.site.register(center_visit, center_visitAdmin)
