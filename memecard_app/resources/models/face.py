"""Face model.

(c) 2023 He-Arc Cyrille Polier
"""

from django.db import models

from .card import Card
from .card_type_face_type import CardTypeFaceType


class Face(models.Model):
    """A face of a card."""

    card = models.ForeignKey(Card, models.CASCADE)
    card_type_face_type = models.ForeignKey(CardTypeFaceType, models.DO_NOTHING)
    content = models.CharField(max_length=1000000, blank=True, null=True)
    reports = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return "" + self.content

    class Meta:
        managed = False
        db_table = "faces"
