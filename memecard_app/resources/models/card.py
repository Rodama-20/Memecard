"""Card model.

(c) 2023 He-Arc Cyrille Polier
"""

from django.db import models

from .user import User
from .deck import Deck


class Card(models.Model):
    """A card in a deck."""

    creator = models.ForeignKey(
        User, models.SET_NULL, db_column="creator", blank=True, null=True
    )
    deck = models.ForeignKey(Deck, models.CASCADE)
    order = models.IntegerField(blank=True, null=True)
    public = models.BooleanField()
    nb_faces = models.IntegerField()

    # Many-to-many fields
    users = models.ManyToManyField(User, through="CardUser", related_name="cards")

    class Meta:
        managed = False
        db_table = "cards"

    def get_with_user_and_deck(self, params: dict):
        """Get a card with its user and deck."""
        return Card.objects.raw(
            """SELECT *
        FROM cards
        JOIN decks ON decks.id = cards.deck_id
        JOIN card_user ON card_user.card_id = cards.id
        WHERE decks.id = %(deck_id)s
        AND card_user.user_id = %(user_id)s
        AND card_user.is_learned = FALSE
        LIMIT 5""",
            params,
        )
