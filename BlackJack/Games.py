import Cards
def askNum(question,low,high):
    """Ask for a number
    this function will take in a question
    for the user to choose a number between a low
    and high range in order to use it you must give it a question, a low number
    and a high number
    Example: askNum("Choose a number(1-10)
    """
    while True:
        num = input(question)
        try:
            num = int(num)
        except:
            print("Can't convert to integer.")
        if num in range(int(low),int(high)):
            return num
        else:
            print("This value is out of range.")


def switchTurn(numPlayers,turn):
    """Switch the turns between players
    this funciton will swap turns between players
    to use this you will need to give it the amount of players and a number value for
    the turn
    Example: switchTurn(2,0) #2 is the number of players and 0 is the turn
    """
    turn = turn
    if turn < numPlayers-1:
        turn+=1
    else:
        turn = 0
    return turn


def yesOrNo(question):
    """Asking the user a yes or no question
    this fucntion will take a question and ask the user for a yes or no
    response. To use you will need to give the question to be asked
    Example: yesOrNo("Does 2+2 = 4?")
    """
    response = None
    while response not in("y","n"):
        response = input(question).lower()
    return response


def winLose(winner):
    """This code will say who wins
    This code will get the winner by taking in the player
    to use this you will need to give it the player to determine who wins
    Example: winLose("player 1")
    """
    print(winner,"wins!")

    input("\n\n[Press enter to quit]")


def openFile(theFile, mode):
    """Opening a file
    This function tries to open a file depending on the mode and name
    It will allow the user to open a file of their choosing
    They will need to enter a file name and the mode
    Example: """
    try:
        tryFile = open(theFile, mode)

    except IOError as e:
        print("Unable to open the file", theFile, "Error Found:", e)
        input("Press the enter key to exit.")
        sys.exit()

    else:
        return tryFile

class Player(object):
    """A player for a game"""
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name
        rep = rep + " " + str(self.score)
        return rep

if __name__ == "__main__":
    print("You ran this module directly(and did not import it).")
    input("\n[Press enter to exit]")