# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from center.models import center_picture, center_visit
from baby_user.models import user_normal, user_daycarecenter, user_bonne
from baby_user.views import resize_uploaded_image

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
                center_data = user_daycarecenter.objects.get(id=center.user_id_daycarecenter)
                center_item['cid'] = center.user_id_daycarecenter
                cu = user_daycarecenter.objects.get(id=center_item['cid'])
                u = user_normal.objects.get(user_id=cu.user_id)
                center_item['name'] = u.name
                center_item['uid'] = u.user_id
                b = user_bonne.objects.filter(user_id_daycarecenter=center_item['cid'])
                center_item['bonnecount'] = b.count()
                if center_data.setuptime:
                    center_item['setuptime'] = center_data.setuptime
                else:
                    center_item['setuptime'] = 1
                center_item['img'] = "" # center.img
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
                if center_data.business_philosophy:
                    response_data['content'] = center_data.business_philosophy
                else:
                    response_data['content'] = ""
            elif data['datatype'] == 1:
                if center_data.diet_plan:
                    response_data['content'] = center_data.diet_plan
                else:
                    response_data['content'] = ""
            elif (data['datatype'] == 2) or (data['datatype'] == 5):
                center_pics = center_picture.objects.filter(user_id=center_data.user_id)
                pics_list = []
                for pic in center_pics:
                    pics_list.append(pic.img.url)
                if data['datatype'] == 2:
                    if pics_list:
                        response_data['imglist'] = pics_list
                    else:
                        response_data['imglist'] = ""
                else:
                    response_data['environment_plan'] = pics_list
                    if center_data.setuptime:
                        response_data['setuptime'] = center_data.setuptime
                    else:
                        response_data['setuptime'] = ""
                    if center_data.business_philosophy:
                        response_data['business_philosophy'] = center_data.business_philosophy
                    else:
                        response_data['business_philosophy'] = ""
                    if center_data.diet_plan:
                        response_data['diet_plan'] = center_data.diet_plan
                    else:
                        response_data['diet_plan'] = ""
                    if center_data.learn_plan:
                        response_data['learn_plan'] = center_data.learn_plan
                    else:
                        response_data['learn_plan'] = ""
                    if center_data.about_us:
                        response_data['about_us'] = center_data.about_us
                    else:
                        response_data['about_us'] = ""
            elif data['datatype'] == 3:
                if center_data.learn_plan:
                    response_data['content'] = center_data.learn_plan
                else:
                    response_data['content'] = ""
            elif data['datatype'] == 4:
                if center_data.about_us:
                    response_data['content'] = center_data.about_us
                else:
                    response_data['content'] = ""
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
            data['datatype'] = int(data['datatype'])
            if data['datatype'] == 6:
                u_c = user_daycarecenter.objects.get(user_id=data['uid'])
                u_c.business_philosophy = data['business_philosophy']
                u_c.diet_plan = data['diet_plan']
                u_c.learn_plan = data['learn_plan']
                u_c.about_us = data['about_us']
                u_c.save()
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
            c = user_daycarecenter.objects.get(user_id=data['cid'])
            data['cid'] = c.id
            # 查詢參訪紀錄是否有被創建
            if not center_visit.objects.filter(user_id=data['uid'], user_id_daycarecenter=data['cid']).exists():
                center_visit.objects.create(user_id=data['uid'], user_id_daycarecenter=data['cid'])
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

from PIL import ImageFile
from django.core.files import File
from django.core.files.base import ContentFile

"""
"""
@csrf_exempt
def updata_center_pic(request):
    response_data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        try:
            uid = request.POST['cpid']
            resizedImage = resize_uploaded_image(request.FILES['uploaded_file'])
            content = File(resizedImage)
            center_pic = center_picture.objects.create(user_id=uid)
            center_pic.img.save(uid+request.FILES['uploaded_file'].name, content)
            response_data['action'] = 1
            response_data['message'] = 'updata_center_pic success'
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = ex.message
    return JsonResponse(response_data)
