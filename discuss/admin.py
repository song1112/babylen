from django.contrib import admin
from discuss.models import *

class discuss_typeAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'name')

class discussAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'title', 'content', 'discuss_type_id', 'user_id')

class discuss_messageAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'content', 'discuss_id', 'user_id')

admin.site.register(discuss_type, discuss_typeAdmin)
admin.site.register(discuss, discussAdmin)
admin.site.register(discuss_message, discuss_messageAdmin)

