from django.db import models

from .card import Card
from .meme import Meme
from .user import User


class CardUser(models.Model):
    """Helper table for many-to-many relationship between cards and users."""
    user = models.ForeignKey(User, models.CASCADE)
    card = models.ForeignKey(Card, models.CASCADE)
    is_learned = models.BooleanField()
    is_known = models.BooleanField()
    meme = models.ForeignKey(Meme, models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_user'
        unique_together = (('user', 'card'),)
