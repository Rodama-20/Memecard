from django.db import models

from .card import Card
from .face_type import FaceType


class Face(models.Model):
    """A face of a card."""
    card = models.ForeignKey(Card, models.CASCADE)
    type = models.ForeignKey(FaceType, models.DO_NOTHING)
    content = models.CharField(max_length=1000000, blank=True, null=True)
    reports = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.content

    class Meta:
        managed = False
        db_table = 'faces'

    