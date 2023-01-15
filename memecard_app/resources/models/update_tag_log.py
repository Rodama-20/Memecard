""" The update log of tags

(c) 2023 He-Arc Cyrille Polier
"""

from django.db import models

from .tag import Tag
from .user import User


class UpdateTagLog(models.Model):
    """The update log of tags"""

    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    tag = models.ForeignKey(Tag, models.DO_NOTHING, blank=True, null=True)
    old_name = models.CharField(max_length=30)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "update_tag_log"
