import random


class TwoPlayerJassStatus:
    """Class representing the game status of a two player Jass"""
    def __init__(self):
        self.cards = [[],[],[],[]]
        allCards = randomCardSet2()
        for i in len(allCards)//4:
            self.cards[0].append(allCards[i])
            self.cards[1].append(allCards[i+9])
            self.cards[2].append(allCards[i+18])
            self.cards[3].append(allCards[i+27])



# see : https://docs.python.org/3/library/random.html
def randomCardSet(max=36):
    for i in range(max):
        card = random.randrange(0, max)



def randomCardSet2(max=36):
    allCards = range(max)
    return random.sample(allCards, k=36)


print(randomCardSet2())
