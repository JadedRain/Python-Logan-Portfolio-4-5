#Value Error
#Type Error
#Indexing Error
#Io Error
#Key Error
#Name Error
#Syntax Error
#ZeroDivisionError

##num = None
##while num == None:
##  try:
##    num = float(input("Enter a number: "))
##  except:
##    print("ENTER A NUMBER YOU FOOL!")
##  try:
##    print(num)
##  except:
##    print("Nothin was able to print")
##
##
##
##try:
##  num = float(input("Enter a number"))
##except ValueError:
##  print("NOT A NUMBER YOU DUMB")
##except NameError:
##  print("Name Error was found")
##
##
##for value in (None, "Hi!"):
##  try:
##    print("Attempting to convert",value,"--> ",end="")
##    print(float(value))
##  except(TypeError):
##    print("There was an issue causing a type error")
##  except(ValueError):
##    print("There was an issue causing a value error")
##
##try:
##  num = float(input("Enter a number"))
##except ValueError as e:
##  print("That was not a number")
##  print("Code terms")
##  print(e) 

try:
  num = float(input("Enter a number"))
except ValueError:
  print("That was not a number")
else:
  print("You entered the legendary number!,",num)
