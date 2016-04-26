# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import datetime
import pytz

from baby_user.views import resize_uploaded_image
from baby.models import *

from PIL import ImageFile
from django.core.files import File
from django.core.files.base import ContentFile

"""[HTTP POST][Insert][Update] 寶寶資料 
POST VALUE:{"uid","Identify","name","birthday","sex","tips","img","height","weight","nickname","bid"}
RETURN:{"action"}
"""
@csrf_exempt
def cu_baby(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    response_data['message'] = 'cu_baby'
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if data.get('birthday')!="" and data.get('birthday'):
                date_object = datetime.datetime.strptime(data['birthday'], '%Y/%m/%d')
            if data.get('bid'):
                response_data['bid'] = data.get('bid')
                b = baby.objects.get(id=data['bid'])
                b.name = data['name']
                b.sex = data['sex']
                b.tips = data['tips']
                b.height = data['height']
                b.weight = data['weight']
                b.nickname = data['nickname']
                if data.get('birthday')!="" and data.get('birthday'):
                    b.birthday=date_object
                b.save()
                response_data['action'] = 1
            else:
                b = baby.objects.create( sex=data['sex'], name=data['name'], \
                                    tips=data['tips'], height=data['height'], weight=data['weight'], \
                                    nickname=data['nickname'], user_id=data['uid'])
                if data.get('birthday')!="" and data.get('birthday'):
                    b.birthday=date_object
                b.save()
                response_data['bid'] = b.id
                response_data['action'] = 1
            return JsonResponse(response_data)
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'cu_baby error:' + ex.message
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
            response_data['message'] = 'u_baby_relevance_remove error:' + ex.message
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
                response_data['selecttime'] = data.get('indextime')
                response_data['action'] = 1
                # local = pytz.timezone ('Asia/Taipei')
#                naive = datetime.datetime.strptime(data['indextime'], '%Y/%m/%d')
#                local_dt = local.localize(naive, is_dst=None)
#                utc_dt = local_dt.astimezone (pytz.utc)
#                dt_str = utc_dt.strftime ("%Y/%m/%d")
#                query_date = dt_str.split('/')
                query_date = data['indextime'].split('/')
                # 取得餵奶
                BreastFeeding = {}
                bf = baby_breastfeeding.objects.filter(createdat__year=query_date[0], createdat__month=query_date[1], \
                                                       createdat__day=query_date[2], baby_id=data['bid']).order_by('-id')
                BreastFeeding['todaycount'] = bf.count()
                if bf.count() > 0:
                    t = bf[0].updatedat.astimezone(pytz.timezone('Asia/Taipei'))
                    BreastFeeding['finaltime'] = str(t.hour) + ":" + str(t.minute)
                else:
                    BreastFeeding['finaltime'] = ""
                response_data['BreastFeeding'] = BreastFeeding
                # 取得副食品
                Grocery = {}
                g = baby_grocery.objects.filter(createdat__year=query_date[0], createdat__month=query_date[1], \
                                                createdat__day=query_date[2], baby_id=data['bid']).order_by('-id')
                Grocery['todaycount'] = g.count()
                if g.count() > 0:
                    t = g[0].updatedat.astimezone(pytz.timezone('Asia/Taipei'))
                    Grocery['finaltime'] = str(t.hour) + ":" + str(t.minute)
                else:
                    Grocery['finaltime'] = ""
                response_data['Grocery'] = Grocery
                # 取得點心
                DessertFruit = {}
                df = baby_dessertfruit.objects.filter(createdat__year=query_date[0], createdat__month=query_date[1], \
                                                createdat__day=query_date[2], baby_id=data['bid']).order_by('-id')
                DessertFruit['todaycount'] = df.count()
                if df.count() > 0:
                    t = df[0].updatedat.astimezone(pytz.timezone('Asia/Taipei'))
                    DessertFruit['finaltime'] = str(t.hour) + ":" + str(t.minute)
                else:
                    DessertFruit['finaltime'] = ""
                response_data['DessertFruit'] = DessertFruit
                # 取得排便
                Defecation = {}
                de = baby_defecation.objects.filter(createdat__year=query_date[0], createdat__month=query_date[1], \
                                                createdat__day=query_date[2], baby_id=data['bid']).order_by('-id')
                Defecation['todaycount'] = de.count()
                if de.count() > 0:
                    t = de[0].updatedat.astimezone(pytz.timezone('Asia/Taipei'))
                    Defecation['finaltime'] = str(t.hour) + ":" + str(t.minute)
                else:
                    Defecation['finaltime'] = ""
                response_data['Defecation'] = Defecation
                # 取得尿布
                Diaper = {}
                d = baby_diaper.objects.filter(createdat__year=query_date[0], createdat__month=query_date[1], \
                                                createdat__day=query_date[2], baby_id=data['bid']).order_by('-id')
                Diaper['todaycount'] = d.count()
                if d.count() > 0:
                    t = d[0].updatedat.astimezone(pytz.timezone('Asia/Taipei'))
                    Diaper['finaltime'] = str(t.hour) + ":" + str(t.minute)
                else:
                    Diaper['finaltime'] = ""
                response_data['Diaper'] = Diaper
            else:
                today = datetime.date.today()
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'get_baby_record_simple error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Select] 餵奶，副食品，點心、水果，排便，尿布的頁面資料(詳)
POST VALUE:{"uid","Identify","bid","recordtype","indextime"}
RETURN VALUE:{"action":1,"selecttime":"2015/12/12","datalist":[{"rid","text","time":"12:33"},{"rid","text","time":"17:33"}]}
"""
@csrf_exempt
def get_baby_record_detail(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        response_data['action'] = 0
        try:
            if data.get('indextime'):
                query_date = data['indextime'].split('/')
                response_data['selecttime'] = data['indextime']
                datalist = []
                response_data['action'] = 1
                data['recordtype']=int(data['recordtype'])
                #  [0:餵奶,1:副食品,2:點心、水果,3:排便,4:尿布]
                if data['recordtype'] == 0:
                    baby_records = \
                        baby_breastfeeding.objects.filter(createdat__year=query_date[0], \
                                                          createdat__month=query_date[1], \
                                                          createdat__day=query_date[2], baby_id=data['bid'])
                    for record in baby_records:
                        tmpdict = {}
                        tmpdict['rid'] = record.id
                        tmpdict['text'] = record.content
                        t = record.updatedat.astimezone(pytz.timezone('Asia/Taipei'))
                        tmpdict['time'] = str(t.hour) + ":" + str(t.minute)
                        datalist.append(tmpdict)
                if data['recordtype'] == 1:
                    baby_records = \
                        baby_grocery.objects.filter(createdat__year=query_date[0], \
                                                    createdat__month=query_date[1], \
                                                    createdat__day=query_date[2], baby_id=data['bid'])
                    for record in baby_records:
                        tmpdict = {}
                        tmpdict['rid'] = record.id
                        tmpdict['text'] = record.content
                        t = record.updatedat.astimezone(pytz.timezone('Asia/Taipei'))
                        tmpdict['time'] = str(t.hour) + ":" + str(t.minute)
                        datalist.append(tmpdict)
                if data['recordtype'] == 2:
                    baby_records = \
                        baby_dessertfruit.objects.filter(createdat__year=query_date[0], \
                                                         createdat__month=query_date[1], \
                                                         createdat__day=query_date[2], baby_id=data['bid'])
                    for record in baby_records:
                        tmpdict = {}
                        tmpdict['rid'] = record.id
                        tmpdict['text'] = record.content
                        t = record.updatedat.astimezone(pytz.timezone('Asia/Taipei'))
                        tmpdict['time'] = str(t.hour) + ":" + str(t.minute)
                        datalist.append(tmpdict)
                if data['recordtype'] == 3:
                    baby_records = \
                        baby_defecation.objects.filter(createdat__year=query_date[0], \
                                                       createdat__month=query_date[1], \
                                                       createdat__day=query_date[2], baby_id=data['bid'])
                    for record in baby_records:
                        tmpdict = {}
                        tmpdict['rid'] = record.id
                        tmpdict['text'] = record.content
                        t = record.updatedat.astimezone(pytz.timezone('Asia/Taipei'))
                        tmpdict['time'] = str(t.hour) + ":" + str(t.minute)
                        datalist.append(tmpdict)
                if data['recordtype'] == 4:
                    baby_records = \
                        baby_diaper.objects.filter(createdat__year=query_date[0], \
                                                   createdat__month=query_date[1], \
                                                   createdat__day=query_date[2], baby_id=data['bid'])
                    for record in baby_records:
                        tmpdict = {}
                        tmpdict['rid'] = record.id
                        tmpdict['text'] = record.content
                        t = record.updatedat.astimezone(pytz.timezone('Asia/Taipei'))
                        tmpdict['time'] = str(t.hour) + ":" + str(t.minute)
                        datalist.append(tmpdict)
            response_data['datalist'] = datalist
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'get_baby_record_detail error:' + ex.message
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
    response_data['message'] = 'cu_baby_record'
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            response_data['action'] = 1
            data['recordtype']=int(data['recordtype'])
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
            response_data['message'] = 'cu_baby_record error:' + ex.message
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
                    pics_list.append(pic.img.url)
                response_data['imglist'] = pics_list
                response_data['selecttime'] = "all"
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'get_baby_picture_imglist error:' + ex.message
    return JsonResponse(response_data)

"""[HTTP POST][Insert] 相機畫面的 +photo 按鈕選擇的圖片
POST VALUE:{"uid","Identify","bid","img"}
"""
@csrf_exempt
def c_baby_picture(request):
    response_data = {}
    data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        try:
            bid = request.POST['bpid']
            resizedImage = resize_uploaded_image(request.FILES['uploaded_file'])
            content = File(resizedImage)
            #file_content = ContentFile(request.FILES['uploaded_file'].read())
            baby_pic = baby_picture.objects.create(baby_id=bid)
            baby_pic.img.save(bid+request.FILES['uploaded_file'].name, content)
            response_data['action'] = 1
            response_data['message'] = 'c_baby_picture success'
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = 'c_baby_picture error:' + ex.message
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
            response_data['message'] = 'u_baby_relevance_b2m error:' + ex.message
    return JsonResponse(response_data)

"""上傳寶寶頭像
POST VALUE: file, bid
"""
@csrf_exempt
def updata_baby_pic(request):
    response_data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        try:
            bid = request.POST['bid']
            # file_content = ContentFile(request.FILES['uploaded_file'].read())
            resizedImage = resize_uploaded_image(request.FILES['uploaded_file'])
            content = File(resizedImage)
            b_data = baby.objects.get(id=bid)
            b_data.img.save(bid+request.FILES['uploaded_file'].name, content)
            response_data['action'] = 1
            response_data['message'] = 'updata_baby_pic success'
        except Exception, ex:
            response_data['action'] = -1
            response_data['message'] = ex.message
    return JsonResponse(response_data)

"""取得寶寶資料
POST VALUE: bid
"""
@csrf_exempt
def get_baby_data(request):
    response_data = {}
    response_data['action'] = 0
    if request.method == 'POST':
        try:
            response_data['action'] = 1
            data = json.loads(request.body)
            b_data = baby.objects.get(id=data['bid'])
            response_data['name'] = b_data.name
            response_data['nickname'] = b_data.nickname
            response_data['height'] = b_data.height
            response_data['weight'] = b_data.weight
            response_data['birthday'] = ''
            if b_data.birthday:
                response_data['birthday'] = str(b_data.birthday.year)+'/'+str(b_data.birthday.month)+'/'+str(b_data.birthday.day)
            response_data['tips'] = b_data.tips
            response_data['sex'] = '未知'
            if(b_data.sex=='0'):
                response_data['sex'] = '女'
            if(b_data.sex=='1'):
                response_data['sex'] = '男'
                
        except Exception, ex:
            #response_data['action'] = -1
            response_data['message'] = ex.message
    return JsonResponse(response_data)
