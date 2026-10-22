from typing import List, Dict
from card_game.card.entity.Card import *
    
def create_hand(list_of_cards=None):
    hand_of_cards = []
    if list_of_cards:
        if isinstance(list_of_cards, str):
            list_of_cards = list_of_cards.split(",")
        for card in list_of_cards:
            if card:
                add_card_to_hand(hand_of_cards, card)
    return hand_of_cards

def get_first_card(hand_of_cards):
    return hand_of_cards[0]

def get_last_card(hand_of_cards):
    return hand_of_cards[- 1]

def get_second_last_card(hand_of_cards):
    return hand_of_cards[-2]

def play_a_card(hand_of_cards, card=None, index=None):
    if card:
        if card in hand_of_cards:
            remove_card_from_hand(card)
            return card
        return None
    elif index is not None:
        return hand_of_cards.pop(index)
    return hand_of_cards.pop()

def add_card_to_hand(hand_of_cards, card):
    hand_of_cards.append(card)

def add_at_start(hand_of_cards, card):
    add_at(hand_of_cards, 0, card)

def add_at(hand_of_cards, index, card):
    hand_of_cards.insert(index, card)

def set_card_at(hand_of_cards, index, card):
    play_a_card(index=index)
    add_at(index, card)

def hand_is_empty(hand_of_cards):
    return not hand_of_cards

def remove_card_from_hand(hand_of_cards, card):
    if card in hand_of_cards:
        hand_of_cards.remove(card)

def clear_hand(hand_of_cards):
    hand_of_cards.clear()

def hand_size(hand_of_cards):
    return len(hand_of_cards)

def sort_hand(hand_of_cards):
    hand_of_cards.sort(key=lambda card: suit_face_order(card))

def sort_hand_by_face(hand_of_cards):
    hand_of_cards.sort(key=lambda card: get_face_card_ordinal(card))

def has_card(hand_of_cards, card):
    return card in hand_of_cards

def has_cards(hand_of_cards, cards):
    separated_cards = cards.split(",") if isinstance(cards, str) else cards
    return all(has_card(card) for card in separated_cards)

def play_cards(hand_of_cards, cards):
    result = False
    separated_cards = cards.split(",")
    for card in separated_cards:
        result = play_a_card(card)
    return result

def add_cards(hand_of_cards, cards):
    separated_cards = cards.split(",") if isinstance(cards, str) else cards
    for card in separated_cards:
        add_card_to_hand(hand_of_cards, card)

def highest_card_of_suit(hand_of_cards, suit):
    return max(
        (card for card in hand_of_cards if card[0] == suit.display_first_letter()),
        key=lambda card: get_face_card_ordinal(card),
        default=None
    )

def lowest_card_of_suit(hand_of_cards, suit):
    lowest_card = None
    for card in hand_of_cards:
        if card[0] == suit.display_first_letter():
            if lowest_card is None or get_face_card_ordinal(lowest_card) > get_face_card_ordinal(card):
                lowest_card = card
    return lowest_card

def highest_card_except_suit(hand_of_cards, suit):
    return max(
        (card for card in hand_of_cards if card[0] != suit.display_first_letter()),
        key=lambda card: get_face_card_ordinal(card),
        default=None
    )

def lowest_card_except_suit(hand_of_cards, suit):
    return min(
        (card for card in hand_of_cards if card[0] != suit.display_first_letter()),
        key=lambda card: get_face_card_ordinal(card),
        default=None
    )

def get_card(hand_of_cards, index):
    return hand_of_cards[index] if 0 <= index < len(hand_of_cards) else None

def display_visibility(hand_of_cards, counter=1):
    display = []
    for card in hand_of_cards:
        display.append(f"{counter} - {card}")
        counter += 1
    return ", ".join(display)

def hand_display(hand_of_cards):
    return ", ".join(str(card) for card in hand_of_cards).strip()