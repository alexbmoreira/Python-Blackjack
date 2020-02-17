import card
import hand
import deck
import chip

LINES = 31
SUITS = ["Spades", "Hearts", "Clubs", "Diamonds"]
RANKS = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", \
         "Ten", "Jack", "Queen", "King", "Ace"]
VALUES = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, \
          "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}
chips = chip.Chip()

def print_hands(player, dealer, chips):    
    print("-" * LINES)
    print(f"Your bet: ${chips.bet}")
    print("Your cards:")
    print(f"{player}")
    print(f"Value: {player.value}\n")

    print("Dealer cards:")
    print(f"{dealer}")
    if dealer.cards[1].face_down:
        print(f"Value: {dealer.value - dealer.cards[1].value}")
    else:
        print(f"Value: {dealer.value}")
    print("-" * LINES)

def place_bet(chips):
    while True:
        try:
            chips.bet = int(input("Place a bet: $"))
        except ValueError:
            print("Please bet a numerical value!")
        else:
            if chips.bet > chips.total:
                print("You don't have enough money!")
                continue
            else:
                break

def get_input():
    while True:
        move = input("'hit' or 'stay'? (q to exit): ").lower()

        if move in ("hit", "stay", "q"):
            print()
            return move

        print("Not a valid choice")

def play_again():
    while True:
        choice = input("Play again? ('yes' or 'no'): ").lower()

        if choice in ("yes", "no"):
            print()
            return choice

        print("Not a valid choice")

def initialize(chips):
    print("\n" * 5 + "=" * LINES)
    print("Welcome to blackjack in python!\n")
    print(f"Players chip count is: ${chips.total}")

    cards = []

    for suit in SUITS:
        for rank in RANKS:
            cards.append(card.Card(suit, rank, VALUES.get(rank)))

    card_deck = deck.Deck(cards)
    player = hand.Hand()
    dealer = hand.Hand()

    card_deck.shuffle()

    place_bet(chips)

    return card_deck, player, dealer, chips

def make_move(card_deck, player, dealer, chips):   
    while True:
        print_hands(player, dealer, chips)
        move = get_input()

        if move == "q":
            print("Goodbye")
            return "quit"

        if move == "hit":
            dealt_card = card_deck.deal()
            player.hit(dealt_card)
            print(f"Hit: {dealt_card}")
            if player.check_bust():
                print(f"Bust! You lost ${chips.bet}!")
                chips.lose()
                if chips.total < 1:
                    print("You've lost all your money!")
                    return "over"
                return "game"
            continue

        if move == "stay":
            dealer.cards[1].face_down = False
            while dealer.value < 17:
                dealer.hit(card_deck.deal())

            if player.is_winner(dealer):
                print(f"You Win ${chips.bet}!")
                chips.win()
            else:
                if dealer.value != player.value:
                    print(f"Dealer wins! You lost ${chips.bet}")
                    chips.lose()
                    if chips.total < 1:
                        print("You've lost all your money!")
                        return "over"
            return "game"

def play(setup):
    card_deck = setup[0]
    player = setup[1]
    dealer = setup[2]
    chips = setup[3]

    print("Dealing cards...")
    temp_card = card_deck.deal()
    temp_card.face_down = True
    dealer.hit(card_deck.deal(), temp_card)
    player.hit(card_deck.deal(), card_deck.deal())

    outcome = make_move(card_deck, player, dealer, chips)

    if outcome != "quit":
        print_hands(player, dealer, chips)
        if outcome != "over":
            return play_again()
    
    return outcome


chips = chip.Chip()
while play(initialize(chips)) == "yes":
    pass

print(f"Thanks for playing. You took home ${chips.total}\n")
