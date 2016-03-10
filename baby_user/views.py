# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from baby_user import user, user_normal, user_daycarecenter, user_bonne

def login():
    return HttpResponse("login")

def register():
    if request.method == 'POST':
        resp_data = {}

        # [account, password, Identify_parents, Identify_bonne, Identify_daycarecenter, email]
        data = json.loads(request.body.decode("utf-8"))
        try:
            # 建立使用者
            reg_user = user.objects.create(account=data['account'], password=data['password'], \
                auth_parents=data['Identify_parents'], auth_bonne=data['Identify_bonne'], \
                auth_daycarecenter=data['Identify_daycarecenter'])

            user_info = user_normal.objects.create(email=data['email'], user_id=reg_user)

            response_data['result'] = 1
            response_data['message'] = 'success'
        except Exception, ex:
            response_data['result'] = 0
            response_data['message'] = 'Error:' + ex.message

    return HttpResponse("register")


