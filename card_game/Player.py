from typing import List
from card_game.card.entity.Hand import *

HAND = "HAND"
COMPETITOR_TYPE = "COMPETITOR_TYPE"
FIRST_NAME = "FIRSTNAME"
WINNER = "WINNER"
SCORE = "SCORE"
level_of_risk = 14

def create_player(competitor_type, first_name: str):
    player = {}
    player[HAND] = create_hand()
    player[COMPETITOR_TYPE] = competitor_type
    player[FIRST_NAME] = first_name
    player[WINNER] = False
    player[SCORE] = 0
    return player

def increment_score(player, score: int) -> None:
    player[SCORE] += score

def get_level_of_risk(player) -> int:
    return level_of_risk

def has_won(player) -> bool:
    return player[WINNER]

def get_card(player, index: int):
    return get_card(player[HAND], index)

def has_hand(player) -> bool:
    return not hand_is_empty(player[WINNER])

def player_add_card(player, card) -> None:
    player[HAND].append(card)

def player_display_hand(player) -> str:
    return hand_display(player[HAND])

def display_hand_with_visibility(player) -> str:
    display = base_to_string(player)
    for card in player[HAND]:
        display += f"\n{card}"
    return display.strip()

def player_play_a_card(player, index: int):
    return play_a_card(player[HAND], index)

def set_hand(player, hand):
    player[HAND] = hand

def base_to_string(player) -> str:
    display = ""
    if player[WINNER]:
        display = "The winner is "

    display += player[FIRST_NAME]
    if player[SCORE] > 0:
        display += f" with score: {player[SCORE]}"
    return display

def player_display(player) -> str:
    display = base_to_string(player)
    display += f"\n{str(player[HAND])}"
    return display