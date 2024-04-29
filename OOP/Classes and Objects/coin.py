import random


class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def getSideup(self):
        return self.sideup


def main():
    # Create an object from the Coin class.
    coin = Coin()

    # Display the side of the coin that is facing up.
    print('This side is up: ', coin.getSideup())

    # Toss the coin
    print('I am tossing the coin.... ')
    coin.toss()

    # Display the side of the coin that is facing up.
    print('This side is up: ', coin.getSideup())


if __name__ == '__main__':
    main()
