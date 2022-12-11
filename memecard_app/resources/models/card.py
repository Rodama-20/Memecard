from django.db import models

from .user import User
from .deck import Deck

class Card(models.Model):
    """A card in a deck."""
    creator = models.ForeignKey(
        User, models.SET_NULL, db_column='creator', blank=True, null=True)
    deck = models.ForeignKey(Deck, models.CASCADE)
    order = models.IntegerField(blank=True, null=True)
    public = models.BooleanField()
    nb_faces = models.IntegerField()

    # Many-to-many fields
    users = models.ManyToManyField(User, through='CardUser', related_name='cards')

    class Meta:
        managed = False
        db_table = 'cards'