from django.db import models

from .card import Card

class Meme(models.Model):
    """A meme wich will be linked to a card to help the user at remembering the card."""
    card = models.ForeignKey(Card, models.CASCADE, related_name='memes')
    url = models.CharField(max_length=256)
    reports = models.IntegerField()

    def __str__(self):
        return self.url

    class Meta:
        managed = False
        db_table = 'memes'
