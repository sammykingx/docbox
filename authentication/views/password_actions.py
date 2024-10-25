from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetCompleteView,
)
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse_lazy
from common.logger import logger


class SendResetLink(PasswordResetView):
    """Sends password reset link to user making the request"""

    template_name = "authentication/password_reset.html"
    email_template_name = html_email_template_name = "emails/pwd_reset_mail.html"
    subject_template_name = "emails/pwd_reset_email_sbj.txt"
    extra_email_context = {}
    success_url = reverse_lazy("reset-pwd-done")


class SendResetLinkDone(PasswordResetCompleteView):
    """Shown after a user has been mailed a link to reset their password."""

    template_name = "authentication/password_reset_done.html"
    


class ChangePassword(PasswordChangeView):
    """
        Updates the authenticated user credentials on the database.
        User has to be logged in before they can update password.
    """

    template_name = "authentication/password_change.html"


class ChangePasswordComplete(PasswordChangeDoneView):
    """Shown when authenticated user credentials is updated successfully"""

    template_name = "authentication/password_change_done.html"
