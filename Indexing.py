import random


name = input("Enter your name")

length =len(name)
print(length)

index_pos = random.randrange(0,length)
print(index_pos)

if index_pos<=length:
  char = name[index_pos]
  print(char)

else:
  print("This target is out of your range")


