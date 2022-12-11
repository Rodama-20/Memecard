from django.db import models

import datetime



class User(models.Model):
    """A user of the site."""
    email = models.CharField(unique=True, max_length=50)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=256)
    last_login = models.DateTimeField(default=datetime.datetime.now)

    #not database fields
    is_active = True
    is_staff = False

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'users'

    def check_password(self, password):
        """Check if the password is correct."""
        return self.password == password
