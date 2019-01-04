import time


##word = input("Enter a word please")
##
##print("\nHere's each letter in your word:")
##for letter in word:
##  print(letter)
##  time.sleep(1)
##  
##message = input("Enter a message:")
##new_message =""
##VOWELS = "aeiouy"
##
##for letter in message:
##  if letter.lower() not in VOWELS:
##    new_message += letter
##    print("A new letter has been added:",new_message)
##    time.sleep(1)
##
##print("\nYour message without vowels is:",new_message)

print("Counting")
for i in range(15):
  print(i,end=" ")

print("\nCounting by 5's")
for i in range(0,50,5):
  print(i, end=" ")
print("\nCount backwards")
for i in range(10,0,-1):
  print(i, end=" ")
