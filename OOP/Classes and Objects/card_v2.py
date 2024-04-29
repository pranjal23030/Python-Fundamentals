import random


class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8",
             "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # return f"{self.rank} of {self.suit}"
        return f"{Card.ranks[self.rank]} of {Card.suits[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = []
        self.update()
        # self.shuffle()

    def update(self):
        ##        for suit in Card.suits:
        ##            for rank in Card.ranks:
        ##                self.cards.append(Card(suit, rank))
        for suit in range(4):
            for rank in range(13):
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        output = ""
        for card in self.cards:
            output += card.__str__() + "\n"

        return output


d = Deck()
print(d)

##c = Card()
##print(c)
