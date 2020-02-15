from card import *
from hand import *
from deck import *

def initialize():
    print("Welcome to blackjack in python!\n")

    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", \
            "Jack", "Queen", "King", "Ace"]
    values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, \
            "Jack":10, "Queen":10, "King":10, "Ace":11}
    cards = []

    for i in range(0, len(suits)):
        for j in range(0, len(ranks)):
            cards.append(Card(suits[i], ranks[j], values.get(ranks[j])))

    deck = Deck(cards)
    player = Hand()
    dealer = Hand()

    return deck, player, dealer

def play(setup):
    deck = setup[0]
    player = setup[1]
    dealer = setup[2]

    print("Dealing cards...")
    temp_card = deck.deal()
    temp_card.face_down = True
    dealer.hit(deck.deal(), temp_card)
    player.hit(deck.deal(), deck.deal())

    while True:
        print("Your cards:")
        print(player)

        print("Dealer cards")
        print(dealer)

        while True:
            move = input("Hit or stay (q to exit): ").lower()

            if move == "hit" or move == "stay" or move == "q":
                break;
            else:
                print("Not a valid choice")


        if move.lower() == "q":
            return "quit"

        if move.lower() == "hit":
            player.hit(deck.deal())
            if not player.check_bust():
                print("                     -hi")
                continue
            else:
                print("Bust! You lost!")
                return "game";
        
        break;



play(initialize())
