# auth app related views

from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, password_actions, verify_account


urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="authentication/login.html",
            next_page=reverse_lazy("user_dashboard"),
        ),
        name="user_login",
    ),
    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("user_login")),
        name="user_logout",
    ),
    path(
        "register/",
        register.UserRegistrationView.as_view(),
        name="register_user",
    ),
    # path(
    #     "verify_account/<str:uid>/<str:token>/",
    #     TemplateView.as_view(
    #         template_name="authentication/verify_account.html",
    #     ),
    #     name="verify_account",
    # ),
    path(
        "verify_account/<str:uid>/<str:token>/",
        verify_account.VerifyEmailView.as_view(),
        name="verify_account",
    ),
    path(
        "reset-password/",
        password_actions.SendResetLink.as_view(),
        name="reset-password",
    ),
    path(
        "reset-password/done/",
        password_actions.SendResetLinkDone.as_view(),
    ),
    path("change-password/", password_actions.ChangePassword.as_view()),
    path(
        "change-password/complete/",
        password_actions.ChangePasswordComplete.as_view(),
    ),
]
