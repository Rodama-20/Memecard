""" User model.

(c) 2023 He-Arc Cyrille Polier
"""

import datetime
from hashlib import scrypt
from os import getenv

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

    def check_password(self, raw_password: str) -> bool:
        return self.password == User.crypt_password(raw_password)

    def has_module_perms(self, app_label):
        return False
    
    @staticmethod
    def crypt_password(raw_password: str) -> str:
        return scrypt(str.encode(raw_password), salt=str.encode(getenv("SALT")), n=2**14, r=8, p=1).hex()
