from card import *
from hand import *
from deck import *

def print_hands(player, dealer):
    print("-------------------------")
    print("Your cards:")
    print(f"{player}")
    print(f"Value: {player.value}\n")

    print("Dealer cards:")
    print(f"{dealer}")
    if dealer.cards[1].face_down:
        print(f"Value: {dealer.value - dealer.cards[1].value}")
    else:
        print(f"Value: {dealer.value}")
    print("-------------------------")

def get_input():
    while True:
        move = input("'hit' or 'stay'? (q to exit): ").lower()

        if move == "hit" or move == "stay" or move == "q":
            print()
            return move
        
        print("Not a valid choice")

def play_again():
    while True:
        choice = input("Play again? ('yes' or 'no'): ").lower()

        if choice == "yes" or choice == "no":
            print()
            return choice
        
        print("Not a valid choice")

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

    deck.shuffle()

    return deck, player, dealer

def make_move(deck, player, dealer):
    while True:
        print_hands(player, dealer)
        move = get_input()

        if move == "q":
            print("Goodbye")
            return "quit"

        if move == "hit":
            card = deck.deal()
            player.hit(card)
            print(f"Hit: {card}")
            if player.check_bust():
                print("Bust! You lost!")
                return
            continue
        
        if move == "stay":
            dealer.cards[1].face_down = False
            while dealer.value < 17:
                dealer.hit(deck.deal())
            
            if player.is_winner(dealer):
                print("Dealer busts! You Win!")
            else:
                print("Dealer wins!")
            return

def play(setup):
    deck = setup[0]
    player = setup[1]
    dealer = setup[2]

    print("Dealing cards...")
    temp_card = deck.deal()
    temp_card.face_down = True
    dealer.hit(deck.deal(), temp_card)
    player.hit(deck.deal(), deck.deal())

    outcome = make_move(deck, player, dealer)

    if outcome != "quit":
        print_hands(player, dealer)
        return play_again()

    return outcome



while play(initialize()) == "yes":
    pass

print("Thanks for playing\n")
