# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from baby_user.models import user, user_normal, user_daycarecenter, user_bonne
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


""" [HTTP POST][Select] 使用者登入
POST VALUE:[account, password, Identify]
"""
@csrf_exempt
def login(request):
    response_data = {}
    data = {}
    if request.method == 'POST':
	data = json.loads(request.body)
	try:
    	    query_u = user.objects.get(account=data['account'])
            if (data['Identify']==0 && query_u.auth_parents==1) ||
               (data['Identify']==1 && query_u.auth_bonne==1) ||
               (data['Identify']==2 && query_u.auth_daycarecenter==1): 
                response_data['action'] = 1
                response_data['uid'] = query_u.id
                response_data['Identify_parents'] = query_u.auth_parents
                response_data['Identify_bonne'] = query_u.auth_bonne 
                response_data['Identify_daycarecenter'] = query_u.auth_daycarecenter
            else:
                response_data['action'] = 0
                response_data['message'] = 'Permission denied'
            return JsonResponse(response_data)
	except Exception, ex:
	    response_data['action'] = -1
	    response_data['message'] = 'Error:' + ex.message
	    return JsonResponse(response_data)
	return HttpResponse('404 Not Found')



""" [HTTP POST][Insert] 使用者註冊
"""
@csrf_exempt
def register(request):
	response_data = {}
	data = {}
	if request.method == 'POST':
	    data = json.loads(request.body)
        try:
            reg_user = user.objects.create(account=data['account'], password=data['password'], \
                auth_parents=data['Identify_parents'], auth_bonne=data['Identify_bonne'], \
                auth_daycarecenter=data['Identify_daycarecenter'])
            user_info = user_normal.objects.create(email=data['email'], user_id=reg_user.id)
            response_data['action'] = 1
            response_data['message'] = 'success'
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
	    return JsonResponse(response_data)
	return HttpResponse('404 Not Found')



""" [HTTP POST][Select] 使用者個人資料
POST VALUE:{"uid":"00000000001","Identify":0}
RETURN:{"action","normal":{"email","name","birthday","sex","tips","img","phone":,"address"},
        "bonne":{"seniority","baby_count_record","specialty","experience"},
        "daycare_center":{"setuptime","business_philosophy","diet_plan","environment_plan_imglist","learn_plan","about_us"}}}
"""
@csrf_exempt
class get_user_datalist(request):
    response_data = {}
    data = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            u_data = user_normal.objects.get(user_id=data['uid'])
            response_data['action'] = 1
            response_data['email'] = u_data.email
            response_data['name'] = u_data.name
            response_data['birthday'] = u_data.birthday
            response_data['sex'] = u_data.sex
            response_data['tips'] = u_data.tips
            response_data['img'] = u_data.img
            response_data['phone'] = u_data.phone
            response_data['address'] = u_data.address
            if data['Identify']==0:
                return JsonResponse(response_data)
            else if data['Identify']==1:
                b_data = user_bonne.objects.get(user_id=data['uid'])
                response_data['seniority'] = b_data.seniority
                response_data['baby_count_record'] = b_data.baby_count_record
                response_data['specialty'] = b_data.specialty
                response_data['experience'] = b_data.experience
                return JsonResponse(response_data)
            else if data['Identify']==2:
                c_data = user_bonne.objects.get(user_id=data['uid'])
                response_data['setuptime'] = c_data.setuptime
                response_data['business_philosophy'] = c_data.business_philosophy
                response_data['diet_plan'] = c_data.diet_plan
                # response_data['environment_plan_imglist'] = 
                response_data['learn_plan'] = c_data.learn_plan
                response_data['about_us'] = c_data.about_us
                return JsonResponse(response_data)
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
	    return JsonResponse(response_data)
    return HttpResponse('404 Not Found')



""" [HTTP POST][Update] 使用者更新個人資料
POST VALUE:{"uid","Identify","email","name","birthday","sex","tips","img","phone","address"}
RETURN:{"action"}
"""
@csrf_exempt
class u_user_datalist(request):
    response_data = {}
    data = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user_normal.objects.get(user_id=data['uid']).update(email=data['email'], name=data['name'], tips=['tips'], \
                                    birthday=data['birthday'], sex=data['sex'], address=['address'], \
                                    img=['img'], phone=['phone'])
            if data['Identify']==1:
                user_bonne.objects.get(user_id=data['uid']).update(seniority=data['seniority'], \
                                       baby_count_record=data['baby_count_record'], specialty=data['specialty'], \
                                       experience=data['experience'])
            return JsonResponse(response_data)
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
	    return JsonResponse(response_data)
    return HttpResponse('404 Not Found')
