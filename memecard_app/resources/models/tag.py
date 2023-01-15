"""Tag model.

(c) 2023 He-Arc Cyrille Polier
"""

from django.db import models

from .deck import Deck


class Tag(models.Model):
    """A tag for a deck."""

    name = models.CharField(unique=True, max_length=30)

    # Many-to-many fields
    decks = models.ManyToManyField(Deck, through="DeckTag", related_name="tags")

    def __str__(self):
        return "" + self.name

    class Meta:
        managed = False
        db_table = "tags"
