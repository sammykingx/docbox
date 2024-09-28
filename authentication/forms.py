from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from typing import Any


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self) -> str:
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("It seems you already have an account")
        
        return email
        
        
    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        phone_number = cleaned_data.get("phone_number")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if CustomUser.objects.filter(phone_number=phone_number).exists():
            self.add_error('phone_number', "Phone Number already registered")

        if password1 != password2:
            self.add_error("password2", "password mis-match")
            
        return cleaned_data
    

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
