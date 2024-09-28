from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from ..forms import RegistrationForm


class UserRegistrationView(CreateView):
    template_name = "authentication/user_registration.html"
    form_class = RegistrationForm
    context_object_name = "user_registration"
    success_url = reverse_lazy("user_login")
     
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        # send user welcome email
        
        return response


    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        """Automatically called by django when form.is_valid() returns False"""
        
        response = super().form_invalid(form)
        
        return response