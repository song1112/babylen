# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from baby.models import baby

class get_main_imglist(request):
    return HttpResponse('404 Not Found')

"""[HTTP POST][Select] 主畫面的資料列表
POST VALUE:{"uid","Identify"}
"""
class get_main_datalist(request):
    response_data = {}
    data = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            if(data['Identify']==0):
                baby_list = baby.objects.filter(user_id=data['uid'])
                response_data['action'] = 1

    return HttpResponse('404 Not Found')
