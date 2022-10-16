import random

deck_count = 4

types_of_cards = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']


def generate_deck(cards, decks):
    new_deck = []
    for card in cards:
        new_list = [card]
        new_deck.extend(new_list * decks)
    random.shuffle(new_deck)
    return new_deck


deck = generate_deck(types_of_cards, deck_count)


def deal_cards():
    two_cards = []
    for i in range(2):
        two_cards.append(deck.pop(0))
    return two_cards


dealer = deal_cards()
hand = deal_cards()

print(dealer, hand)
print(deck)
