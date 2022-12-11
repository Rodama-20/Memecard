from django.db import models

class CardType(models.Model):
    """A type of card, defining the fields it has."""
    name = models.CharField(unique=True, max_length=30)
    description = models.CharField(max_length=1000000)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'card_types'
