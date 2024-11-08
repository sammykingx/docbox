from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import force_str
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from typing import Union


class VerifyEmailView(View):
    http_method_names = ["get"]
    
    def get(self, request, **kwargs) -> HttpResponse:
        uid = force_str(urlsafe_base64_decode(kwargs.get("uid")))
        token = kwargs.get("token")

        user = self.get_user_or_none(uid)
        if default_token_generator.check_token(user, token):
            self.activate_account(user)
            # redirect user to dashboard if authenticated
            # else log in and redirect
            context = dict(verified=True)
            
        else:
            context = dict(verified=False)
        
        return render(
            request,
            "authentication/verify_account.html",
            context
        )
        
    def get_user_or_none(self, uid:str) -> Union[AbstractUser, None]:
        _User = get_user_model()

        try:
            _user = _User.objects.get(pk=uid)
            
        except _User.DoesNotExist:
            return None

        return _user
    
    def activate_account(self, user:AbstractUser) -> None:
        """
            updates user is_verified status to true directly
            on the database.
            
            Note: This doesn't updates the previous call to
            user model, so previous call will still have it's
            is_verified property false if the user wasn't verified.
        """

        if not user.is_verified:
            user.__class__.objects.filter(pk=user.pk).update(is_verified=True)
            
        return None