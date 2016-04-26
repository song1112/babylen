from django.contrib import admin
from baby_user.models import user, user_normal, user_daycarecenter, user_bonne, header_pic

class userAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'account', 'password', \
                    'auth_parents', 'auth_bonne', 'auth_daycarecenter')

class user_normalAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'name', 'birthday','sex', \
                    'tips', 'img', 'phone', 'address', 'user_id')

class user_daycarecenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'business_philosophy',  \
                    'diet_plan', 'learn_plan', 'about_us', 'user_id', 'baby_auth')

class user_bonneAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'seniority', 'specialty',  \
                    'experience', 'baby_count_record', 'user_id', 'user_id_daycarecenter', 'baby_auth')

class header_picAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'img')

admin.site.register(user, userAdmin)
admin.site.register(user_normal, user_normalAdmin)
admin.site.register(user_daycarecenter, user_daycarecenterAdmin)
admin.site.register(user_bonne, user_bonneAdmin)
admin.site.register(header_pic, header_picAdmin)

