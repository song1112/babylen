from django.contrib import admin
from produce.models import *

class produce_typeAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'name')

class produceAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'name', 'price', 'img', 'produce_type_id')

class produce_tradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'createdat', 'updatedat', 'money', 'trade_data', 'allpay_data', 'user_id')

admin.site.register(produce_type, produce_typeAdmin)
admin.site.register(produce, produceAdmin)
admin.site.register(produce_trade, produce_tradeAdmin)
