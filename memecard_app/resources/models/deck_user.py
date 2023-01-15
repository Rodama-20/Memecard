"""DeckUser model.

(c) 2023 He-Arc Cyrille Polier
"""

from django.db import models

from deck import Deck
from user import User


class DeckUser(models.Model):
    """Helper table for many-to-many relationship between decks and users."""

    user = models.ForeignKey(User, models.CASCADE)
    deck = models.ForeignKey(Deck, models.CASCADE)

    class Meta:
        managed = False
        db_table = "deck_user"
        unique_together = (("user", "deck"),)
