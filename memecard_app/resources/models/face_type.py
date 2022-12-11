from django.db import models

from .card_type import CardType


class FaceType(models.Model):
    """A type of face, defining its field."""
    name = models.CharField(unique=True, max_length=30)
    description = models.CharField(max_length=1000000)
    question = models.BooleanField()
    response = models.BooleanField()

    # Many-to-many fields
    card_types = models.ManyToManyField(CardType, through='CardTypeFaceType', related_name='face_types')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'face_types'