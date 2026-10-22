from typing import Dict

from card_game.card.entity.FaceCard import *

def get_card_ordinal(card):
    return get_face_card_order(card[1:])

def get_card_score(card):
    return get_face_card_score(card[1:])

def suit_face_order(card):
    return f"{card[0]}{str(get_card_ordinal(card))}"
