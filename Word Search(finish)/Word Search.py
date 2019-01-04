##Must present triva question about python user must guess
##Must answer qustion correctly
##Diplay word serch puzzle
##User must find and give index positions
##Check word to see if correct, if correct move on to next trivia
##Must keep track of attempts for word search and trivia
##Minimum of 10 words
##At leaset a 10 x 10 puzzle
##Comment code follow naming conventions
##Must use functions
##Add a point system

questionNum = 1
attempts = 0

def triviaQues():
  global questionNum
  global attempts
  print("Attempts:",attempts)
  
  if questionNum == 1:
    answerQ = input("What is a binary value representing \"True\" and \"False\"?\nAnswer:")
  elif questionNum == 2:
    answerQ = input("What code can be reused and is really good at doing one task?\nAnswer:")
  elif questionNum == 3:
    answerQ = input("This code will execute when an if/else statement returns false.\nAnswer:")
  elif questionNum == 4:
    answerQ = input("What is it when you are bringing in code?\nAnswer:")
  elif questionNum == 5:
    answerQ = input("A sequence of characters is also known as?\nAnswer:")
  elif questionNum == 6:
    answerQ = input("What kind of loop will go until something in the code breaks the loop?\nAnswer:")
  elif questionNum == 7:
    answerQ = input("This command will leave a while loop without needing to change the condition.\nAnswer")
  elif questionNum == 8:
    answerQ = input("what can be used to find a number or integer in a string?\nAnswer:")
  elif questionNum == 9:
    answerQ = input("This can be used to check if another condition is true if the first returns false.\nAnswer:")
  elif questionNum == 10:
    answerQ = input("")
  elif questionNum == 11:
    answerQ = input("")
  elif questionNum == 12:
    answerQ = input("")
  elif questionNum == 13:
    answerQ = input("")
  elif questionNum == 14:
    answerQ = input("")
  elif questionNum == 15:
    answerQ = input("")
  elif questionNum == 16:
    answerQ = input("")
  attempts += 1


while True:
  triviaQues()
    
