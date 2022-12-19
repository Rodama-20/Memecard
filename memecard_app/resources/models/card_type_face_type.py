from django.db import models

from .card_type import CardType
from .face_type import FaceType

class CardTypeFaceType(models.Model):
    """Helper table for many-to-many relationship between card types and face types."""
    card_type = models.ForeignKey(
        CardType, models.DO_NOTHING)
    face_type = models.ForeignKey(FaceType, models.DO_NOTHING)
    name = models.CharField(max_length=30)
    required = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'card_type_face_type'
        unique_together = (('card_type', 'face_type', 'name'),)

    def getFaceFormDeck(deck_id: int):
        return CardTypeFaceType.objects.raw('''SELECT *
            FROM card_type_face_type
            JOIN card_types ON card_type_face_type.card_type_id = card_types.id
            JOIN decks ON card_types.id = decks.card_type_id
            WHERE decks.id = %s''', [deck_id])
    