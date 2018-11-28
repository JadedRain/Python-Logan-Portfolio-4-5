##Logan Douglas
##Player Inventory
##11/18

import os
import random

def hud():
  print("Stats: ",player_stats)
  print("inventory: ",inventory)
  print("Equiped: ", equiped)
chest_items = ["gold","gems","bow","boots","funky hat"]
player_health = 100
player_armor = 1250
player_attack = 250
player_money = 0
inventory = ["Magic Staff","Mana Potion","Small healing potion","Old Cloak"]
max_inventory = 15
equiped = []
player_stats = ["health",player_health,"aromor",player_armor,"attack",
                player_attack,"money",player_money]

print("As you start out as an apprentice you have the following")
print("Player stats")
print(player_stats)
print()
print("Your items include:")
for item in inventory:
  print(item)
input("\n[Press enter to continue]")
os.system('cls')
hud()

input("\n[Press enter to continue]")

print("You have", len(inventory),"/",max_inventory,"Items in your possession.")
print("SO you can picek up",max_inventory-len(inventory),"more items")
input("\n[Press enter to continue]")
os.system('cls')
hud()

print("You tripped over a rock and took some damage")
player_stats[1] -= 24
input("\n[Press enter to continue]")

input("\nYou have taken some damage"+
      " your health is at "+str(player_stats[1])+"\n"+
      "you need to use your healing potion \n[Press enter to continue]")

if "Small healing potion" in inventory:
  print("You have used the healing potion.")
  player_stats[1]+=16
  inventory.remove("Small healing potion")
input("\n[Press enter continue]")
os.system('cls')
hud()


for i in range(len(inventory)):
  print(str(i),inventory[i])
print("Equip some armor!")
index = int(input("\nEnter the index number for an armor item in your inventory"))

while index > len(inventory)-1 or index < 0 and index != "":
  print("That number is our of range")
  index = int(input("\nEnter the index number for an armor item in your inventory"))
print("You equip your:",inventory[index])
equiped.append(inventory[index])
inventory.remove(inventory[index])

if "Old Cloak" in equiped:
  player_stats[3] += 500
input("\n[Press enter continue]")
os.system('cls')
hud()

chest = []

for i in range(random.randrange(len(chest_items))):
  item = random.choice(chest_items)
  chest.append(item)

print("You find a chest which contains:")
print(item)
print()
print("You add the contents of the chest to your inventory")

if len(inventory)+len(chest)<max_inventory:
  inventory += chest
else:
  drop = len(inventory)+len(chest) - max_inventory
  for i in range(drop):
    x = random.choice(chest)
    chest.remove(x)
  inventory += chest
input("\n[Press enter continue]")
os.system('cls')
hud()
print("Conver treasuer to gold")
if "gold" in inventory:
  player_stats[7]+=100
  inventory.remove("gold")
if "gems" in inventory:
  player_stats[7]+=1000
  inventory.remove("gems")
input("\n[Press enter continue]")
os.system('cls')
hud()

if player_stats[7] > 100:
  print("Your trade in your sword for a bow gaining 20 gold for the sword and buying the bow for 100")
  player_stats[7]+=20
  player_stats[7]-=100
  inventory[0] = "bow"
input("\n[Press enter continue]")
os.system('cls')
hud()

print("You trade in the last 2 items from your inventory")
inventory[len(inventory)-2:len(inventory)] = ["orb of mana"]
input("\n[Press enter continue]")
os.system('cls')
hud()

print("In a great battle you lost your cloak")
for i in range(len(inventory)):
  if inventory[i] == "Old Cloak":
    del inventoryp[i]
for i in range(len(equiped)):
  if equiped[i] == "Old Cloak":
    del equiped[i]
input("\n[Press enter continue]")
os.system('cls')
hud()

print("Your first 2 items were stolen by thieves")
del inventory[:2]
print("Your inventory now has:")
print(inventory)
input("\n[Press enter continue]")
os.system('cls')

                  
  






