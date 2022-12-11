from django.db import models

from .card import Card
from .user import User


class UpdateCardLog(models.Model):
    """The update log of cards"""
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    card = models.ForeignKey(Card, models.SET_NULL, blank=True, null=True)
    face_id = models.IntegerField(blank=True, null=True)
    old_content = models.CharField(max_length=1000000)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'update_card_log'
