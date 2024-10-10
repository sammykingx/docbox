from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = "authentication/login.html"
    next_page = reverse_lazy("user_dashboard")
