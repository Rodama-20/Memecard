from django.db import models

from .card import Card
from .user import User


class RevLog(models.Model):
    """The review log of users"""
    user = models.ForeignKey(User, models.CASCADE)
    card = models.ForeignKey(Card, models.CASCADE)
    answer = models.IntegerField()
    interval = models.IntegerField()
    easiness_factor = models.IntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rev_log'