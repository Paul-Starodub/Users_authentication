from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=70)
    first_name = models.CharField(_("first name"), max_length=70, blank=True)
    last_name = models.CharField(_("last name"), max_length=70, blank=True)
    address_one = models.CharField(_("address"), max_length=128, blank=True)
    address_two = models.CharField(_("address"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=128, blank=True)
    country = models.CharField(_("country"), max_length=128, blank=True)
    province = models.CharField(_("province"), max_length=128, blank=True)
    postal_code = models.CharField(_("postal_code"), max_length=20, blank=True)
    phone = models.CharField(_("phone"), max_length=15, blank=True, null=True)
    marketing_consent_one = models.BooleanField(_("first marketing_consent"), default=False)
    marketing_consent_two = models.BooleanField(_("second marketing_consent"), default=False)
    username = models.CharField(_("username"), max_length=255, unique=True, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    required_fields = ["first_name", "last_name"]

    def __str__(self) -> str:
        return self.email
