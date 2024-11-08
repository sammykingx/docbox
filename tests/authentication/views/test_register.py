from django.test import TestCase
from django.urls import reverse_lazy
from django.test import RequestFactory
from authentication.views import register
from unittest.mock import patch, MagicMock
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from pathlib import Path


START_COLOR = "\033[92m"
END_COLOR = "\033[0m"
CUR_DIR = Path(__file__).parent.name
CUR_FILE = Path(__file__).name

class TestUserRegistrationView(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._model = register.UserRegistrationView.form_class.Meta.model
        print(f"{START_COLOR}Running {CUR_FILE} in {CUR_DIR}{END_COLOR}")
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        print(f"\n{START_COLOR}Finished running all test in {CUR_FILE}{END_COLOR} ✅")
        return super().tearDownClass()

    def setUp(self) -> None:
        self._user = self._model.objects.create_user(
            email="test@example.com",
            password="samplePassword@!123",
        )
        self._request = RequestFactory().get("/demo_url")
        return super().setUp()
    
    def tearDown(self) -> None:
        self._model.objects.all().delete()
        return super().tearDown()
    
    @patch.object(register.UserRegistrationView, "send_welcome_email", return_value=True)
    def testPost(self, mocked_send_welcome_email:MagicMock) -> None:
        url = reverse_lazy("register_user")
        self.client.post(
            url,
            data={
                "first_name": "Test",
                "last_name": "User",
                "email": "gangsta1905@cumfoto.com",
                "password1": "superSecret!23_",
                "password2": "superSecret!23_",
                "phone_number": "+2347034216543",
            },
        )
        user = self._model.objects.get(email="gangsta1905@cumfoto.com")
        self.assertEqual(user.role, "staff")
        mocked_send_welcome_email.assert_called_once()

    @patch.object(register, "render_to_string", return_value="Rendered String")
    @patch.object(register, "deliver_email", return_value=False)
    def testSendWelcomeEmail(self, mocked_deliver_email:MagicMock, mocked_render_to_string: MagicMock) -> None:
        view_class = register.UserRegistrationView()
        view_class.object = self._user
        view_class.request = self._request
        view_class.send_welcome_email("xxxx")
        mocked_render_to_string.assert_called_once_with(
            template_name="emails/verify_email.html",
            context={
                "uid": urlsafe_base64_encode(force_bytes(self._user.pk)),
                "token": "xxxx",
                "protocol": "http",
                "hostname": self._request.get_host(),
            },
        )
        mocked_deliver_email.assert_called_once()
