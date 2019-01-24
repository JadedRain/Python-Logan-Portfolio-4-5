import time
import datetime
import calendar

class Critter(object):
    #A virtual pet
    def __init__(self,name,hunger,boredom):
        self.name = name
        self.__hunger = hunger
        self.__boredom = boredom

    def __passTime(self):
        self.__hunger+=calendar.timegm(time.gmtime())/5
        self.__boredom+=1

    def play(self):
        print("You decide to play with",self.name+"!")
        self.__boredom-=2
        if self.__boredom<0:
            self.__boredom = 0
        self.__passTime()

    def talk(self):
        print(self.name,"is",self.mood)
        self.__passTime()

    def eat(self):
        print("You decide to feed",self.name+"!")
        self.__hunger-=2
        if self.__hunger<0:
            self.hunger=0
        self.__passTime()

    @property
    def mood(self):
        unhappiness = self.__hunger + self.__boredom
        if 5 > unhappiness:
           mood = "Happy"
        elif unhappiness <= 10:
            mood = "Okay"
        elif unhappiness <= 15:
            mood = "Frustrated"
        else:
            mood = "Mad"
        return mood

def main():
    name = input("Enter your critter's name!: ")
    crit = Critter(name,0,0)
    choice = None
    while choice != 0:
        print("""
        Talk:1
        Eat:2
        Play:3
        Quit:0
        """)
        choice = int(input("Choice: "))
        if choice == 0:
            print("GoodBye")
        elif choice == 1:
            crit.talk()
        elif choice == 2:
            crit.eat()
        elif choice == 3:
            crit.play()
        else:
            print("Not a valid option!")
main()