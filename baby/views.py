# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import datetime

from baby.models import *

"""[HTTP POST][Insert][Update] 寶寶資料 
POST VALUE:{"uid","Identify","name","birthday","sex","tips","img","height","weight","nickname","bid"}
RETURN:{"action"}
"""
@csrf_exempt
def cu_baby(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            if data.get(bid):
                baby.objects.get(id=data['bid']).update(name=data['name'], birthday=data['birthday'], sex=data['sex'], \
                                 tips=data['tips'], img=data['img'], height=data['height'], weight=data['weight'], \
                                 nickname=data['nickname'])
            else:
                baby.objects.create(birthday=data['birthday'], sex=data['sex'], \
                                    tips=data['tips'], img=data['img'], height=data['height'], weight=data['weight'], \
                                    nickname=data['nickname'], user_id=data['uid'])
            response_data['action'] = 1
            return JsonResponse(response_data)
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Update] 寶寶資料連結取消：從列表中移出該寶寶 
POST VALUE:{"uid","Identify","bid"}
RETURN:{"action"}
"""
@csrf_exempt
def u_baby_relevance_remove(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            baby_data = baby.objects.get(id=data['bid'])
            baby_data.delete()
            response_data['action'] = 1
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Select] 餵奶，副食品，點心、水果，排便，尿布的頁面資料(簡)
POST VALUE:{"uid","Identify","bid"}
POST VALUE:{"uid","Identify","bid","indextime"}
RETURN:{"action","selecttime","BreastFeeding":{"todaycount","finaltime"},"Grocery":{"todaycount","finaltime"},"DessertFruit":{"todaycount","finaltime"},"Defecation":{"todaycount","finaltime"},"Diaper":{"todaycount","finaltime"}}
"""
@csrf_exempt
def get_baby_record_simple(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        response_data['action'] = 0
        try:
            if data.get('indextime'):
                pass
            else:
                today = datetime.date.today()
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Select] 餵奶，副食品，點心、水果，排便，尿布的頁面資料(詳)
POST VALUE:{"uid","Identify","bid","recordtype","indextime"}
"""
@csrf_exempt
def get_baby_record_detail(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    return JsonResponse(response_data)

"""[HTTP POST][Insert][Update] 餵奶，副食品，點心、水果，排便，尿布的資料
POST VALUE:{"uid","Identify","bid","recordtype","newtext"}
POST VALUE:{"uid","Identify","bid","recordtype","newtext","rid"}
"""
@csrf_exempt
def cu_baby_record(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            # update
            if data.get('rid'):
                if data['recordtype'] == 0:  # 餵奶 baby_breastfeeding
                    recode = baby_breastfeeding.objects.get(id=data['rid'])
                    recode.content = data['newtext']
                    recode.save()
                elif data['recordtype'] == 1:  # 副食品 baby_grocery
                    recode = baby_grocery.objects.get(id=data['rid'])
                    recode.content = data['newtext']
                    recode.save()
                elif data['recordtype'] == 2:  # 點心、水果 baby_dessertfruit
                    recode = baby_dessertfruit.objects.get(id=data['rid'])
                    recode.content = data['newtext']
                    recode.save()
                elif data['recordtype'] == 3:  # 排便 baby_defecation
                    recode = baby_defecation.objects.get(id=data['rid'])
                    recode.content = data['newtext']
                    recode.save()
                elif data['recordtype'] == 4:  # 尿布 baby_diaper
                    recode = baby_diaper.objects.get(id=data['rid'])
                    recode.content = data['newtext']
                    recode.save()
                else:
                    response_data['action'] = 0
                    response_data['message'] = 'Error: recordtype'
            # create
            else:
                if data['recordtype'] == 0:  # 餵奶 baby_breastfeeding
                    recode = baby_breastfeeding.objects.create(baby_id=data['bid'], content=data['newtext'])
                elif data['recordtype'] == 1:  # 副食品 baby_grocery
                    recode = baby_grocery.objects.create(baby_id=data['bid'], content=data['newtext'])
                elif data['recordtype'] == 2:  # 點心、水果 baby_dessertfruit
                    recode = baby_dessertfruit.objects.create(baby_id=data['bid'], content=data['newtext'])
                elif data['recordtype'] == 3:  # 排便 baby_defecation
                    recode = baby_defecation.objects.create(baby_id=data['bid'], content=data['newtext'])
                elif data['recordtype'] == 4:  # 尿布 baby_diaper
                    recode = baby_diaper.objects.create(baby_id=data['bid'], content=data['newtext'])
                else:
                    response_data['action'] = 0
                    response_data['message'] = 'Error: recordtype'
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Select] 相機畫面的已上傳圖片網址
POST VALUE:{"uid":"00000000001","Identify":0,"bid":"00000000001"}
POST VALUE:{"uid":"00000000001","Identify":0,"bid":"00000000001","indextime":"2222/2/22"}
{"action","selecttime","imglist":[]}
"""
@csrf_exempt
def get_baby_picture_imglist(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            if data.get('indextime'):
                pics = baby_picture.objects.filter(createdat=data['indextime'], baby_id=data['bid'])
                pics_list = []
                for pic in pics:
                    pics_list.append(pic.img)
                response_data['imglist'] = pics_list
                response_data['selecttime'] = data['indextime']
            else:
                pics = baby_picture.objects.filter(baby_id=data['bid'])
                pics_list = []
                for pic in pics:
                    pics_list.append(pic.img)
                response_data['imglist'] = pics_list
                response_data['selecttime'] = "all"
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Insert] 相機畫面的 +photo 按鈕選擇的圖片
POST VALUE:{"uid","Identify","bid","img"}
"""
@csrf_exempt
def c_baby_picture(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    return JsonResponse(response_data)

"""[HTTP POST][Select] 寶寶聊天室的聊天人資料
POST VALUE:{"uid":"1","Identify":0,"bid":"1"}
"""
@csrf_exempt
def get_baby_chat_datalist(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    return JsonResponse(response_data)

def get_chart_baby_datalist(request):
    return HttpResponse('404 Not Found')

"""[HTTP POST][Update] 托育中心更新多個寶寶到某保姆名下
POST VALUE:{"uid":"00000000001","Identify":2,"mid":"00000000001","bid_text":"1,2,3"}
"""
@csrf_exempt
def u_baby_relevance_b2m(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            if data['Identify'] == 2:
                # 分割寶寶id
                bid_list = data['bid_text'].split(',')
                for bid in bid_list:
                    # 新增保母id到寶寶
                    baby_data = baby.objects.get(id=int(bid))
                    baby_data.user_id_bonne = data['mid']
                    baby_data.save()
                response_data['action'] = 1
            else:
                response_data['message'] = 'Permission denied'
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

