""" FaceFaceUser model.

(c) 2023 He-Arc Cyrille Polier
"""

from django.db import models

from .face import Face
from .meme import Meme
from .user import User


class FaceFaceUser(models.Model):
    """Helper table for many-to-many relationship between faces pairs and users."""

    user = models.OneToOneField(User, models.CASCADE)
    face_one = models.ForeignKey(Face, models.CASCADE, related_name="face_one")
    face_two = models.ForeignKey(Face, models.CASCADE, related_name="face_two")
    next_due = models.DateTimeField()
    repetition = models.IntegerField()
    interval = models.IntegerField()
    easiness_factor = models.IntegerField()
    meme = models.ForeignKey(Meme, models.SET_NULL, blank=True, null=True)
    is_known = models.BooleanField()

    class Meta:
        managed = False
        db_table = "face_face_user"
        unique_together = (("user", "face_one", "face_two"),)

    def get_card_for_review(self, user_id: int, deck_id: int):
        """Get a card for review."""
        return FaceFaceUser.objects.raw(
            """SELECT *
            FROM face_face_user
            JOIN faces ON face_face_user.face_one_id = faces.id
            JOIN cards ON faces.card_id = cards.id
            JOIN decks ON cards.deck_id = decks.id
            WHERE face_face_user.user_id = %s
            AND decks.id = %s
            AND face_face_user.next_due <= NOW()
            ORDER BY face_face_user.next_due
            LIMIT 5""",
            [user_id, deck_id],
        )

    def __str__(self) -> str:
        face1 = Face.objects.get(id=self.face_one)
        face2 = Face.objects.get(id=self.face_two)
        return face1.content + " - " + face2.content
