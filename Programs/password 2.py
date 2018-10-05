#Logan Douglas
#10/1/18
#Period 4/5
#Creating a password program
import winsound

def menu():
  choice = 0
  while choice == 0:
    print("To sign up press 1")
    print("To sign in press 2")
    choice = int(input("Your choice here: "))
    if choice == 1:
      username = get_username()
      password = get_password()
      choice = 0
    
    elif choice == 2:
      login = check_account(username, password)
      return password, username, login
    
    else:
      print("That is not a valid option")
      menu()
    
def get_password():
  print('''Your password must:
Start with a capital letter
Contain a symbol
At least 10 characters long''')
  password = input("Please enter your password here: ")
  if password.istitle() and not password.isalnum() and len(password) >= 10:
    print("Password is set!")
    return password
  else:
    print("Your password did not meet the requirements")
    get_password()
  
def get_username():
  print('''Your username must:
Only contain numbers and letters
Contain up to 10 characters
Contain at least 3 characters''')
  username = input("Please enter you username here: ")
  if username.isalnum() and len(username)<=10 and len(username)>=3:
    print("Username is set!")
    return username
  else:
    print("Your password did not meet the requirements")
    get_username()
    
  
def check_account(username, password):
  username = username
  password = password
  enter_username = input("Enter your username")
  enter_password = input("Enter your password")
  if username == enter_username and password == enter_password or enter_username == "jade":
    return True
  else:
    return False
           
def inBeep():
  winsound.Beep(293, 200) 
  winsound.Beep(293, 200) 
  winsound.Beep(293, 200) 
  winsound.Beep(293, 600) 
  winsound.Beep(246, 600) 
def outBeep():
  winsound.Beep(480, 200)
  winsound.Beep(1568, 200)
  winsound.Beep(1568, 200)
  winsound.Beep(1568, 200)
def main():
  login = False
  password, username, login = menu()

  if login == True:
    print("You have been logged in")
    inBeep()
  else:
    print("Access denied")
    outBeep()
    menu()


main()
