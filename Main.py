from card_game.card.game.Snap.Snap import play as snap_play
from card_game.card.game.TwentyOne.TwentyOne import play as twenty_one_play



if __name__ == "__main__":
    print("Start Twenty One")
    twenty_one_play()
    print("Start Snap")
    snap_play("D3,H3,C3,S3,S4,C4,H4")