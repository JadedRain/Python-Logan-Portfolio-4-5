##Hangman Game
##Logan Douglas
##11/18
##The classic game Hangman. Choose a random word for player to guess


##Imports
import random
import time

##Constant
HANGMAN = ('''
-----
|   |
|   |
|    
|   
|
|
|
------''',
'''
-----
|   |
|   |
|   O
|   
|
|
|
------''',
'''
-----
|   |
|   |
|   O
|   #
|   #
|
|
------''',
'''
-----
|   |
|   |
|   O
|   #/
|   #
|
|
------''',
'''
-----
|   |
|   |
|   O
|  \#/
|   #
|
|
------''',
'''
-----
|   |
|   |
|   O
|  \#/
|   #
|  /
|
------''',
'''
-----
|   |
|   |
|   O
|  \#/
|   #
|  / \
|
------
GAME OVER!!!''')
MAX_WRONG = len(HANGMAN)-1
WORDS = ("PYTHON",
         "ISDIGIT",
         "FUNCTION",
         "FOR LOOP",
         "WHILE LOOP",
         "STRING",
         "IF",
         "ELSE",
         "ELIF",
         "VARIABlE",
         "INTEGER",
         "BOOLEAN",
         "IMPORT",
         "INPUT",
         "GLOBAL",
         "ISALPHA",
         "FLOAT",
         "INDEX",
         "LISY",
         "TUPLE")

word = random.choice(WORDS)##The wortd that will be guessed
so_far = "-"*len(word)## A dash for each letter
wrong = 0 ##Number of wrong guesses
used = [] ##Letters guessed

def title():
  print("Welcome one and all to HANGMAN...Good Luck!")
def showHangman():
  global MAX_WRONG
  global wrong
  global WORDS
  global word
  global so_far
  global used
  while wrong < MAX_WRONG and so_far != word:
    
    print(HANGMAN[wrong])
    print("You have used the letters:\n",used)
    print("\nSo far, the word is:",so_far)

    guess = input("\n\nEnter your guess")
    guess = guess.upper()

    while guess in used:
      print("You already used this letter",guess)
      guess = input("Enter your guess")
      guess = guess.upper()

    used.append(guess)


    if guess in word:
      print("The letter",guess,"is in the word")

      #Create a new so_far to include guess
      new = ""
      for i in range(len(word)):
        if guess == word[i]:
          new+= guess
        else:
          new+=so_far[i]
      so_far = new
    else:
      print("\nThe letter",guess,"is not in the word")
    wrong+=1
  
def winLose():
  if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("You've been hanged!")

  else:
    print("You got it right!")
  print("The word was",word)

  input("\n\n[Press enter to quit]")

def main():
  title()
  showHangman()
  winLose()
main()


