#Logan Douglas
#9/13


import math

#Get a users name
def get_name(name):
  input_name = name
  input_name = input_name.lower()
  input_name = input_name.title()

#Step 2: Display the name back to the user.
  print("Your name is currently", input_name)
#Step 3: Verify that the name was correct.
  input("Is this your name? Yes or No")
name = input("What is your name?")
get_name(name)


def pythagoras_theorem(ap = 1,bp = 1):
  a = float(ap)
  b = float(bp)
  c = a*a+b*b
  c = math.sqrt(c)

  print("The third side is", c)



##pythagoras_theorem(ai,bi)




def add_numbers(x,y):
  num1 = x
  print("num1 = x ",num1)
  num2 = y
  print("num2 = y",num2)
  num3 = int(num1) + int(num2)
  return num3

x = 1
y = 10
##num4 = add_numbers(x,y)
##print(num4)
  
