# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    email = models.CharField(unique=True, max_length=50)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'users'


class CardType(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.CharField(max_length=1000000)

    class Meta:
        managed = False
        db_table = 'card_types'


class Deck(models.Model):
    name = models.CharField(max_length=30)
    public = models.BooleanField()
    strict_one_way = models.BooleanField()
    card_type = models.ForeignKey(CardType, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'decks'


class DeckUser(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)
    deck = models.ForeignKey(Deck, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'deck_user'
        unique_together = (('user', 'deck'),)


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'tags'


class DeckTag(models.Model):
    deck = models.ForeignKey(Deck, models.CASCADE)
    tag = models.OneToOneField(Tag, models.CASCADE, primary_key=True)

    class Meta:
        managed = False
        db_table = 'deck_tag'
        unique_together = (('tag', 'deck'),)


class Card(models.Model):
    creator = models.ForeignKey(
        User, models.SET_NULL, db_column='creator', blank=True, null=True)
    deck = models.ForeignKey(Deck, models.CASCADE)
    order = models.IntegerField(blank=True, null=True)
    public = models.BooleanField()
    nb_faces = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cards'


class FaceType(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.CharField(max_length=1000000)
    question = models.BooleanField()
    response = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'face_types'


class CardTypeFaceType(models.Model):
    card_type = models.OneToOneField(
        CardType, models.DO_NOTHING, primary_key=True)
    face_type = models.ForeignKey(FaceType, models.DO_NOTHING)
    name = models.CharField(max_length=30)
    required = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'card_type_face_type'
        unique_together = (('card_type', 'face_type', 'name'),)


class Meme(models.Model):
    card = models.ForeignKey(Card, models.CASCADE)
    url = models.CharField(max_length=256)
    reports = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'memes'


class CardUser(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)
    card = models.ForeignKey(Card, models.CASCADE)
    is_learned = models.BooleanField()
    is_known = models.BooleanField()
    meme = models.ForeignKey(Meme, models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_user'
        unique_together = (('user', 'card'),)


class Face(models.Model):
    card = models.ForeignKey(Card, models.CASCADE)
    type = models.ForeignKey(FaceType, models.DO_NOTHING)
    content = models.CharField(max_length=1000000, blank=True, null=True)
    reports = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faces'


class FaceFaceUser(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)
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


class RevLog(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    card = models.ForeignKey(Card, models.CASCADE)
    answer = models.IntegerField()
    interval = models.IntegerField()
    easiness_factor = models.IntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rev_log'


class UpdateDeckLog(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    deck = models.ForeignKey(Deck, models.SET_NULL, blank=True, null=True)
    card = models.ForeignKey(Card, models.SET_NULL, blank=True, null=True)
    tag = models.ForeignKey(Tag, models.SET_NULL, blank=True, null=True)
    action = models.CharField(max_length=30)
    old_name = models.CharField(max_length=30)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'update_deck_log'


class UpdateTagLog(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    tag = models.ForeignKey(Tag, models.DO_NOTHING, blank=True, null=True)
    old_name = models.CharField(max_length=30)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'update_tag_log'


class UpdateCardLog(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    card = models.ForeignKey(Card, models.SET_NULL, blank=True, null=True)
    face_id = models.IntegerField(blank=True, null=True)
    old_content = models.CharField(max_length=1000000)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'update_card_log'


class UpdateMemeLog(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    meme = models.ForeignKey(Meme, models.SET_NULL, blank=True, null=True)
    old_url = models.CharField(max_length=256)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'update_meme_log'
