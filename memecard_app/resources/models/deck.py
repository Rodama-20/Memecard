"""Deck model.

(c) 2023 He-Arc Cyrille Polier
"""

from django.db import models

from card_type import CardType
from user import User


class Deck(models.Model):
    """A collection of cards."""

    name = models.CharField(max_length=30)
    public = models.BooleanField()
    strict_one_way = models.BooleanField()
    card_type = models.ForeignKey(CardType, models.CASCADE)

    # Many-to-many fields
    users = models.ManyToManyField(User, through="DeckUser", related_name="decks")

    def __str__(self) -> str:
        return "" + self.name

    class Meta:
        managed = False
        db_table = "decks"
