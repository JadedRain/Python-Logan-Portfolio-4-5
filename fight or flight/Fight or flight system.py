##Logan Doulgas
##12/10/18
##4-5

import random

win = 0
player_health = 100
troll_health = 100000


print("You are screwed")
choice = input("Fight or Flight")
choice = choice.lower()

while choice == "fight":
  player_damage = random.randrange(0,31)
  print("You attack the king troll and did", player_damage,"damage")
  troll_health -= player_damage
  if troll_health > 0:
    troll_damage = random.randrange(0, 150)
    print("The king troll is fighting back dealing", troll_damage,"damage")
    player_health -= troll_damage
  if player_health <= 0:
    print("You have died in battle.")
    win = 0
    break
  elif troll_health <= 0:
    print("YOU HAVE ERADICATED THE TROLL KING")
    win = 1
    break
  elif player_health >= 0 and troll_health >= 0:
    print("You have", player_health,"health")
    print("The king troll has",troll_health,"health")
    choice = input("fight or flight")
    choice = choice.lower()
    if choice == "fight":
      print("You have kept up your efforts!")
    elif choice == "flight":
      break
if choice == "flight":
  print("You have fled from the troll king!")
if win == 0:
  print("Wow you suck")
else:
  print("YOU WIN")
