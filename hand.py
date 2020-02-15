class Hand():

    def __init__(self, cards = None, value = 0, aces = 0):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards

        self.value = value
        self.aces = aces

    def __str__(self):
        string = ""
        length = len(self.cards) - 1

        if length < 0:
            return string

        for i in range(0, length):
            string += str(self.cards[i]) + "\n"

        return string + str(self.cards[length])

    def __len__(self):
        return len(self.cards)
        
    def hit(self, *args):
        for card in args:
            self.cards.append(card)
            self.value += card.value

            if(card.rank == "Ace"):
                if self.value > 21:
                    self.value -= 10
                    card.value = 1

                self.aces += 1

    def check_bust(self):
        if self.value > 21:
#            if self.aces == 0:
#                return True
#
#            for i in range(0, self.aces):
#                self.value -= 10
#
#                if self.value <= 21:
#                    return False
#            
            return True
        
        return False

    def check_winner(self, dealer):
        if dealer.value > 21:
            return True
        if self.value > 21:
            return False
        
        if 21 - self.value < 21 - dealer.value:
            return True
        
        return False

if __name__ == "__main__":
    import random
    from deck import *
    from card import *

    hand_a = Hand()
    card_a = Card("Hearts", "King", 10)

    hand_a.hit(card_a, Card("Hearts", "Jack", 10), Card("Clubs", "Ace", 11))
    print(f"{hand_a} - {hand_a.value}")
    print(hand_a.check_bust())

    print()
    
    hand_b = Hand()
    card_b1 = Card("Spades", "Queen", 10)
    card_b2 = Card("Clubs", "King", 10)
    card_b3 = Card("Diamonds", "Six", 6)

    hand_b.hit(card_b1, card_b2, card_b3)
    print(f"{hand_b} - {hand_b.value}")
    print(hand_b.check_bust())

    print(hand_a.check_winner(hand_b))         # Should be True