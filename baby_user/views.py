# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from baby_user.models import user, user_normal, user_daycarecenter, user_bonne
from baby.models import baby

""" [HTTP POST][Select] 使用者登入
POST VALUE:[account, password, Identify]
"""
@csrf_exempt
def login(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
		data = json.loads(request.body)
    try:
        query_u = user.objects.get(account=data['account'])
        if (data['Identify']==0 and query_u.auth_parents==1) or \
           (data['Identify']==1 and query_u.auth_bonne==1) or \
           (data['Identify']==2 and query_u.auth_daycarecenter==1):
           response_data['action'] = 1
           response_data['uid'] = query_u.id
           response_data['Identify_parents'] = query_u.auth_parents
           response_data['Identify_bonne'] = query_u.auth_bonne 
           response_data['Identify_daycarecenter'] = query_u.auth_daycarecenter
        else:
           response_data['action'] = 0
           response_data['message'] = 'Permission denied'
    except Exception, ex:
	    response_data['action'] = -1
	    response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)



""" [HTTP POST][Insert] 使用者註冊
"""
@csrf_exempt
def register(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            reg_user = user.objects.create(account=data['account'], password=data['password'], \
                auth_parents=data['Identify_parents'], auth_bonne=data['Identify_bonne'], \
                auth_daycarecenter=data['Identify_daycarecenter'])
            user_normal.objects.create(email=data['email'], user_id=reg_user.id)
            # 如果有保母權限則建立保母資料
            if data['Identify_bonne']==1:
                user_bonne.objects.create(user_id=reg_user.id)
            # 如果有中心權限則建立保母資料
            if data['Identify_daycarecenter']==1:
                user_daycarecenter.objects.create(user_id=reg_user.id)
            response_data['action'] = 1
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)



""" [HTTP POST][Select] 使用者個人資料
POST VALUE:{"uid":"00000000001","Identify":0}
RETURN:{"action","normal":{"email","name","birthday","sex","tips","img","phone":,"address"},
        "bonne":{"seniority","baby_count_record","specialty","experience"},
        "daycare_center":{"setuptime","business_philosophy","diet_plan","environment_plan_imglist","learn_plan","about_us"}}}
"""
@csrf_exempt
def get_user_datalist(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            u_data = user_normal.objects.get(user_id=data['uid'])
            resp_normal = {}
            response_data['action'] = 1
            resp_normal['email'] = u_data.email
            resp_normal['name'] = u_data.name
            resp_normal['birthday'] = u_data.birthday
            resp_normal['sex'] = u_data.sex
            resp_normal['tips'] = u_data.tips
            resp_normal['img'] = u_data.img.url
            resp_normal['phone'] = u_data.phone
            resp_normal['address'] = u_data.address
            response_data['normal'] = resp_normal
            if data['Identify']==1:
                b_data = user_bonne.objects.get(user_id=data['uid'])
                resp_bonne = {}
                resp_bonne['seniority'] = b_data.seniority
                resp_bonne['baby_count_record'] = b_data.baby_count_record
                resp_bonne['specialty'] = b_data.specialty
                resp_bonne['experience'] = b_data.experience
                response_data['bonne'] = resp_bonne
            elif data['Identify']==2:
                resp_center = {}
                c_data = user_daycarecenter.objects.get(user_id=data['uid'])
                resp_center['setuptime'] = c_data.setuptime
                resp_center['business_philosophy'] = c_data.business_philosophy
                resp_center['diet_plan'] = c_data.diet_plan
                # response_data['environment_plan_imglist'] = 
                resp_center['learn_plan'] = c_data.learn_plan
                resp_center['about_us'] = c_data.about_us
                response_data['daycare_center'] = resp_center
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)



""" [HTTP POST][Update] 使用者更新個人資料
POST VALUE:{"uid","Identify","email","name","birthday","sex","tips","img","phone","address"}
RETURN:{"action"}
"""
@csrf_exempt
def u_user_datalist(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            un_data = user_normal.objects.get(user_id=data['uid'])
            un_data.email = data['email']
            un_data.phone=data['phone']
            un_data.address=data['address']
            un_data.save()
                                #    birthday=data['birthday'], sex=data['sex'], tips=['tips']\
                                #    img=['img'], name=data['name'])
            if data['Identify']==1:
                data['baby_count_record'] = int(data['baby_count_record'])
                data['specialty'] = int(data['specialty'])
                ub_data = user_bonne.objects.get(user_id=data['uid'])
                ub_data.seniority = data['seniority']
                ub_data.baby_count_record = data['baby_count_record']
                ub_data.specialty=data['specialty']
                ub_data.experience=data['experience']
                ub_data.save()

        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Update] 條碼掃瞄 托育中心掃保母：托育中心新增保母到該名下
POST VALUE:{"uid","Identify","mid"}
"""
@csrf_exempt
def u_barcode_relevance_m2c(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            # 找到托育中心
            center_data = user_daycarecenter.objects.get(user_id=data['uid'])
            # 找到保姆
            bonner_data = user_bonne.objects.get(user_id=data['uid'])
            # 新增托育中心id到保姆托育中心id
            bonner_data.user_id_daycarecenter = center_data.id
            bonner_data.save()
            response_data['action'] = 1
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Update] 條碼掃瞄 保母掃寶寶：保母新增寶寶到該名下
POST VALUE:{"uid":"00000000001","Identify":1,"bid":"00000002221"}
"""
@csrf_exempt
def u_barcode_relevance_b2m(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            # 找到寶寶
            baby_data = baby.objects.get(id=data['bid'])
            # 找到保姆
            bonner_data = user_bonne.objects.get(user_id=data['uid'])
            # 新增保姆id到寶寶的保姆id
            baby_data.user_id_bonne = bonner_data.id
            baby_data.save()
            response_data['action'] = 1
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Update] 條碼掃瞄 父母掃寶寶：父母新增寶寶到該名下
POST VALUE:{"uid":"00000000001","Identify":0,"bid":"00000002221"}
"""
@csrf_exempt
def u_barcode_relevance_b2p(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            # 找到寶寶
            baby_data = baby.objects.get(id=data['bid'])
            # 新增id到寶寶的父母id
            baby_data.user_id = data['uid']
            baby_data.save()
            response_data['action'] = 1
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Update] 條碼掃瞄 托育中心掃寶寶：托育中心新增寶寶到該名下
POST VALUE:{"uid","Identify","bid"}
"""
@csrf_exempt
def u_barcode_relevance_b2c(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            # 找到寶寶
            baby_data = baby.objects.get(id=data['bid'])
            # 找到托育中心
            center_data = user_daycarecenter.objects.get(user_id=data['uid'])
            # 新增id到寶寶的托育中心id
            baby_data.user_id_daycarecenter = center_data.id
            baby_data.save()
            response_data['action'] = 1
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Select] 所有寶寶清單的資料列表
POST VALUE:{"uid":"00000000001","Identify":2}
POST VALUE:{"uid":"00000000001","Identify":2,"mid":"00000000001"}
RETURN:{"action":1,"typelist":[{"bonne","img","mid","datalist":{"datalist":[{"bid","name","img"}]}
"""
@csrf_exempt
def get_baby_datalist(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            if data['Identify'] == 2:
                # 找到該托育中心的所有保姆
                c_data = user_daycarecenter.objects.get(user_id=data['uid'])
                bonnes_data = user_bonne.objects.filter(user_id_daycarecenter=c_data.id)
                bonnes_list = [] # 儲存托育中心旗下所有保母
                for bonne_data in bonnes_data:
                    bonne_item = {}
                    bonne_item['mid'] = bonne_data.id
                    u_data = user_normal.objects.get(id=bonne_data.user_id)
                    bonne_item['name'] = u_data.name
                    bonne_item['img'] = u_data.img.url
                    # 找到保母旗下的所有寶寶
                    babys_data = baby.objects.filter(user_id_bonne=bonne_data.id)
                    babys_list = []  # 儲存保母旗下所有寶寶
                    # 列出寶寶要回傳的資料
                    for baby_data in babys_data:
                        baby_item = {}
                        baby_item['bid'] = baby_data.id
                        baby_item['name'] = baby_data.name
                        baby_item['img'] = baby_data.img
                        babys_list.append(baby_item)
                    bonne_item['datalist'] = babys_list  # 儲存保母旗下寶寶資料
                    bonnes_list.append(bonne_item)
                response_data['typelist'] = bonnes_list # 儲存中心旗下保母資料
                response_data['action'] = 1
            else:
                response_data['message'] = 'Permission denied'
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

from PIL import ImageFile
from django.core.files import File
from django.core.files.base import ContentFile
"""
POST VALUE: file, uid
"""
@csrf_exempt
def updata_user_pic(request):
    response_data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        try:
            uid = request.POST['uid']
            response_data['action'] = -2
            resizedImage = resize_uploaded_image(request.FILES['uploaded_file'])
            content = File(resizedImage)
            #file_content = ContentFile(resize_uploaded_image(request.FILES['uploaded_file']).read)
            u_data = user_normal.objects.get(user_id=uid)
            response_data['action'] = 0
            u_data.img.save(uid+request.FILES['uploaded_file'].name, content)
            response_data['action'] = 1
            response_data['message'] = 'updata_user_pic success'
        except Exception, ex:
            #response_data['action'] = -1
            response_data['message'] = ex.message
    return JsonResponse(response_data)

"""取得中心旗下的所有保母
POST VALUE: uid
RETURN: {datalist:[boid,uid,name,seniority,specialty,experience,baby_count_record]}
"""
@csrf_exempt
def get_center_bonne(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            bonnes = user_bonne.objects.filter(user_id_daycarecenter=user_daycarecenter.objects.get(user_id=data['uid']).id)
            datalist = []
            for b in bonnes:
                datadict = {}
                datadict['boid'] = b.user_id
                datadict['uid'] = b.user_id
                datadict['name'] = user_normal.objects.get(id=data['uid']).name
                datadict['seniority'] = b.seniority
                datadict['specialty'] = b.specialty
                datadict['experience'] = b.experience
                datadict['baby_count_record'] = b.baby_count_record
                datalist.append(datadict)
            response_data['datalist'] = datalist
            response_data['action'] = 1
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = ex.message
    return JsonResponse(response_data)


import StringIO
from PIL import Image
def resize_uploaded_image(buf):
    image = Image.open(buf)

    (width, height) = image.size
    #(width, height) = scale_dimensions(width, height, longest_side=240)

    resizedImage = image.resize((180, 180))

    # Turn back into file-like object
    resizedImageFile = StringIO.StringIO()
    resizedImage.save(resizedImageFile , 'PNG', optimize = True)
    resizedImageFile.seek(0)    # So that the next read starts at the beginning

    return resizedImageFile
