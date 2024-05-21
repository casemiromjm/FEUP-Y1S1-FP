from cards import * # import everything from cards.py
import random

def card_value(card):
    CARDS_VALUES = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J":10, "Q": 10, "K": 10, "A": 11}

    suit, rank = card

    value = CARDS_VALUES[rank]

    if suit == "♣" or suit == "♠":
        value = value * 2
    return value


def play(seed_value):
    random.seed(seed_value)
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)
    wins = [0, 0, 0, 0]
    while hands[start_player]:
        lista = []
        for name in turn_order:
            card = choose(hands[name])
            lista.append(card_value(card))
            hands[name].remove(card)
        max1 = max(lista)
        for i in range(len(lista)):
            if lista[i] == max1:
                wins[i] += 1
    max2 = max(wins)
    res = ""
    if wins[turn_order.index("P1")] == max2:
        res += "P1 "
    if wins[turn_order.index("P2")] == max2:
        res += "P2 "
    if wins[turn_order.index("P3")] == max2:
        res += "P3 "
    if wins[turn_order.index("P4")] == max2:
        res += "P4 "
    # for i in range(4):
    #     if wins[i] == max2:
    #         res += turn_order[i] + " "
    return res[:-1]