# encoding: utf-8
from django import forms
from django.contrib.auth.models import User
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']


class LoginForm(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(label=u"电子邮箱")
    username = forms.CharField(label=u"姓名", max_length=50)
    password = forms.CharField(label=u"密码", max_length=30, widget=forms.PasswordInput)
    password1 = forms.CharField(label=u"确认密码", max_length=30, widget=forms.PasswordInput)

    # def clean(self):
    #     cleaned_data = super(RegisterForm, self).clean()
    #     password = RegisterForm.get("password")
    #     password1 = cleaned_data.get("password1")
    #     if password != password1:
    #         raise forms.ValidationError(u"两次密码必须一致")
