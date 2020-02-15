class Card():

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"

if __name__ == "__main__":
    card = Card("Hearts", "Two", 2)

    print(card)
    print()
