

def average(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):


  average_score = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
  average_score = average_score/10
  
  return average_score
  
num1 = float(input("Please enter a test score(#1)"))
num2 = float(input("Please enter a test score(#2)"))
num3 = float(input("Please enter a test score(#3)"))
num4 = float(input("Please enter a test score(#4)"))
num5 = float(input("Please enter a test score(#5)"))
num6 = float(input("Please enter a test score(#6)"))
num7 = float(input("Please enter a test score(#7)"))
num8 = float(input("Please enter a test score(#8)"))
num9 = float(input("Please enter a test score(#9)"))
num10 = float(input("Please enter a test score(#10)"))

score_average = (average(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10), "is your test score average")

print(score_average)



input()

