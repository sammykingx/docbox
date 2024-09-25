from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from typing import Any


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    
    def clean(self) -> dict[str, Any]:
        return super().clean()


    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
        )
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
        }
