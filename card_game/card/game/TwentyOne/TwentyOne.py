from card_game.Player import *
from card_game.card.CardGame import *
from card_game.communication.ConsoleInOut import *
from card_game.card.entity.PlayerType import *
from card_game.card.entity.FaceCard import *
from card_game.card.game.TwentyOne.TwentyOneActions import TwentyOneActions

max_score = 21
        
def play_a_round(deck) -> None:
    for player in players:
        if player[COMPETITOR_TYPE] == USER:
            user_plays(player, deck)
        else:
            computer_plays(player, deck)

def play(override="") -> None:
    deck = initiate(no_of_cards, override)
    play_a_round(deck)
    reset_players()
    winner = determine_winner()
    winner[WINNER] = True
    show_players()

def generate_help():
    return get_enum_index(TwentyOneActions)

def get_player_action(player) -> TwentyOneActions:
    if len(player[HAND]) > 0:
        print(player[HAND])
    return generate_help()

def user_plays(player, deck):
    player[SCORE] = score_hand(player[HAND])
    user_action = TwentyOneActions.TWIST
    while player[SCORE] > 0 and user_action != TwentyOneActions.STICK.num:
        user_action = get_player_action(player)
        if user_action == TwentyOneActions.TWIST.num:
            player[HAND].append(play_a_card_from_deck(deck))
            player[SCORE]= score_hand(player[HAND])

def computer_plays(player, deck):
    hand = player[HAND]
    player[SCORE] = score_hand(hand)
    while player[SCORE] <= get_level_of_risk(player):
        hand.append(play_a_card_from_deck(deck))
        player[SCORE] = score_hand(hand)

def score_hand(hand) -> int:
    score = 0
    has_an_ace = False
    for card in hand:
        if card[1] == ace:
            has_an_ace = True
        score += get_card_score(card)
    if score > max_score and has_an_ace:
        score -= get_face_card_score(ace) - 1
    if score > max_score:
        score = 0
    return score