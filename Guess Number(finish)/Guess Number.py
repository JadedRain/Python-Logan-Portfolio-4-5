##Logan Douglas and Zachary Page

import random



guesses = 0
maxi = 0

##Creating menu for users choices
def menu():
  
  global guesses
  global maxi
  guesses = 5
  maxi = 100

  ##While the menu is open display options and get their choice
  while True:
    print("Play\nOptions\nCredits\nQuit")
    menu_choice = input("Your choice here: ")

    ##If the user enters play run game
    if menu_choice.lower() == "play":
      break

    ##If the user enters options display options with their choices
    elif menu_choice.lower() == "options":
         print("Guesses\nMaximum value")
         user_choice = input("Enter choice here: ")

         ##If the user enters guesses as a choice tell them requirements
         ##and get their amount of guesses
         if user_choice.lower() == "guesses":
           option_guesses = input("How many guesses do you want?\nMust be\nGreater than 0\nLower than 16\n ")
           if option_guesses.isdigit():
             option_guesses = int(option_guesses)
             if option_guesses > 0 and option_guesses < 16:
                guesses = option_guesses
                print("These changes have been made")
           else:
             print("Did not meet requirements")


        
         ##If the user enters maximum value as a choice tell them requirements
         ##and get their maximum value
         elif user_choice.lower() == "maximum value":
            option_maxi = input("What do you want your maximum number range to be? \nMust be\nLess than 1000\n ")
            if option_maxi.isdigit():
              option_maxi = int(option_maxi)
              if option_maxi > 0 and option_maxi < 1000:
                maxi = option_maxi
                print("These changes have been made")
              else:
                print("Did not meet requirements")
                
            ##If the user didn't enter a valid option    
            else:
              print("Did not meet requirements")
      
    ##If the user enters credits display credits  
    elif menu_choice.lower() == "credits":
      print("Made by\nLogan Douglas\nZachary Page")

    ##If the user enters quit exit program  
    elif menu_choice.lower() == "quit":
      exit()

    ##Anything else results in the menu to rerun  
    else:
      continue

##While the game hasn't been quit run the menu and play game
while True:  
  menu()
  
  guesses_left = guesses
  number = random.randrange(1,maxi)

  ##While user still has guesses ask for their guess between the amount
  while guesses_left > 0:
    print("Please guess a number between 1 and",maxi)
    print(guesses_left,"guesses left")
    num_guess = input("Enter your number")

    ##Check if number is a digit and check what number it is
    if num_guess.isdigit():
      num_guess = int(num_guess)
      
      ##If the user got the correct answer tell them they were correct
      if num_guess == number:
        print("You got it! my number was",number)
        
      ##If the user entered a number above the maximum value tell them   
      elif num_guess > maxi:
        print("This guess was above the maximum or below the maximum")
        
      ##If the users guess was greater than the number tell them  
      elif num_guess > number:
        print("You need to guess lower than that")
        guesses_left-=1

      ##If the users guess was less than the number tell them  
      elif num_guess < number:
        print("You need to guess higher than that")
        guesses_left-=1

      ##If the users value isn't accepted tell them  
      else:
        print("Not an accepted value")
    ##If the user doesn't enter a number tell them    
    else:
      print("This is not an accepted value")
    ##if the user lost tell them  
  if guesses_left == 0:
    print("You have lost! Better luck next time")
   

