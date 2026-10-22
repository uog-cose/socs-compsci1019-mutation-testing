face_cards = {"J" : 11, "Q" : 12, "K" : 13, "A" : 14}
ace = "A"

def get_face_card_score(face_card):
    if face_card == ace:
        score = 11
    elif face_card in face_cards.keys():
        score = 10
    else:
        score = int(face_card)
    return score

def get_face_card_order(face_card):
    if face_card in face_cards.keys():
        order = face_cards.get(face_card)
    else:
        order = int(face_card)
    return order