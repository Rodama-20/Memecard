from django.db import models

from .card import Card
from .deck import Deck
from .tag import Tag
from .user import User

class UpdateDeckLog(models.Model):
    """The update log of decks"""
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    deck = models.ForeignKey(Deck, models.SET_NULL, blank=True, null=True)
    card = models.ForeignKey(Card, models.SET_NULL, blank=True, null=True)
    tag = models.ForeignKey(Tag, models.SET_NULL, blank=True, null=True)
    action = models.CharField(max_length=30)
    old_name = models.CharField(max_length=30)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'update_deck_log'
