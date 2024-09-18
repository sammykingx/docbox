from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView


# Create your views here.
class UserLoginView(LoginView):
    template_name = "auth/login.html"
