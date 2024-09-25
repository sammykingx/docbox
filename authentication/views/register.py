from django.views.generic import CreateView
from ..forms import RegistrationForm


class UserRegistrationView(CreateView):
    template_name = "authentication/user_registration.html"
    form_class = RegistrationForm
    context_object_name = "user_model"