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


def you_win():
    print('you win')
    print(dealer_values)


def you_lose():
    print('you lose')
    print(dealer_values)


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
while not values >= 21:
    more = input('взять ещё карту? ')
    if more == 'да':
        hand.append(deck.pop(0))
        values = hand_values(hand, types_of_cards)
        print(hand)
        print(values)
        if values > 21:
            you_lose()
            break
    elif more == 'нет':
        if dealer_values > 21:
            you_win()
            break
        elif 21 >= values > dealer_values:
            you_win()
            break
        else:
            you_lose()
            break
