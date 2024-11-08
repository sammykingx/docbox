from django.test import TestCase
from django.contrib.auth import get_user_model
from authentication.views import verify_account
from pathlib import Path

START_COLOR = "\033[92m"
END_COLOR = "\033[0m"
CUR_DIR = Path(__file__).parent.name
CUR_FILE = Path(__file__).name

class TestVerifyEmailView(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._model = get_user_model()
        cls.view = verify_account.VerifyEmailView()
        print(f"{START_COLOR}Running {CUR_FILE} in {CUR_DIR}{END_COLOR}")
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        print(f"\n{START_COLOR}Finished running all test in {CUR_FILE}{END_COLOR} ✅\n")
        return super().tearDownClass()
    
    def setUp(self) -> None:
        self._user = self._model.objects.create_user(
            email="test@example.com",
            password="samplePassword@!123",
        )
        return super().setUp()
    
    def tearDown(self) -> None:
        self._model.objects.all().delete()
        return super().tearDown()
    
    def testGetUserOrNone(self) -> None:
        user_exist = self.view.get_user_or_none(self._user.pk)
        null_user = self.view.get_user_or_none(50000)
        self.assertIsNotNone(user_exist)
        self.assertIsNone(null_user)
        
    def testActivateAccount(self) -> None:
        self.view.activate_account(self._user)
        self._user.refresh_from_db()
        self.assertTrue(self._user.is_verified)
