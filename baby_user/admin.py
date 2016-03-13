from django.contrib import admin
from baby_user.models import user, user_normal, user_daycarecenter, user_bonne 

class userAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'account', 'password', 'auth_parents', 'auth_bonne', 'auth_daycarecenter')

admin.site.register(user, userAdmin)
admin.site.register(user_normal)
admin.site.register(user_daycarecenter)
admin.site.register(user_bonne)


