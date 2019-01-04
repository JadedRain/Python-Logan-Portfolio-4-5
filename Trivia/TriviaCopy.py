
#Logan Douglas
#1/2/2019
#Trivia Game
#



#Import system
import sys

#Define the funtion to open a file
def openFile(theFile,mode):
  try:
    tryFile = open(theFile,mode)
  except IOError as e:
    print("Unable to open the file",theFile,"Error Found:",e)
    input("Press the enter key to exit.")
    sys.exit()
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
  file = "r_file.txt"
  theFile = openFile(file, "r")

  title = nextLine(theFile)

  showTitle(title)

  score = 0

  category, question, answersList, correctAnswer, explanation = nextBlock(theFile)

  while category:
    print(category)
    print(question)

    for i in range(4):
      print(str(i)+ answersList[i])

    answer = input("Enter answer here: ")
    if answer == correct:
      print("Correct, great Job!")
      score+=1
    else:
      print("Incorrect, better luck next time!")

    print(explanation)
    print(score)

    category, question, answersList, correctAnswer, explanation = nextBlock(theFile)

    
main()




