import csv
from typing import List, Dict, Type, TypeVar
from enum import Enum

from card_game.communication.ConsoleInOut import *
from card_game.card.entity.PlayerType import *
from card_game.Player import *
from card_game.LoadCSV import *

# Define a type variable for enum types
T = TypeVar('T', bound=Enum)

winning_score = 0
ask_name = "What is your name"
ask_number_of_competitors = "How many competitors, minimum of two?"
player_names_file = "resource/card_player.csv"
user_index = 1

computer_names = []
players = []
finish_game = False

def get_player(index: int):
    return players[index]

def get_players():
    return players

def get_finish_game() -> bool:
    return finish_game

def get_players_size() -> int:
    return len(players)

def clear_players() -> None:
    players.clear()

def reset_players() -> None:
    for player in players:
        player[WINNER] = False

def get_number_of_players() -> int:
    return get_input_integer(ask_number_of_competitors)

def get_game_info():
    name = get_input_string(ask_name)
    number_of_players = get_input_integer(ask_number_of_competitors)
    return name, number_of_players
    
def initiate_players(name, number_of_players) -> None:
    players.clear()
    create_human_player(name)
    computer_names = get_computer_players_names()
    create_computer_competitors(number_of_players - 1, computer_names)

def add_player(competitor) -> None:
    players.append(competitor)

def create_human_player(name) -> None:
    add_player(create_player(USER, name))

def get_computer_players_names():
    if not computer_names:
        raw_player_names = get_csv_rows(player_names_file)
        for raw_player in raw_player_names:
            computer_names.append(raw_player[1])
    return computer_names

def get_next_computer_name(computer_names):
    return computer_names.pop(0)

def create_computer_competitors(no_of_computer_competitors: int, computer_names) -> None:
    for name in computer_names[:no_of_computer_competitors]:
        add_player(create_player(COMPUTER, name))

def determine_winner():
    winning_score = -1
    winning_player = None
    individual_has_won = False
    for player in players:
        current_score = player[SCORE]
        if player[WINNER]:
            winning_player = player
            individual_has_won = True
        if not individual_has_won and current_score > winning_score:
            winning_score = current_score
            winning_player = player
    return winning_player

def show_players() -> None:
    for player in players:
        display_player_with_visibility(player)
