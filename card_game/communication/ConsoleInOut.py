import sys
from typing import List, Type, TypeVar
from enum import Enum

from card_game.card.entity.Hand import *
from card_game.card.entity.Card import *
from card_game.communication.YesOrNo import YesOrNo
from card_game.Player import *

# Define a type variable for enum types
T = TypeVar('T', bound=Enum)

default_list_question = "Please select an item"
select_card = "Please select a card"
wrong_index = "Please select an index in range."
enter_integer = "Please enter an integer"
output_on = True
input_on = True

user_input = sys.stdin

def set_input(input_stream) -> None:
    """Set a custom input stream (for testing or redirection)."""
    user_input = input_stream

def set_output_on(on: bool) -> None:
    output_on = on

def get_string() -> str:
    return input()

def get_integer() -> int:
    max_attempts = 5
    for _ in range(max_attempts):
        try:
            return int(get_string())
        except ValueError:
            display(enter_integer)
    return -1  # Return -1 if all attempts fail

def get_input_string(message: str) -> str:
    display(message)
    return get_string()

def get_input_integer(message: str) -> int:
    display(message)
    return get_integer()

def get_list_index(selection: List[str]) -> int:
    return get_list_index_with_question(default_list_question, selection)

def get_list_index_with_question(question: str, selection: List[str]) -> int:
    max_retries = 3
    display(question)
    for i, item in enumerate(selection):
        display(f"{i} - {item}")
    for _ in range(max_retries):
        index = get_integer()
        if 0 <= index < len(selection):
            return index
        display(wrong_index)
    return len(selection)  # Return the out-of-bounds index if exceeded retries

def get_enum_index(selection: Type[T]) -> T:
    return get_enum_index_with_question(default_list_question, selection)

def get_enum_index_with_question(question: str, selection: Type[T]) -> T:
    enum_constants = [enum_member.name for enum_member in selection]
    index = get_list_index_with_question(question, enum_constants)
    return selection.values()[index]

def get_yes_or_no(question: str) -> YesOrNo:
    answer = get_input_string(question)
    if 'y' in answer.lower() or answer == '0':
        return YesOrNo.YES
    return YesOrNo.NO

def display(message):
    if output_on:
        print(message)

def display_player(player) -> None:
    display(str(player))

def get_players_card(player):
    display_player_with_visibility(player)
    return play_a_card(player, get_input_integer(select_card))

def display_player_with_visibility(player) -> None:
    display(display_hand_with_visibility(player))

def display_card(name: str, card) -> None:
    display(f"{name} {card}")

def display_hand_of_cards(hand):
    for card in hand:
        display(card)

def display_hand(hand, name: str, ) -> None:
    display(f"{name} {display_hand_of_cards(hand)}")

def main():
    selected_enum = get_enum_index(YesOrNo)
    display(str(selected_enum))

# Entry point for the application
if __name__ == "__main__":
    main()