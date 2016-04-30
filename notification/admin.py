from django.contrib import admin
from notification.models import *

class notification_apnsAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'useragent', 'deviceid', 'user_id')

class notification_gcmAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'token', 'user_id')

admin.site.register(notification_apns, notification_apnsAdmin)
admin.site.register(notification_gcm, notification_gcmAdmin)
