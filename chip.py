class Chip():

    def __init__(self, total = 500, bet = 0):
        self.total = total
        self.bet = bet

    def win(self):
        self.total += self.bet

    def lose(self):
        self.total -= self.bet

if __name__ == "__main__":
