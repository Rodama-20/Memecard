""" User model.

(c) 2023 He-Arc Cyrille Polier
"""

import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    """A user of the site."""

    email = models.CharField(unique=True, max_length=50)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=256)
    last_login = models.DateTimeField(default=datetime.datetime.now)

    # Django related fields
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "password"]

    is_staff = False

    def __str__(self):
        return "" + self.username

    class Meta:
        managed = False
        db_table = "users"

    # TODO: Implement this method with hashing
    def check_password(self, raw_password: str) -> bool:
        return self.password == raw_password

    def has_module_perms(self, app_label):
        return False
