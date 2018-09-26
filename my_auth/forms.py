# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class RegForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {"username","email"}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('password do not match')

        return cd['password2']
