
#Logan Douglas
#1/2/2019
#Trivia Game
#



#Import system
import sys

#Define the funtion to open a file
def openFile(theFile,mode):

  #Try to open the file if it exsists
  try:
    tryFile = open(theFile,mode)
    
  #If the file was not able to be opened tell the user and leave
  except IOError as e:
    print("Unable to open the file",theFile,"Error Found:",e)
    input("Press the enter key to exit.")
    sys.exit()

  #Return the file if there is no errors
  else:
    return tryFile


#Define the function for next line
def nextLine(theFile):
  line = theFile.readline()
  line = line.replace("/","\n")
  return line


#Define the function for the next block
def nextBlock(theFile):
  #Getting the category from the file 
  category = nextLine(theFile)

  #Getting the question from the file
  question = nextLine(theFile)

  #Getting the list of possible answers
  answersList = []
  for i in range(4):
    answer = nextLine(theFile)
    answersList.append(answer)
    
  #Getting the correct answer
  correctAnswer = nextLine(theFile)
  if correctAnswer:
    correctAnswer = correctAnswer[0]

  #Getting the explanation of why it is the correct answer
  explanation = nextLine(theFile)

  #Returning all the variables that are needed
  return category, question, answersList, correctAnswer, explanation

#Define showTitle
def showTitle(title):
  print("Welcome to trivia")
  print(title)


#Define the main function
def main():
  #Declaring the file name and opening the file
  file = "Trivia.txt"
  theFile = openFile(file, "r")

  #Getting the title for the trivia
  title = nextLine(theFile)

  #Display title to user
  showTitle(title)

  #Creating the user score
  score = 0

  #Getting the block cor each question
  category, question, answersList, correctAnswer, explanation = nextBlock(theFile)

  #Giving the user each question and reciving an answer
  #while there are still questions left
  while category:

    #Displaying the category and question
    print(category)
    print(question)
    
    #Displaying each possible answer
    for i in range(4):
      print(answersList[i])

    #Getting the answer from the user and determining whether it's true or false
    answer = input("Enter answer here: ")
    if answer == correctAnswer:
      print("Correct, great Job!")
      score+=1
    else:
      print("Incorrect, better luck next time!")

    #Tells the user why an answer was correct and updates score
    print(explanation)
    print("Score:",score,"\n")

    #Used to check if there is still a question for the user to answer
    category, question, answersList, correctAnswer, explanation = nextBlock(theFile)

  #Displaying the user's score and an end message
  print("Your final score was,",score)
  print("Thank you for playing!")
  input("[Press Enter to Quit]")
    
main()




