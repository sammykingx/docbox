from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    template_name = "authentication/login.html"
