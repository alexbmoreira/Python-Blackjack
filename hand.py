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

        for card in self.cards:
            if not card.face_down:
                string += str(card) + "\n"
            else:
                string += "*Face down*" + "\n"

        return string[:-1]

    def __len__(self):
        return len(self.cards)
        
    def hit(self, *args):
        for card in args:
            self.cards.append(card)
            self.value += card.value
            if(card.rank == "Ace"):
                self.aces += 1

            if self.value > 21 and self.aces > 0:
                for ace in self.cards:
                    if ace.rank == "Ace" and ace.value == 11:
                        self.value -= 10
                        ace.value = 1
                        self.aces -= 1
                        break

    def check_bust(self):
        if self.value > 21:
            return True
        
        return False

    def is_winner(self, dealer):
        if dealer.check_bust():
            return True
        
        if 21 - dealer.value < 21 - self.value:
            return False
        
        return True

if __name__ == "__main__":
    import random
    from deck import *
    from card import *

    hand_a = Hand()
    card_a1 = Card("Hearts", "Ace", 11)
    card_a2 = Card("Spades", "Ace", 11)
    card_a3 = Card("Hearts", "King", 10)

    hand_a.hit(card_a1, card_a2)

    print(f"{hand_a}")
    print(f"Value: {hand_a.value}\n")

    hand_a.hit(card_a3)

    print(f"{hand_a}")
    print(f"Value: {hand_a.value}\n")
