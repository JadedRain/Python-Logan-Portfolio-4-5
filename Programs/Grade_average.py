##Logan Douglas
##10/5/18
##Gets user input for 10 grades then gets the average an checks what it is equal to

grade1 = int(input("Please enter your grade"))
grade2 = int(input("Please enter your grade"))
grade3 = int(input("Please enter your grade"))
grade4 = int(input("Please enter your grade"))
grade5 = int(input("Please enter your grade"))
grade6 = int(input("Please enter your grade"))
grade7 = int(input("Please enter your grade"))
grade8 = int(input("Please enter your grade"))
grade9 = int(input("Please enter your grade"))
grade10 = int(input("Please enter your grade"))


sum_grades = grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7 + grade8 + grade9 + grade10
average = sum_grades/10

if average >= 90:
 grade = "Your grade is an A!"
elif average >= 80:
 grade = "Your grade is a B!"
elif average >= 70:
 grade = "Your grade is a C!"
elif average >= 60:
 grade = "Your grade is a D!"
elif average >= 50:
 grade = "Your grade is an F!"
else:
  grade = "You are failing!"

print("Your average is",average)
print(grade)
  
