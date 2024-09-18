from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetCompleteView,
)


class SendResetLink(PasswordResetView):
    """Sends password reset link to user making the request"""

    template_name = "auth/password_reset.html"


class SendResetLinkDone(PasswordResetCompleteView):
    """Shown after a user has been mailed a link to reset their password."""

    template_name = "auth/password_reset_done.html"


class ChangePassword(PasswordChangeView):
    """Updates the authenticated user credentials on the database"""

    template_name = "auth/password_change.html"


class ChangePasswordComplete(PasswordChangeDoneView):
    """Shown when authenticated user credentials is updated successfully"""

    template_name = "auth/password_change_done.html"
