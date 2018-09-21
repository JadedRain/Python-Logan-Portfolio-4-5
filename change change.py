##Logan Douglas
##9/21/18
##Converting change to: Dimes, Quarters, Nickels, and Pennies

def change():
##  ##Step 1: Get input from user. Find out how much change
  total_change = int(input("What is the total value of change"))
##  ##Step 2: Calculate total for q n d p
  q = total_change//25
  whats_left = total_change%25
  d = total_change/10
  whats_left = whats_left%10
  n = whats_left/5
  whats_left = whats_left%5  
  p = whats_left
##  ##Step 3: Display it back to the user
  print("The amount of Change you have is:","\n",q,"quarters,","\n",d,"dimes,","\n",n,"nickels,","\n",p,"pennies")
##change()




def change2(total_change):
  ##Step 1: Get input from user. Find out how much change
  total_change = total_change
  ##Step 2: Calculate total for q n d p
  dol = total_change//100
  whats_left = total_change%100
  q = total_change//25
  whats_left = whats_left%25
  d = total_change//10
  whats_left = whats_left%10
  n = whats_left//5
  whats_left = whats_left%5
  p = whats_left
  return dol,q,d,n,p

total_change = 34
dol,q,d,n,p = change2(total_change)
##Step 3: Display it back to the user
print("$",dol,"The amount of Change you have is:","\n",q,"quarters,","\n",d,"dimes,","\n",n,"nickels,","\n",p,"pennies")
        









