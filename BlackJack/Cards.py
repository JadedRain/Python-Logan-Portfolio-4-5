#Logan Douglas
#Card game program(mostly blackjack)
#This program gives the idea for card games and uses what it has for blackjack

#Imports
import random

#Class
class Card(object):
    """A playing card.
    this class will build a single card
    to build a card call Card() and pass in a rand an a suit
    Example: card = Card(rank = "A", suit = "s"
    """

    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    SUITS = ["♣","♦","♥","♠"]

    def __init__(self,rank,suit,faceUp = True):
        self.rank = rank
        self.suit = suit
        self.isFaceUp = faceUp

    def __str__(self):
        if self.isFaceUp:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.isFaceUp = not self.isFaceUp\

class Hand(object):
    """A hand of playing cards.
    This class creates a hand to the player.
    to create a hand call Hand() and without passing anything in.
    Example: myHand = Hand()"""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card)+ " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card,otherHand):
        self.cards.remove(card)
        otherHand.add(card)

class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, perHand = 1):
        for rounds in range(perHand):
            for hand in hands:
                if self.cards:
                    topCard = self.cards[0]
                    self.give(topCard,hand)

if __name__ == "__main__":
    print("You ran this module directly(and did not 'import it).")
    input("[Press enter to exit]")