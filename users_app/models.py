from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom user class.
    """
    username = None
    email = models.EmailField(
        max_length=250,
        unique=True,
        verbose_name=_('Email')
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
