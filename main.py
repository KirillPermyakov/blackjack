import random

deck_count = 4

types_of_cards = {'A': 11,
                  'K': 10,
                  'Q': 10,
                  'J': 10,
                  '10': 10,
                  '9': 9,
                  '8': 8,
                  '7': 7,
                  '6': 6,
                  '5': 5,
                  '4': 4,
                  '3': 3,
                  '2': 2}


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


def hand_values(hand, cards):
    sum_of_values = 0
    for card in hand:
        sum_of_values += cards.get(card)
    return sum_of_values


values = hand_values(hand, types_of_cards)
dealer_values = hand_values(dealer, types_of_cards)
print(hand)
print(values)
#print(deck)
while not values >= 21:
    more = input('взять ещё карту? ')
    if more == 'да':
        hand.append(deck.pop(0))
        values = hand_values(hand, types_of_cards)
        print(hand)
        print(values)
    elif more == 'нет':
        if values > dealer_values and values <= 21:
            print('you win')
            break
        else:
            print('you lose')
            break
