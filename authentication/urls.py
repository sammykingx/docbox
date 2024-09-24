# auth app related views

from django.urls import path
from .views import login, password_actions


urlpatterns = [
    path(
        "login/",
        login.UserLoginView.as_view(),
        name="user-login",
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
    path(
        "change-password/", password_actions.ChangePassword.as_view()
    ),
    path(
        "change-password/complete/",
        password_actions.ChangePasswordComplete.as_view(),
    ),
]
