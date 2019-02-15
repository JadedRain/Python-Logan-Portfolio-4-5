#Logan Douglas
#2/15/19
#Black Jack
#Compete from 1-7 players against a dealer

#Imports
################################
import Cards, Games

#Classes
################################
class BJ_Card(Cards.Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.isFaceUp:
            v = BJ_Card.RANKS.index(self.rank)+1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(Cards.Deck):
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank,suit))

class BJ_Hand(Cards.Hand):
    def __init__(self,name):
        super(BJ_Hand,self).__init__()
        self.name = name
    def __str__(self):
        rep = self.name+":\t"+ super(BJ_Hand,self).__str__()
        if self.total:
            rep += "("+str(self.total)+")"
        return rep

    @property
    def total(self):
        #If a card in the hand has a value of None, the total is None
        for card in self.cards:
            if not card.value:
                return None
        #Add up card values, treat each ace as 1
        t = 0
        for card in self.cards:
            t += card.value
        #determine if hand contains an Ace
        containsAce = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                    ontainsAce = True
        #If hand contians Ace and total is low enought treat ace as 11
        if containsAce and t <= 11:
            t += 10
        return t
    def isBusted(self):
        return self.total>21

class BJ_Player(BJ_Hand):
    """A BlackJack Player"""
    def isHitting(self):
        response = Games.yesOrNo("\n"+self.name+" ,do you want a hit(Y/N):")
        return response == "y"
    def bust(self):
        print(self.name,"busts")
    def lose(self):
        print(self.name,"is a loser")
    def win(self):
        print(self.name,"is a winner")
    def push(self):
        print(self.name,"pushes")

class BJ_Dealer(BJ_Hand):
    """A BlackJack dealer"""
    def isHitting(self):
        return self.total< 17 #Extra credit hard 17 (10) soft 17 (no 10)

    def bust(self):
        print(self.name, "busts")

    def flipFirstCard(self):
        firstCard = self.cards[0]
        firstCard.flip()

class BJ_Game(object):
    """A BlackJack game"""
    def __init__(self,names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer: Thompson")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def stillPlaying(self):
        sp = []
        for player in self.players:
            if not player.isBusted():
                sp.append(player)
        return sp

    def __additionalCards(self,player):
        while not player.isBusted() and player.isHitting():
            self.deck.deal([player])
            print(player)
            if player.isBusted():
                player.bust()

    def play(self):
        #Deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer],perHand = 2)
        self.dealer.flipFirstCard() #Hide dealers first card
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__additionalCards(player)

        self.dealer.flipFirstCard() #Reveal dealer's first

        if not self.stillPlaying:
            #since all players have busted, just show dealers hand
            print(self.dealer)
        else:
            #Deal more cards to dealer
            print(self.dealer)
            self.__additionalCards(self.dealer)

            if self.dealer.isBusted():
                #Everyone still playing wins
                for player in self.stillPlaying:
                    player.win()

            else:
                #Compare each player still playing to dealer
                for player in self.stillPlaying:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        #Remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()


#Main
##################################
def main():
    print("Welcome to BlackJack!\n")
    names = []
    number = Games.askNum("How many players? (1-7):",low = "1",high = "8")
    for i in range(number):
        name = input("Enter your name: ")
        names.append(name)

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = Games.yesOrNo("Do you want to play again(Y/N)")

main()
input("[Enter to quit]")
