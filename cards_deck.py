from random import*
from colorama import*

class cards:
    def __init__(self):
        self.deck = []

    def decks(self):

        cardfaces = [' A ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', '10 ', ' J ', ' Q ', ' K ']
        suits = [' Heart ', 'Diamond', " Spade ", " Club  "]
        x =0
        for i in suits:
            x+=1
            for j in cardfaces:
                if x <= 2:
                    self.deck.append([Fore.RED+j,Fore.RED+i])
                else:
                    self.deck.append([Fore.BLACK+j,Fore.BLACK+i])
        shuffle(self.deck)
        return self.deck
y= cards()
p = y.decks()
#Here p is the list of shuffled cards, dont try to print(p), just use print(p[0][1])
