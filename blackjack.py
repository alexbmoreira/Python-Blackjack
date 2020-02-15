import random
import card
import hand
import deck

def main():
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", \
            "Jack", "Queen", "King", "Ace"]
    values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, \
            "Jack":10, "Queen":10, "King":10, "Ace":11}

    for i in range(0, len(suits)):
        for j in range(0, len(ranks)):
            cards.append(Card(suits[i], ranks[j], values.get(ranks[j])))