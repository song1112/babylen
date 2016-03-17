# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from baby.models import baby

@csrf_exempt
def get_main_imglist(request):
    return HttpResponse('404 Not Found')

"""[HTTP POST][Select] 主畫面的資料列表
POST VALUE:{"uid","Identify"}
"""
@csrf_exempt
def get_main_datalist(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            if(data['Identify']==0):
                baby_list = baby.objects.filter(user_id=data['uid'])
                baby_coll = []  # babys data list
                for baby_item in baby_list:
                    baby_data = {}  # baby data dict
                    baby_data['bid'] = baby_item.id
                    baby_data['name'] = baby_item.name
                    baby_data['birthday'] = baby_item.birthday
                    baby_data['img'] = baby_item.img.url
                    baby_data['sex'] = baby_item.sex
                    baby_data['height'] = baby_item.height
                    baby_data['weight'] = baby_item.weight
                    baby_data['nickname'] = baby_item.nickname
                    baby_data['bonne'] = baby_item.user_id_bonne
                    baby_data['tips'] = baby_item.tips
                    baby_coll.append(baby_data)
                response_data['datalist'] = baby_coll
                response_data['action'] = 1
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)
