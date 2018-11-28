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
WORDS = ("Python",
         "Isdigit",
         "Function",
         "For loop",
         "While Loop",
         "String",
         "If",
         "Else",
         "Elif",
         "Variable",
         "Integer",
         "Boolean",
         "Import",
         "Input",
         "Global",
         "Isalpha",
         "Float",
         "Index",
         "List",
         "Tuple")
for i in range(len(HANGMAN)):
  print(HANGMAN[i])
  time.sleep(5)

