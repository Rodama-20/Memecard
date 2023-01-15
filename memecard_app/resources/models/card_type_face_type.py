"""CardTypeFaceType model.

(c) 2023 He-Arc Cyrille Polier
"""
from django.db import models
from django.db.models.query import RawQuerySet

from .card_type import CardType
from .face_type import FaceType


class CardTypeFaceType(models.Model):
    """Helper table for many-to-many relationship between card types and face types."""

    card_type = models.ForeignKey(CardType, models.DO_NOTHING)
    face_type = models.ForeignKey(FaceType, models.DO_NOTHING)
    name = models.CharField(max_length=30)
    required = models.BooleanField()

    class Meta:
        """Meta class for CardTypeFaceType."""

        managed = False
        db_table = "card_type_face_type"
        unique_together = (("card_type", "face_type", "name"),)

    def get_face_form_deck(self, deck_id: int) -> RawQuerySet:
        """Get all face types for a deck.

        Args:
            deck_id (int): The id of the wanted deck.

        Returns:
            RawQuarySet: An iterable of CardTypeFaceType objects.
        """
        return CardTypeFaceType.objects.raw(
            """SELECT *
            FROM card_type_face_type
            JOIN card_types ON card_type_face_type.card_type_id = card_types.id
            JOIN decks ON card_types.id = decks.card_type_id
            WHERE decks.id = %s""",
            [deck_id],
        )
