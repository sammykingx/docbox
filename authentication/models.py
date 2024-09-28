from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    ROLE_OPTIONS = [
        ("admin", "Admin"),
        ("staff", "Staff"),
        ("user", "Standard User"),
        ("guest", "Guests")
    ]
    
    number_validator = RegexValidator(
        regex=r'^\+?1?\d{10,16}$',
        message="Phone numbers must be between 10 and 16 digits, with or without country code.",
    )
    
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(validators=[number_validator], max_length=15,)
    alt_number = models.CharField(
        validators=[number_validator],
        max_length=15,
        blank=True,
    )
    
    role = models.CharField(max_length=20, choices=ROLE_OPTIONS)
    is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "password",
        "phone_number",
        "role",
    ]
    
    class Meta:
        db_table = "app_users"
        verbose_name = "User Accounts"
        indexes = [
            models.Index(
                fields=["email"],
                name="email_idx",
            ),
        ]
        
        constraints = models.UniqueConstraint(
            fields=["phone_number"],
            name="unique_phone_number"),
