# -*- coding: utf-8 -*-
from django.views.generic import View
#from my_auth.forms import LoginForm
from django.contrib import auth
from django.http import HttpResponse
import json


# Create your views here.
class UserControl(View):

    def post(self,request,*args,**kwargs):
        #get the operation
        slug = self.kwargs.get('slug')

        if 'register' == slug:
            return self.register(request)
        elif 'login' == slug:
            return self.login(request)

    def register(self,request):
        username = self.request.POST.get("username","")
        email = self.request.POST.get("email","")
        password1 = self.request.POST.get("password1","")
        password2 = self.request.POST.get("password2", "")

        print(username,email)
        print(password1,password2)

    def login(self,request):
        username = self.request.POST.get("username", "")
        password = self.request.POST.get("password", "")

        user = auth.authenticate(username=username,password=password)


        errors = []

        if user is not None:
            auth.login(request,user)
        else:
            errors.append("username or password not correct")

        mydict = {"errors": errors}

        return HttpResponse(json.dumps(mydict),content_type="application/json")