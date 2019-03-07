#Logan Douglas
#Fight Save repeat
#3/19

#Imports
import random
from tkinter import *
import pickle


#Variables
CHARLIST = []
NAMELIST = ["Jade","Emily","Logan","Joel","Jack","Mark","Steve","Jordan","Oliver","Ellie","Nea","Greg",Tom]

#Classes
class Character(object):

    def __init__(self,name,health,minDam,maxDam):
        self.name = name
        self.health = health
        self.minDam = minDam
        self.maxDam = maxDam



    def getHit(self,minDam,maxDam):
        pass

class Menu(Frame):

    def __init__(self, master):
        """Initialze the Frame."""
        super(Menu, self).__init__(master)
        self.grid()
        self.createWidgets()

#Methods

    def createWidgets(self):
        #Creating buttons
        self.createBttn = Button(self)
        self.fightBttn = Button(self)
        self.addBttn = Button(self)
        self.chooseBttn = Button(self)
        self.saveBttn = Button(self)
        self.loadBttn = Button(self)
        self.clearBttn = Button(self)

        self.createBttn.grid(row = 0, column = 0, sticky = NS)
        self.fightBttn.grid(row = 1, column = 0, sticky = NS)
        self.addBttn.grid(row = 2, column = 0, sticky = NS)
        self.chooseBttn.grid(row = 3, column = 0, sticky = NS)
        self.saveBttn.grid(row = 4, column = 0, sticky = NS)
        self.loadBttn.grid(row = 5, column = 0, sticky = NS)
        self.clearBttn.grid(row = 6, column = 0, sticky = NS)

        #Button text
        self.createBttn["text"] = "Create Character"
        self.fightBttn["text"] = "Fight an enemy"
        self.addBttn["text"] = "Add preset to list"
        self.chooseBttn["text"] = "Choose a saved character"
        self.saveBttn["text"] = "Save Preset"
        self.loadBttn["text"] = "Load Preset"
        self.clearBttn["text"] = "Clear Preset"

        #Button Commands
        self.createBttn["command"] = self.savePresets
        self.fightBttn["command"] = self.savePresets
        self.addBttn["command"] = self.savePresets
        self.chooseBttn["command"] = self.savePresets
        self.saveBttn["command"] = self.savePresets
        self.loadBttn["command"] = self.loadPresets
        self.clearBttn["command"] = self.clearPresets

        #Creating TextBox
        self.infoTxt = Text(self, width = 24, height = 8, wrap = WORD, state = DISABLED)

        self.infoTxt.grid(row = 8, column = 0, sticky = NS)

    #Changing the message in the text box
    def infoText(self,message):
        self.infoTxt.configure(state=NORMAL)
        self.infoTxt.delete(0.0, END)
        self.infoTxt.insert(0.0, message)
        self.infoTxt.configure(state=DISABLED)

    #Create the current character for the player
    def createChar(self):
        root = Tk()
        root.title("Create your character")
        root.geometry("250x350")

        #Create the labels

        #Create the entry

        #Create submit button

        #Create random char button

    def fightEnemy(self):
        pass

    def addChar(self):
        pass

    def chooseChar(self):
        pass


    #Save the current presets in the list of characters
    def savePresets(self):
        try:
            savefile = open("PlayerSave.txt", "w")

            pickler = pickle.Pickler(savefile)
            pickler.dump(CHARLIST)

            savefile.close()


        except:
            self.infoText("There was an error while saving the file.")

        self.infoText("Save Successful!")

    #Load the presets form the save file to the list of characters
    def loadPresets(self):
        try:
            savefile = open("PlayerSave.txt", "r")

            unpickler = pickle.Unpickler(savefile)
            CHARLIST = unpickler.load()

            savefile.close()

        except:
            self.infoText("There was an error while loading the file.")

            self.infoText("Load Successful!")

    #Clear all presets from the list of characters
    def clearPresets(self):
        CHARLIST = []
        self.infoText("Clear Successful! If you want to keep this change save and exit the program.")


#Functions





#Main
root = Tk()
root.title("Fight Save Repeat")
root.geometry("195x275")

app = Menu(root)

root.mainloop()
