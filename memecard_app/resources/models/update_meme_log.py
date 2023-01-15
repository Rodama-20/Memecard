"""The update log of memes

(c) 2023 He-Arc Cyrille Polier
"""

from django.db import models

from .meme import Meme
from .user import User


class UpdateMemeLog(models.Model):
    """The update log of memes"""

    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    meme = models.ForeignKey(Meme, models.SET_NULL, blank=True, null=True)
    old_url = models.CharField(max_length=256)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "update_meme_log"
