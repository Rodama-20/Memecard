# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


from .resources.models.user import User
from .resources.models.card_type import CardType
from .resources.models.deck import Deck
from .resources.models.deck_user import DeckUser
from .resources.models.tag import Tag
from .resources.models.deck_tag import DeckTag
from .resources.models.card import Card
from .resources.models.face_type import FaceType
from .resources.models.card_type_face_type import CardTypeFaceType
from .resources.models.meme import Meme
from .resources.models.card_user import CardUser
from .resources.models.face import Face
from .resources.models.face_face_user import FaceFaceUser
from .resources.models.rev_log import RevLog
from .resources.models.update_deck_log import UpdateDeckLog
from .resources.models.update_tag_log import UpdateTagLog
from .resources.models.update_card_log import UpdateCardLog
from .resources.models.update_meme_log import UpdateMemeLog
