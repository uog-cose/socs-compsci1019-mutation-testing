from card_game.communication import YesOrNo
from card_game.card.CardGame import *
from card_game.card.entity.Hand import *
from card_game.communication.YesOrNo import YesOrNo
from card_game.communication.ConsoleInOut import *


want_to_snap = "Do you want to Snap?"
discard_pile_message = "Discard Pile"
rounds_to_win = 2
number_of_players = 2
no_of_cards = 0
discard_pile = create_hand()

def play(override="") -> None:
    deck = initiate(no_of_cards, override)
    while not players[user_index][WINNER] and len(players[user_index][HAND]) > 0:
        player_plays_hand(players[user_index])
    reset_players()
    winner = determine_winner()
    winner[WINNER] = True
    show_players()

def has_snapped(player, is_snap, discard_pile):
    if is_snap.value == YesOrNo.YES.value and len(discard_pile) >=2:
        if get_last_card(discard_pile)[1:] == get_second_last_card(discard_pile)[1:]:
            increment_score(player, 1)
        else:
            increment_score(player,-1)

def get_number_of_players():
    return number_of_players

def player_plays_hand(player):
    card_played = play_a_card(player[HAND])
    discard_pile.append(card_played)
    display_card(discard_pile_message, get_last_card(discard_pile))
    is_snap = get_yes_or_no(want_to_snap)
    has_snapped(player, is_snap, discard_pile)
    print("You have scored " + str(player[SCORE]))
    if player[SCORE] >= rounds_to_win:
        player[WINNER] = True

