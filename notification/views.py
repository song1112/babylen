# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from notification.models import notification_apns, notification_gcm

"""[HTTP POST][Update] 推播裝置資料新增修改
POST VALUE:{"provider","useragent","deviceid","user_id", "token"}
"""
@csrf_exempt
def cu_notification_id(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            # [0:GCM, 1:APNS]
            if data['provider'] == 0:
                notification_gcm.objects.create(token=data['token'], user_id=data['user_id'])    
            elif data['provider'] == 1:
                notification_apns.objects.create(useragent=data['useragent'], deviceid=data['deviceid'], user_id=data['user_id'])
            else:
                response_data['action'] = 0
                response_data['message'] = 'Error: provider'
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Select] 推播裝置資料查看
POST VALUE:{"provider":0}
"""
@csrf_exempt    
def get_notification_datalist(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            # [0:GCM, 1:APNS]
            all_list = []
            if data['provider'] == 0:
                all_data = notification_gcm.objects.all()
                for gcm in all_data:
                    gcm_item = {}
                    gcm_item['id'] = gcm.id
                    gcm_item['createdat'] = gcm.createdat
                    gcm_item['updatedat'] = gcm.updatedat
                    gcm_item['token'] = gcm.token
                    gcm_item['user_id'] = gcm.user_id
                    all_list.append(gcm_item)
                response_data['datalist'] = all_list
            elif data['provider'] == 1:
                all_data = notification_apns.objects.all()
                for gcm in all_data:
                    gcm_item = {}
                    gcm_item['id'] = gcm.id
                    gcm_item['createdat'] = gcm.createdat
                    gcm_item['updatedat'] = gcm.updatedat
                    gcm_item['useragent'] = gcm.useragent
                    gcm_item['deviceid'] = gcm.deviceid
                    gcm_item['user_id'] = gcm.user_id
                    all_list.append(gcm_item)
                response_data['datalist'] = all_list
            else:
                response_data['action'] = 0
                response_data['message'] = 'Error: provider'
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)
