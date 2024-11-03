from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
)
from .views import register, verify_account


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
    path(
        "verify_account/<str:uid>/<str:token>/",
        verify_account.VerifyEmailView.as_view(),
        name="verify_account",
    ),
    path(
        "reset-password/",
        PasswordResetView.as_view(
            template_name = "authentication/password_reset.html",
            email_template_name = "emails/pwd_reset_mail.html",
            html_email_template_name = "emails/pwd_reset_mail.html",
            subject_template_name = "emails/pwd_reset_email_sbj.txt",
            success_url = reverse_lazy("reset-pwd-done"),
        ),
        name="reset-password",
    ),
    path(
        "reset-password/done/",
        PasswordResetDoneView.as_view(
            template_name = "authentication/password_reset_done.html"
        ),
        name="reset-pwd-done",
    ),
    path(
        "change-password/<str:uidb64>/<str:token>/",
        PasswordResetConfirmView.as_view(
            template_name = "authentication/password_change.html",
            success_url = reverse_lazy("change-pwd-done"),
        ),
        name="change-pwd"),
    path(
        "change-password/complete/",
        PasswordResetCompleteView.as_view(
            template_name="authentication/password_change_done.html",
        ),
        name="change-pwd-done"
    ),
    path(
        "update-password/",
        PasswordChangeView.as_view(
            template_name = "authentication/update_password.html",
            success_url = reverse_lazy("user_dashboard"),
        ),
        name="update-pwd"
    ),
]
