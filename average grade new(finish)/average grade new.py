##Logan Douglas
##12/18
##Average Grades new

gradeList = []

def getGrade(gradeList):
  while True:
    maxGrade = 100
    grade = input("Please enter a grade(Enter 'x' to quit)")
    if grade == "x":
      break
    elif grade.isdigit():
      grade = float(grade)
      if grade <= maxGrade:
        gradeList.append(grade)
      else:
        q=input("Are you sure this "+str(grade)+" is a good grade(Y or N)")
        if q.upper() == "Y":
          gradeList.append(grade)
        else:
          print("*mistical deleting noises*")
      
    else:
      print("This was an invalid input.")


def avefunct(gradeList):
  total = sum(gradeList)
  
  average = total/len(gradeList)
  return average




def main(gradeList):
  getGrade(gradeList)
  ave = avefunct(gradeList)
  maxi = max(gradeList)
  mini = min(gradeList)
  print(maxi,mini)
  print("The average is: "+str(ave))

main(gradeList)

