from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from produce.models import produce_type, produce, produce_trade

"""[HTTP POST][Select] 寶貝商城(含照育權限)的商品列表內容
POST VALUE:{"uid":"00000000001","Identify":0}
"""
@csrf_exempt
def get_shop_datalist(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    return JsonResponse(response_data)
    
"""[HTTP POST][Insert] 寶貝商城交易成功後歐付寶回傳的資料
VALUE:{"uid","Identify","trade_data":{"mainmoney","buylist":[{"pid","count","money"}]},"allpay_data":{"MerchantID","MerchantTradeNo","RtnCode","RtnMsg","TradeNo","TradeAmt","PaymentDate","PaymentType","PaymentTypeChargeFee","TradeDate","SimulatePaid","CheckMacValue"}}
"""
@csrf_exempt
def c_shop_trade(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    return JsonResponse(response_data)

"""[HTTP POST][Select] 使用者購物紀錄清單內容
POST VALUE:{"uid":"00000000001","Identify":0}
"""
@csrf_exempt
def get_shop_tradelist(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    return JsonResponse(response_data)



