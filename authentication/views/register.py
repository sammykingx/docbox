from django.http import HttpResponse
from django.urls import reverse_lazy
from django.forms import BaseModelForm
from django.views.generic import CreateView
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from ..forms import RegistrationForm
from common.utils import deliver_email


class UserRegistrationView(CreateView):
    template_name = "authentication/user_registration.html"
    form_class = RegistrationForm
    context_object_name = "user_registration"
    success_url = reverse_lazy("user_login")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """Automaticaally called when form validation is completed both on form level and model level"""

        user = form.save(commit=False)
        user.role = "staff"
        email_token = default_token_generator.make_token(user)
        response = super().form_valid(form)

        if not self.send_welcome_email(email_token):
            print("mail wasn't sent")

        # login user, welcome on board
        # send user welcome email on the backeground

        return response
    

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        """Automatically called by django when form.is_valid() returns False"""

        response = super().form_invalid(form)

        return response
    

    def send_welcome_email(self, token: str) -> None:
        """
        send account activation toke to request user email address
        """

        msg = render_to_string(
            template_name="emails/verify_email.html",
            context={
                "uid": urlsafe_base64_encode(force_bytes(self.object.pk)),
                "token": token,
                "protocol": (
                    "https" if self.request.is_secure() else "http"
                ),
                "hostname": self.request.get_host(),
            },
        )

        return deliver_email(
            mail_heading="Verify Your Account - docbox",
            mail_msg=msg,
            recipient=[self.object],
        )
