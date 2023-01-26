"""All the models for the memecard application.

(c) 2023 He-Arc Cyrille Polier
"""


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
