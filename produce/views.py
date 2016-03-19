from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from produce.models import produce_type, produce, produce_trade

"""[HTTP POST][Select] 寶貝商城(含照育權限)的商品列表內容
POST VALUE:{"uid":"00000000001","Identify":0}
RETURN:{"action":1,"typelist":{"MilkPowder":[{"pid","name","money","img"},{"pid","name","money","img"}],"Diapers":[{"pid","name","money","img"},{"pid","name","money","img"}],"care_permission":{"pid","money"}}}
"""
@csrf_exempt
def get_shop_datalist(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        try:
            response_data['action'] = 1
            data = json.loads(request.body)
            typedict = {}
            # 取得奶枌資料
            milk_produce = produce.objects.filter('produce_type_id'=1)
            milk_list = []
            for m_p in milk_produce:
                MilkPowder = {}
                MilkPowder['pid'] = m_p.id
                MilkPowder['name'] = m_p.name
                MilkPowder['money'] = m_p.money
                MilkPowder['img'] = m_p.img
                milk_list.append(MilkPowder)
            typedict['MilkPowder'] = milk_list
            # 取得尿布資料
            diapers_produce = produce.objects.filter('produce_type_id'=2)
            diapers_list = []
            for d_p in diapers_produce:
                Diapers = {}
                Diapers['pid'] = d_p.id
                Diapers['name'] = d_p.name
                Diapers['money'] = d_p.money
                Diapers['img'] = d_p.img
                diapers_list.append(Diapers)
            typedict['Diapers'] = diapers_list
            # 取得尿布資料
            care_produce = produce.objects.filter('produce_type_id'=3)
            care_list = []
            for c_p in care_produce:
                care_permission = {}
                care_permission['pid'] = d_p.id
                care_permission['name'] = d_p.name
                care_permission['money'] = d_p.money
                care_permission['img'] = d_p.img
                care_list.append(care_permission)
            typedict['care_permission'] = care_list
            response_data['typelist'] = typedict
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)
    
"""[HTTP POST][Insert] 寶貝商城交易成功後歐付寶回傳的資料
VALUE:{"uid","Identify","trade_data":{"mainmoney","buylist":[{"pid","count","money"}]},"allpay_data":{"MerchantID","MerchantTradeNo","RtnCode","RtnMsg","TradeNo","TradeAmt","PaymentDate","PaymentType","PaymentTypeChargeFee","TradeDate","SimulatePaid","CheckMacValue"}}
"""
@csrf_exempt
def c_shop_trade(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        try:
            response_data['action'] = 1
            data = json.loads(request.body)
            trade = produce_trade.objects.create(user_id=data['uid'])
            trade.money = data['trade_data']['mainmoney']
            trade.trade_data = data['trade_data']
            trade.allpay_data = data['allpay_data']
            trade.save()
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Select] 使用者購物紀錄清單內容
POST VALUE:{"uid":"00000000001","Identify":0}
RETURN:{"action":1,"datalist":[{"mainmoney","time","itemlist":[{"pid","name","money","count","img"}]},{"mainmoney","time","itemlist":[{"pid","name","money","count","img"}]}]}
"""
@csrf_exempt
def get_shop_tradelist(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            trade = produce_trade.objects.filter(user_id=data['uid'])
            response_data['action'] = 1
            datalist = []
            for t in trade:
                tmpdict = {}
                tmpdict['mainmoney'] = t.money
                tmpdict['time'] = t.createdat.strftime("%Y/%m/%d %H:%M:%S")
                tmpdict['itemlist'] = t.trade_data
                datalist.append(tmpdict)
            response_data['datalist'] = datalist
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)



