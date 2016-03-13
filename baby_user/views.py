# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from baby_user.models import user, user_normal, user_daycarecenter, user_bonne
from django.views.decorators.csrf import csrf_exempt
import json

def login():
    return HttpResponse("login")

@csrf_exempt
def register(request):
    if request.method == 'POST':
	data = {}
        # [account, password, Identify_parents, Identify_bonne, Identify_daycarecenter, email]
        data = json.loads(request.body)
	
	response_data = {}
        try:
            reg_user = user.objects.create(account=data['account'], password=data['password'], \
                auth_parents=data['Identify_parents'], auth_bonne=data['Identify_bonne'], \
                auth_daycarecenter=data['Identify_daycarecenter'])

            user_info = user_normal.objects.create(email=data['email'], user_id=reg_user)

            response_data['result'] = 1
            response_data['message'] = 'success'
        except Exception, ex:
            response_data['result'] = 0
            response_data['message'] = 'Error:' + ex.message
	return HttpResponse(response_data['message'])
    return HttpResponse('Not things')

