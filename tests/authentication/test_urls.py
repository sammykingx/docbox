from django.test import TestCase
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
)
from django.urls import resolve, reverse_lazy
from django.contrib.auth import get_user_model
from authentication.views import register, verify_account
from pathlib import Path


START_COLOR = "\033[92m"
END_COLOR = "\033[0m"
CUR_DIR = Path(__file__).parent.name

class TestUrls(TestCase):
    """
        Test all authentication app urls to see if they're
        routing to the appropriate view class and also
        the write templates is called with it's context.
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            email="test@example.com",
            password="samplePassword@!123",
        )
        print(f"{START_COLOR}Running {Path(__file__).name} in {CUR_DIR}{END_COLOR}")
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        print(f"{START_COLOR}Finished running all test{END_COLOR} ✅")
        return super().tearDownClass()

    def testLogin(self) -> None:
        url = reverse_lazy("user_login")
        resolved_view = resolve(url)
        self.assertEqual(resolved_view.func.view_class, LoginView)
        self.assertTemplateUsed(self.client.get(url), "authentication/login.html")

    def testLogout(self) -> None:
        url = reverse_lazy("user_logout")
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, LogoutView)
        
    def testRegister(self) -> None:
        url = reverse_lazy("register_user")
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, register.UserRegistrationView)
        self.assertTemplateUsed(self.client.get(url), "authentication/user_registration.html")
        
    def testVerifyAccount(self) -> None:
        expected_template = "authentication/verify_account.html"
        url = reverse_lazy(
            "verify_account",
            kwargs=dict(
                    uid="Mjc",
                    token="xxxxx",
                )
            )
        resolved_view = resolve(url).func.view_class
        response = self.client.get(url)
        self.assertEqual(resolved_view, verify_account.VerifyEmailView)
        self.assertTemplateUsed(response, expected_template)
        self.assertIn("verified", response.context)
        self.assertIsInstance(response.context["verified"], bool)
        
    def testPasswordResetLink(self) -> None:
        url = reverse_lazy("reset-password")
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, PasswordResetView)
        self.assertTemplateUsed(self.client.get(url), "authentication/password_reset.html")
        
    def testPasswordResetLinkDone(self) -> None:
        url = reverse_lazy("reset-pwd-done")
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, PasswordResetDoneView)
        self.assertTemplateUsed(self.client.get(url), "authentication/password_reset_done.html")
        
    def testChangePassword(self) -> None:
        url = reverse_lazy(
            "change-pwd",
            kwargs=dict(
                    uidb64="xxxx".encode(),
                    token="xxxxxx",
                )
            )
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, PasswordResetConfirmView)
        self.assertTemplateUsed(self.client.get(url), "authentication/password_change.html")
        
    def testChangePasswordDone(self) -> None:
        url = reverse_lazy("change-pwd-done")
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, PasswordResetCompleteView)
        self.assertTemplateUsed(self.client.get(url), "authentication/password_change_done.html")
        
    def testPasswordUpdate(self) -> None:
        url = reverse_lazy("update-pwd")
        resolved_view = resolve(url).func.view_class
        self.client.login(
            email="test@example.com",
            password="samplePassword@!123",
        )
        response = self.client.get(url)
        self.assertEqual(resolved_view, PasswordChangeView)
        self.assertTemplateUsed(response, "authentication/update_password.html")
