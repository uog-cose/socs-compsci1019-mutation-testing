from typing import Optional

from card_game.Game import *
from card_game.communication.ConsoleInOut import *
from card_game.card.entity.PlayerType import *
from card_game.card.entity.Hand import *
from card_game.card.entity.Deck import *
from card_game.card.CardSelectHelp import CardSelectHelp


no_of_cards = 2
ask_card_to_play = "Select card by number starting with zero"
dealer_name = "Dealer"
computer_player_prefix = "Comp - "

discard_pile = create_hand()

def create_dealer(computer_names) -> None:
    add_player(create_player(DEALER, get_next_computer_name(computer_names)))

def get_players_card(player):
    return get_players_card(player)

def initiate_players(name, number_of_players) -> None:
    clear_players()
    computer_names = get_computer_players_names()
    create_dealer(computer_names)
    create_human_player(name)
    create_computer_competitors(number_of_players - 2, computer_names)

def get_card_to_play() -> int:
    return get_input_integer(ask_card_to_play)

def score_hand(hand) -> int:
    # TODO: Implement scoring logic
    return 0

def get_score(player) -> int:
    score = sum(score_hand(player.get_hand_at_index(counter)) for counter in range(player.get_number_of_hands()))
    return score

def user_plays(competitor) -> None:
    pass  # TODO: Implement user play logic

def computer_plays(competitor) -> None:
    pass  # TODO: Implement computer play logic

def after_play_of_round() -> None:
    pass  # TODO: Implement after round logic

def before_play_of_round() -> None:
    pass  # TODO: Implement before round logic

def deal_cards(deck, no_of_cards) -> None:
    all_cards = False
    if no_of_cards == 0:
        no_of_cards = len(deck) // get_players_size()
        all_cards = True
    else:
        no_of_cards = no_of_cards
    
    for counter in range(get_players_size()):
        player = players[counter]
        player[HAND] = deal_hand(deck, no_of_cards)

    if all_cards:
        for counter in range(get_players_size()):
            player = players[counter]
            if len(deck) > 0:
                add_card_to_hand(player[HAND], play_a_card_from_deck(deck))

def deal_hand(deck, no_of_cards_to_deal: int):
    hand = create_hand()
    for counter in range(no_of_cards_to_deal):
        if len(deck) > 0:
            hand.append(play_a_card_from_deck(deck))
    return hand

def player_select_card(player, deck):
    display_card("Discard Pile", get_last_discarded_card())
    display_player_with_visibility(player)
    user_choice = get_enum_index(CardSelectHelp)
    if user_choice == CardSelectHelp.DISCARD:
        return play_a_card(discard_pile)
    else:
        return play_a_card_from_deck(deck)

def add_to_discarded(card) -> None:
    discard_pile.add(card)

def get_last_discarded_card():
    return discard_pile.get_last_card()

def initiate(no_of_cards, deck_override="") -> None:
    name, number_of_players = get_game_info()
    initiate_players(name, number_of_players)
    deck = create_deck(deck_override)
    deal_cards(deck, no_of_cards)
    return deck
