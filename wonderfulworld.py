from cardbank import Cardbank
import time
import itertools

def set_next_round_ressources():
    grey = input("Enter your value for grey: ") or 0
    black = input("Enter your value for black: ") or 0
    green = input("Enter your value for green: ") or 0
    yellow = input("Enter your value for yellow: ") or 0
    blue = input("Enter your value for blue: ") or 0
    return [grey, black, green, yellow, blue]


def set_drafted_card():
    drafted_cards = []
    for i in range(7):
        try:
            # drafted_cards.append(bank.card_from_name(input("Enter your value for card {}: ".format(i))))
            drafted_cards.append(bank.card_from_name("submarine"))

        except KeyError:
            print('error with the card')
            i = i-1
    return drafted_cards


def set_early_ressources(cards, scenario):
    grey, black, green, yellow, blue = 0, 0, 0, 0, 0
    for i in range(len(cards)):
        if scenario[i]:
            grey = grey + cards[i].discard_reward.grey
            black = black + cards[i].discard_reward.black
            green = green + cards[i].discard_reward.green
            yellow = yellow + cards[i].discard_reward.yellow
            blue = blue + cards[i].discard_reward.blue
    return [grey, black, green, yellow, blue]


if __name__ == "__main__":

    bank = Cardbank()

    res = set_next_round_ressources()

    cards = set_drafted_card()

    scenarios = list(itertools.product([0, 1], repeat=7))
    for scenario in scenarios:
        early_ressources = set_early_ressources(cards, scenario)


    pass