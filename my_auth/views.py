# -*- coding: utf-8 -*-
from django.views.generic import View
from my_auth.forms import RegForm
from django.contrib import auth
from django.http import HttpResponse
import json
from django.core.exceptions import PermissionDenied


# Create your views here.
class UserControl(View):

    def post(self,request,*args,**kwargs):
        #get the operation
        slug = self.kwargs.get('slug')
        print(slug)
        if 'register' == slug:
            return self.register(request)
        elif 'login' == slug:
            return self.login(request)
        elif 'logout' == slug:
            return self.logout(request)
        elif 'passwd_change' == slug:
            return self.change_password(request)

    def register(self,request):
        username = self.request.POST.get("username","")
        email = self.request.POST.get("email","")
        password1 = self.request.POST.get("password1","")
        password2 = self.request.POST.get("password2", "")
        print(username)
        print(username,email)
        print(password1,password2)

        user_form = RegForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            user = auth.authenticate(username=username,password=password2)
            auth.login(request,user)
            return HttpResponse(json.dumps({"ok":"successfully"}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"error":"Failed"}),content_type="application/json")

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

    def logout(self,request):
        if not request.user.is_authenticated():
            raise PermissionDenied
        else:
            auth.logout(request)
            return HttpResponse("OK")

    def change_password(self, request):
        if not request.user.is_authenticated():
            raise PermissionDenied
        old_passwd = self.request.POST.get("old_passwd", "")
        new_passwd = self.request.POST.get("new_passwd", "")

        print(old_passwd)
        print(new_passwd)
        errors=['OK']
        mydict = {"errors": errors}

        return HttpResponse(json.dumps(mydict), content_type="application/json")