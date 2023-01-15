"""CardType model.

(c) 2023 He-Arc Cyrille Polier
"""

from django.db import models


class CardType(models.Model):
    """A type of card, defining the fields it has."""

    name = models.CharField(unique=True, max_length=30)
    description = models.CharField(max_length=1000000)

    def __str__(self) -> str:
        return "" + self.name

    class Meta:
        """Meta class for CardType."""

        managed = False
        db_table = "card_types"
