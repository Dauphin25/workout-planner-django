from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField (_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    phone_number = models.CharField(_("Phone Number"), max_length=20, blank=True, null=True)
    city = models.CharField(_("City"), max_length=255)
    date_of_birth = models.DateField(_("Date of Birth"), blank=True, null=True)
    registration_date = models.DateTimeField(_("Registration Date"), auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
