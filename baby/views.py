from django.shortcuts import render
from baby.models import *

"""[HTTP POST][Insert][Update] 寶寶資料 
POST VALUE:{"uid","Identify","name","birthday","sex","tips","img","height","weight","nickname","bid"}
RETURN:{"action"}
"""
class cu_baby(request):
    response_data = {}
    data = {}
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

    return HttpResponse('404 Not Found')

"""[HTTP POST][Update] 寶寶資料連結取消：從列表中移出該寶寶 
POST VALUE:{"uid","Identify","bid"}
RETURN:{"action"}
"""
class u_baby_relevance_remove(request):
    response_data = {}
    data = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            baby_data = baby.objects.get(id=data['bid'])
            baby_data.delete()
            response_data['action'] = 1
            return JsonResponse(response_data)
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'Error:' + ex.message
            return JsonResponse(response_data)
    return HttpResponse('404 Not Found')

class get_baby_record_simple(request):
    return HttpResponse('404 Not Found')

class get_baby_record_detail(request):
    return HttpResponse('404 Not Found')
    
class cu_baby_record(request):
    return HttpResponse('404 Not Found')

class get_baby_picture_imglist(request):
    return HttpResponse('404 Not Found')

class c_baby_picture(request):
    return HttpResponse('404 Not Found')

class get_baby_chat_datalist(request):
    return HttpResponse('404 Not Found')

class get_chart_baby_datalist(request):
    return HttpResponse('404 Not Found')
    
class get_baby_datalist(request):
    return HttpResponse('404 Not Found')
