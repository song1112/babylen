# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from center.models import center_picture, center_visit
from baby_user.models import user_normal, user_daycarecenter, user_bonne

"""[HTTP POST][Select] 托育中心參訪紀錄的主資料列表
POST VALUE:{"uid","Identify"}
"""
@csrf_exempt
def get_center_record_simple(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            # 尋找參訪過的中心
            centers = center_visit.objects.filter(user_id=data['uid'])
            center_list = []
            for center in centers:
                center_item = {}
                center_data = user_daycarecenter.objects.get(id=user_id_daycarecenter)
                center_item['cid'] = center.user_id_daycarecenter
                center_item['name'] = center_data.name
                # center_item['bonnecount']
                center_item['setuptime'] = center_data.setuptime
                center_item['img'] = center.img
                center_list.append(center_item)
            response_data['datalist'] = center_list
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Select] 托育中心參訪紀錄的詳細內容資料
POST VALUE:{"uid","Identify","cid","datatype"}
"""
@csrf_exempt
def get_center_record_detail(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            center_data = user_daycarecenter.objects.get(id=data['cid'])
            # 0:經營理念,1:飲食規劃,2:環境規劃,3:學習規劃,4:關於我們,5:全部資料
            if data['datatype'] == 0:
                response_data['content'] = center_data.business_philosophy
            elif data['datatype'] == 1:
                response_data['content'] = center_data.diet_plan
            elif (data['datatype'] == 2) or (data['datatype'] == 5):
                center_pics = user_daycarecenter.objects.filter(user_id=center_data.user_id)
                pics_list = []
                for pic in center_pics:
                    pics_list.append(pic.img)
                if data['datatype'] == 2:
                    response_data['imglist'] = pics_list
                else:
                    response_data['environment_plan_imglist'] = pics_list
                    response_data['setuptime'] = center_data.setuptime
                    response_data['business_philosophy'] = center_data.business_philosophy
                    response_data['diet_plan'] = center_data.diet_plan
                    response_data['learn_plan'] = center_data.learn_plan
                    response_data['about_us'] = center_data.about_us
            elif data['datatype'] == 3:
                response_data['content'] = center_data.learn_plan
            elif data['datatype'] == 4:
                response_data['content'] = center_data.about_us
            else:
                response_data['action'] = 1
                response_data['message'] = 'Error: datatype'
        except Exception, ex:
	        response_data['action'] = -1
	        response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Update] 托育中心參訪紀錄的詳細內容資料
POST VALUE:{"uid","Identify","datatype","content","cid"}
POST VALUE:{"uid","Identify":2,"datatype":6,"business_philosophy","diet_plan","learn_plan","about_us"}
"""
@csrf_exempt
def u_center_record_detail(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            if data['datatype'] == 6:
                center = user_daycarecenter.objects.get(id=data['uid'])
                center['business_philosophy'] = data['business_philosophy']
                center['diet_plan'] = data['diet_plan']
                center['learn_plan'] = data['learn_plan']
                center['about_us'] = data['about_us']
                center.save()
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Insert] 條碼掃瞄 父母掃托育中心：參訪記錄新增
POST VALUE:{"uid","Identify","cid"}
"""
@csrf_exempt
def c_barcode_cneter_visit(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            center_picture.objects.create(user_id=data['uid'], user_id_daycarecenter=data['cid'])
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)
