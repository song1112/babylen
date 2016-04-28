from django.contrib import admin
from baby.models import *

class babyAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'name', 'birthday', \
                    'sex', 'tips', 'img', 'height', 'weight', 'nickname', \
                    'user_id', 'user_id_father', 'user_id_mother', \
                    'user_id_bonne', 'user_id_daycarecenter')

class baby_barcodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'user_id', 'identify', 'baby_id')

class baby_breastfeedingAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'content', 'baby_id')

class baby_chatAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'user_id', 'identify', 'message', 'baby_id')

class baby_defecationAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'content', 'baby_id')

class baby_dessertfruitAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'content', 'baby_id')
class baby_diaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'content', 'baby_id')

class baby_groceryAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'content', 'baby_id')
    
class baby_pictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'img', 'baby_id')

class baby_relativesAdmin(admin.ModelAdmin): 
    list_display = ('id', 'createdat', 'updatedat', 'user_id', 'baby_id')

class care_recordAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'bonne_id', 'baby_id', 'sex')

admin.site.register(baby, babyAdmin)
admin.site.register(baby_barcode, baby_barcodeAdmin)
admin.site.register(baby_breastfeeding, baby_breastfeedingAdmin)
admin.site.register(baby_chat, baby_chatAdmin)
admin.site.register(baby_defecation, baby_defecationAdmin)
admin.site.register(baby_dessertfruit, baby_dessertfruitAdmin)
admin.site.register(baby_diaper, baby_diaperAdmin)
admin.site.register(baby_grocery, baby_groceryAdmin)
admin.site.register(baby_picture, baby_pictureAdmin)
admin.site.register(baby_relatives, baby_relativesAdmin)
admin.site.register(care_record, care_recordAdmin)
