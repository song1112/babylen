# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from discuss.models import discuss_type, discuss, discuss_message
from baby_user.models import user_normal

from django.core.files.base import ContentFile

"""[HTTP POST][Select] 照育討論區的討論串資料列表
POST VALUE:{"uid":"00000000001","Identify":0}
RETURN:{"action","datalist":[{"fid","name"}]}
"""
@csrf_exempt
def get_discuss_group_datalist(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            d_data = discuss.objects.all()
            d_list = []
            for d in d_data:
                d_item = {}
                d_item['fid'] = d.id
                d_item['name'] = d.title
                d_list.append(d_item)
            response_data['datalist'] = d_list
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Select] 照育討論區的討論文章資料列表
POST VALUE:{"uid":"00000000001","Identify":0,"fid":"00000000001"}
"""
@csrf_exempt
def get_discuss_article_datalist(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            d_topic = discuss.objects.get(id=data['fid'])
            d_data = discuss_message.objects.filter(discuss_id=data['fid'])
            response_data['title'] = d_topic.title
            response_data['name'] = "test"
            response_data['imglist'] = ""
            response_data['content'] = d_topic.content
            response_data['time'] = d_topic.createdat
            d_list = []
            for d in d_data:
                imglist = []
                if (d.img):
                    imglist.append(d.img.url)
                if (d.img2):
                    imglist.append(d.img2.url)
                if (d.img3):
                    imglist.append(d.img3.url)
                d_item = {}
                d_item['content'] = d.content
                # u_name = user_normal.objects.get(user_id=data['uid'])
                d_item['time'] = d.updatedat
                d_item['name'] = "test"
                d_item['imglist'] = imglist
                d_list.append(d_item)
            response_data['datalist'] = d_list
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Insert] 照育討論區的討論串
POST VALUE:{"uid","Identify","title","img1","img2","img3","content"}
"""
@csrf_exempt
def c_discuss_group(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            discuss.objects.create(title=data['title'], content=data['content'], user_id=data['uid'])
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

""""[HTTP POST][Insert] 照育討論區的討論文章訊息
POST VALUE:{"uid","Identify","fid","img1","img2","img3","content"}
"""
@csrf_exempt
def c_discuss_article(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            d_m = discuss_message.objects.create(discuss_id=data['fid'], content=data['content'], user_id=data['uid'])
            response_data['mid'] = d_m.id
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
    return JsonResponse(response_data)

"""上傳討論區照片
POST VALUE:{"uid","mid","img1","img2","img3"}
"""
@csrf_exempt
def updata_discuss_pic(request):
    response_data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        try:
            mid = request.POST['mid']
            file_content = ContentFile(request.FILES['uploaded_file'].read())
            m_data = discuss_message.objects.get(id=mid)
            m_data.img.save(mid+request.FILES['uploaded_file'].name, file_content)
            response_data['action'] = 1
            response_data['message'] = 'updata_discuss_pic success'
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = ex.message
    return JsonResponse(response_data)
