from django.db import models

from .deck import Deck
from .tag import Tag

class DeckTag(models.Model):
    """Helper table for many-to-many relationship between decks and tags."""
    deck = models.ForeignKey(Deck, models.CASCADE)
    tag = models.ForeignKey(Tag, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'deck_tag'
        unique_together = (('tag', 'deck'),)
