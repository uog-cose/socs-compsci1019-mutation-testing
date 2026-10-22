import random
from card_game.card.entity.FaceCard import *
from card_game.card.entity.Hand import *
from card_game.card.entity.Suit import *

random = random.Random()
small_deck_size = 8

def create_deck(deck_override=""):
    if deck_override == "":
        hand_of_cards = generate_deck()
    else:
        hand_of_cards = create_hand(deck_override)
    return hand_of_cards
    
def generate_deck():
    hand_of_cards = []
    for suit in suits:
        for counter in range(2,11):
            add_card_to_hand(hand_of_cards, suit[0] + str(counter))
        for rank in face_cards.keys():
            add_card_to_hand(hand_of_cards, suit[0] + rank)
    return hand_of_cards

def play_a_card_from_deck(hand_of_cards):
    if len(hand_of_cards) == 0:
        hand_of_cards = generate_deck()
    index = len(hand_of_cards) - 1
    if index > small_deck_size:
        index = random.randint(0, index)
    return play_a_card(hand_of_cards, index=index)

