from django.db import models

from .face import Face
from .meme import Meme
from .user import User

class FaceFaceUser(models.Model):
    """Helper table for many-to-many relationship between faces pairs and users."""
    user = models.OneToOneField(User, models.CASCADE)
    face_one = models.ForeignKey(Face, models.CASCADE, related_name='face_one')
    face_two = models.ForeignKey(Face, models.CASCADE, related_name='face_two')
    next_due = models.DateTimeField()
    repetition = models.IntegerField()
    interval = models.IntegerField()
    easiness_factor = models.IntegerField()
    meme = models.ForeignKey(Meme, models.SET_NULL, blank=True, null=True)
    is_known = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'face_face_user'
        unique_together = (('user', 'face_one', 'face_two'),)