from django.contrib import admin
from discuss.models import *

admin.site.register(discuss_type)
admin.site.register(discuss)
admin.site.register(discuss_message)

