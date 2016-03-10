from django.contrib import admin
from notification.models import *

admin.site.register(notification_apns)
admin.site.register(notification_gcm)
