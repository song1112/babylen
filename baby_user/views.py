# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from baby_user.models import user, user_normal, user_daycarecenter, user_bonne
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def login(request):
	response_data = {}
	data = {}
    if request.method == 'POST':
		# [account, password, Identify]
		data = json.loads(request.body)
		try:
			query_u = uder.objects.get(account=data['account'])
		except Exception, ex:
			response_data['action'] = -1
			response_data['message'] = 'Error:' + ex.message
			return JsonResponse(response_data)
	return HttpResponse('404 Not Found')


@csrf_exempt
def register(request):
	response_data = {}
	data = {}
	if request.method == 'POST':
        # [account, password, Identify_parents, Identify_bonne, Identify_daycarecenter, email]
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
	    return HttpResponse(response_data['message'])
	return HttpResponse('404 Not Found')


