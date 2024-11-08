from django.test import TestCase
from authentication.forms import RegistrationForm


class TestForms(TestCase):
    _model = RegistrationForm.Meta.model

    def setUp(self) -> None:
        self._existing_user = self._model.objects.create_user(
            email="testuser@example.com",
            password="suPer$ecre123",
            phone_number="+1234567890",
        )
        self._form_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@example.com",
            "phone_number": "+2341234567890",
            "password1": "super$ecr123",
            "password2": "super$ecr123",
        }
        return super().setUp()
    
    def tearDown(self) -> None:
        self._model.objects.all().delete()
        return super().tearDown()
    
    def testUniqueEmail(self):
        valid_form = RegistrationForm(data=self._form_data)
        self.assertTrue(valid_form.is_valid())

        self._form_data["email"] = "testuser@example.com"
        invalid_form = RegistrationForm(data=self._form_data)
        self.assertFalse(invalid_form.is_valid())
        self.assertIn("email",  invalid_form.errors)
        
    def testUniquePhoneNumber(self) -> None:
        self._form_data["phone_number"] = self._existing_user.phone_number
        invalid_form = RegistrationForm(data=self._form_data)
        self.assertFalse(invalid_form.is_valid())
        self.assertIn("phone_number",  invalid_form.errors)
        
    def testPasswordMismatch(self) -> None:
        self._form_data["password1"] = "super$ecr1231"
        invalid_form = RegistrationForm(data=self._form_data)
        self.assertFalse(invalid_form.is_valid())
        self.assertIn("password2",  invalid_form.errors)
