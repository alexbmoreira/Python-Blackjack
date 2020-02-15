import random

class Deck():

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        string = ""
        length = len(self.cards) - 1

        if length < 0:
            return string

        for card in self.cards:
            string += str(card) + "\n"

        return string

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        card_index = random.randint(0, len(self.cards) - 1)
        card = self.cards.pop(card_index)

        return card


if __name__ == "__main__":
    
    import random
    from card import *

    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", \
             "Jack", "Queen", "King", "Ace"]
    values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, \
              "Jack":10, "Queen":10, "King":10, "Ace":11}
    cards = []

    for suit in suits:
        for rank in ranks:
            cards.append(Card(suit, rank, values.get(rank)))

    deck = Deck(cards)

    print(f"{deck} - {len(deck)}")
    deck.shuffle()
    #print(deck)
    print("\n\n\n\n")

    card = deck.deal()
    print(f"{card} - {card.value}")
