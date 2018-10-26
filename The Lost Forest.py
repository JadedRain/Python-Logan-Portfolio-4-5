##Logan Douglas
##The Lost Forest Game
##10/20/18

import sys
import random
import time

player_inventory = ""
player_health = 50


def menu():
  print('''
      The Lost Forest

        **********
      **************
     **    Play    **
    ***   Credits  ***
   ****    Exit    ****
  **********************
''')
  choice = input("Your choice here: ")
  

  if choice.lower() == "play":
    return "play"
  elif choice.lower() == "credits":
    print('''
      -Credits-

  Programming: Logan Douglas
  Art: Emily Simoes
''')
    menu()
  elif choice.lower() == "exit":
    leave_game()
  else:
    print()
    print("Not a valid option")
    menu()
    
def leave_game():
  sys.exit()
  
def starting_area():
  
  global player_inventory
  print('''
             |     |   |    |    |   |    ||    | |  |     |         |  |   |   |  |           |    |      |     |       
             |     |   |    |    |   |    ||    | |  |     |         |  |   |   |  |           |    |      |     |       
             |     |   |    |    |   |    ||    | |  |     |         |  |   |   |  |           |    |      |     |       
             |     |   |    |    |   |    ||    |/    \    |         |  |   |   |  |           |    |      |     |       
             |     |   |    |    |   |    ||    |          |         |  |   |   |  |           |    |      |     |       
             |     |   |    |    |   |    ||    |          |         |  |   |   |  |           |    |      |     |       
             |     |   |    |    |   |    |      \         |         |  |   |   |  |           |    |      |  /\ |       
             |     |   |    |    |  /      \               |         |  |   |   |  |           |    |      | |  ||       
             |     |   |    |    |                         |         |  |   |   |  |           |    |      | |  ||       
             |     |   |    |    |                         |         | /     \  |  |           |    |      |  \/ |       
             |     |   |   /      \                       /           \         |  |           |    |      |     |       
             |    /     \                                ##########            /    \          |    |      |     |       
             |                                          ############                           |    |      |     |       
             |                                        ################                         |    |      |     |       
             |                                         ##############                         /      \     |     |       
             |                                         /############\                                      |     |       
             |                                       /  ************  \                                    |     |       
             |                                      |  **************  |                                  /       \      
             |                                      | **************** |                                                 
             |                                      |  **************  |                                                 
             |                                       \  ************  /                                                  
             |                                         \____________/                                                    
             |                                                                                                           
             |                                                                                                           
                                                                                                                         
                                                                                                          

''')
  print()
  print('''
You take a quick glance around you as you take in your surroundings.
You look at the trees that encloses the small area that you have. They are
taller than anything you have seen before. Their canopies hundreds of feet high off the ground.
A small fire the only source of heat that you have.
There is a small hole in one of the trees.
''')

  action = input("Enter action: ")
  action = action.lower()
  print()

  if action == "move":
    print("You see three pathways around through the forest.")
    print()
    print("The first path that you examine has dried blood along the ground in patches.")
    print("The second path that you examine has a small gold coin engraved with a paw print.")
    print("The third path that you examine has a light fog along the trail.")
    print()
    print("These are the only three ways out of this clearing.")
    pathway = input("Enter the path you choose. (This action cannot be undone): ")
    pathway = pathway.lower()
    
    if pathway == "path 1":
      answer = input("Are you sure? ")
      if answer.lower() == "yes":
        print('''
As you take your first few steps down the path, a wall of roots form behind you.
Your fate has been sealed.''')            
        print()
        print()
        time.sleep(5)
        hunter_pathway()
      elif answer.lower() == "no":
        print('''
A swarm of regret comes over you and you decide to take a few steps back
away from the path.''')
        starting_area()
      else:
        print("I have no choice but to interpret this as a no.")
        starting_area()


        
    elif pathway == "path 2":
      answer = input("Are you sure? ")
      if answer.lower() == "yes":
        print('''
As you take your first few steps down the path, a wall of roots form behind you.
Your fate has been sealed.''')
        print()
        print()
        player_inventory += " round coin"
        time.sleep(5)
        adventure_pathway()
      elif answer.lower() == "no":
        print('''
A swarm of regret comes over you and you decide to take a few steps back
away from the path.''')
        starting_area()
      else:
        print("I have no choice but to interpret this as a no.")
        starting_area()


        
    elif pathway == "path 3":
      answer = input("Are you sure? ")
      if answer.lower() == "yes":
        print('''
As you take your first few steps down the path, a wall of roots form behind you.
Your fate has been sealed.''')            
        print()
        print()
        time.sleep(5)
        magic_pathway()
      elif answer.lower() == "no":
        print('''
A swarm of regret comes over you and you decide to take a few steps back
away from the path.''')
        starting_area()
      else:
        print("I have no choice but to interpret this as a no.")
        starting_area()

    else:
      print("I didn't understand what you meant")
      starting_area()

    
  elif action == "smell":
    sub_action = input("What would you like to smell? ")

    if sub_action.lower() == "fire":
      print("The fire smells like charrd wood and burnt leaves.")
    elif sub_action.lower() == "air":
      print("The scent of some rotting meat and a lake breeze lingers in the air.")
    elif sub_action.lower() == "tree":
      print("The trees smell familiar, like something from home?")
    elif sub_action.lower() == "leaves":
      print("The leaves smell of sap.")
    else:
      print("You can't smell this")
    time.sleep(1)
    print()
    starting_area()


  elif action == "take":
  
    sub_action = input("What would you like to take? ")
    if sub_action.lower() == "bow" and "bow" not in player_inventory:
      player_inventory += " bow"
    elif sub_action.lower() == "campfire" and "campfire" not in player_inventory:
      player_inventory += " campfire"
    elif sub_action.lower() == "leaf" and "leaf" not in player_inventory:
      player_inventory += " leaf"
    elif sub_action.lower() == "quiver" and "quiver" not in player_inventory:
      player_inventory += " quiver"
    else:
      print("There is no resason to take", sub_action.lower()+".")
      starting_area()
      time.sleep(1)
      print()
    print(sub_action.title(), "has been added to your invenory")
    print()
    time.sleep(1)
    
    starting_area()

    
  elif action == "look":
    print('''
You take a closer look around the area.
You see that there is something inside the hole of the tree.
Nothing else seems out of the ordinary, other then three pathways
that you can make out from where you are.''')
    starting_area()



  elif action == "examine":
    sub_action = input("What would you like to examine")
    if sub_action.lower() == "hole":
      print('''
You look closer into the hole, there is a bow and quiver that lay inside.
It seems as if the hole was meant to hide or protect these items.''')
    elif sub_action.lower() == "bow":
      print('''
You look at the bow very closly. There seem to be carvings of leaves
and lines you have never seen before. It is made out of what seems like the root
of a tree. It looks older then time itself.''')
    elif sub_action.lower() == "quiver":
      print('''
You touch the quiver as you examine it. The material seems to be some kind of old leather.
The leather is worn out and fadded. The quiver still contains a bundle of arrows. still sharp to the touch.''')
    elif sub_action.lower() == "campfire":
      print('''
You come close to the fire and feel the heat radiate off of it. It seems out of place.
You try to touch the glowing orange light. There is heat, but no pain comes to follow.''')
    elif sub_action.lower() == "leaves":
      print('''
You look down at the leaves below you. They are many different colors.
Most of them have died years and years ago. Thought while searching through the crunching, dead leaves
you find one deep green. Almost an emerald green. It seems to be thriving though being long detached
from the tree that dropped it.''')
    else:
      print("You may not examine this item.")
      starting_area()
    print()
    time.sleep(1)
    starting_area()
  
  else:
    print("Not a valid entry")
    print()
    starting_area()
    

def hunter_pathway():
  global player_inventory
  print('''
  |    |   |    |   |  |  |   |  |   |   |     |      |   |   |    |  |  |  |   |   |    |    |     |  |   |   |   |  |    |    |  
  |    |   |    |   |  |  |   |  |   |   |     |      |   |   |    |  |  |  |   |   |    |    |     |  |   |   |   |  |    |    |  
  |    |   |    |   |  |  |   |  |   |   |     |      |   |   |    |  |  |  |   |   |    |    |     |  |   |   |   |  |    |    |
  |    |   |    |   |  |  |   |  |   |   |     |      |   |   |    |  | /    \  |   |    |    |     |  |   |   |   |  |    |    |
  |    |   |    |   |  |  |   |  |   |   |     |      |   |   |    |  |         |   |    |    |     |  |   |   |   |  |    |    |
  |    |   |    |   | /    \  |  |   |   |     |      |   |   |    |  |         |   |    |    |     |  |   |   |   |  |    |    |
   \   |   |    |   |        /    \  |   |     |      |   |   |    |  |         |   |    |    |    /    \  |   |   |  |    |    |
      /     \   |   |                |   |     |      |   |   |    |  |         |   |    |    |            |   |   |  |    |    |
                |   |                |   |     |      |  /     \   |  |         |   |    |    |            |   |  /    \   |    |
                |   |               /     \    |      |            |  |         |   |    |    |            |   |           |    |
               /      \                        |      |            |  |         |   |   /      \           |   |           |    |
                                               |      |            |  |         |   |                      |   |           |    |
                                               |      |            |  |         |   |                      |   |           |    |
                                               |      |           /    \        |   |                      |   |           |    |
                                               |      |                        /     \                     |   |           |    |
                                              /        \                                                  /     \          |    |
                                                                                                                          /      \
                                                                                                                          
                                                                                                                          __
                                                                                                                         |  |
                                                                                                                         |__|
                        __
                       |  |
                      /    \
                     (      )
                      ------                                                                                                           ''')
  print()
  print('''
You walk down the path knowing that there is no going back now.
You feel your heart pounding away in you chest. Thoughts pound in your head.
Something seems to be calling out in your head. You panic remembering the blood
at the start of the trail. After taking a deep breath you look around trying to stay calm.
You decide to stop for a break to take in your surroundings.''')
  print()
  action = input("Enter action: ")
  action = action.lower()
  print()
  if action == "move":
    print('''
You look at the pile of blood around you as a knot comes into your stomach.
A deep breath fills your lungs as you wonder what is to come.''')
    answer = input("Would you like to move on from this area?")
    if answer.lower() == "yes":
      print('''
A swarm of doubt hits you. You a worried of what's to come.
You continue on, scared with a confident front.''')
      print()
      print()
      time.sleep(3)
      bodies()
    elif answer.lower() == "no":
      print('''
You decide to take a final look around trying to forget
that you have to move on.''')
      print()
      print()
      time.sleep(1)
      hunter_pathway()
    else:
      print("I have no choice but to take this as a no.")
      print()
      print()
      time.sleep(1)
      hunter_pathway()
    

    
  elif action == "take":
    sub_action = input("What would you like to take? ")
    if sub_action.lower() == "potion" and "potion" not in player_inventory:
      player_inventory += " potion"
    elif sub_acition.lower() == "vile" and "vile" not in player_inventory:
      player_inventory += " vile"
    elif sub_action.lower() == "paper" and "paper" not in player_inventory:
      player_invnentory += " paper"
    else:
      print("You can't pick up this item.")
      print()
      print()
      time.sleep(1)
      hunter_pathway()
    print(sub_action.title(),"has been added to your inventory.")
    print()
    print()
    time.sleep(1)
    hunter_pathway()


    
  elif action == "look":
    print('''
  You look around the area. A small pool of blood, two red viles, and a piece of paper.
  The area has nothing too special about it as you take in the surroundings.''')


    
  elif action == "examine":
    sub_aciton = input("What would you like to examine? ")
    if sub_action.lower() == "paper" and "paper" in player_inventory:
      print('''
The paper has the words:
Only death lies ahead''')
    elif sub_action.lower() == "vile":
      print("It is a strange red vile, it seems to have no purpose.")
    elif sub_action.lower() == "potion":
      print("It is a strange potion full of a weird red liquid.")
    elif sub_action.lower() == "blood":
      print("The blood is recent maybe only a few hours before you arived.")
    else:
      print("You can't examine this item.")
    print()
    print()
    time.sleep(1)
    hunter_pathway()

    
  elif action == "smell":
    sub_action = input("What would you like to smell? ")
    if sub_action.lower() == "blood":
      print("It has almost no scent but the smal amount there is smells awful.")
    elif sub_action.lower() == "potion":
      print('''The potion smells like a light cherry scent, it reminds you of somehting.
You have no idea what the memory is before it fades to nothingness.''')
    elif sub_action.lower() == "vile":
      print("It has the same cherry smell as the potion.")
    elif sub_action.lower() == "paper":
      print("It smells of an old book.")
    else:
      print("You can't smell this.")
    print()
    print()
    time.sleep(1)
    hunter_pathway()
    
  else:
    print("This is not a valid action.")
    hunter_pathway()
  
def adventure_pathway():
  global player_inventory
  print('''
  |    |   |    |    |  |  |   |  |   |   |     |      |   |   |    |  |  |  |   |   |    |    |     |  |   |   |   |  |    |     |  
  |    |   |    |    |  |  |   |  |   |   |     |      |   |   |    |  |  |  |   |   |    |    |     |  |   |   |   |  |    |     |  
  |    |   |    |    |  |  |   |  |   |   |     |      |   |   |    |  |  |  |   |   |    |    |     |  |   |   |   |  |    |     |
  |    |   |    |    |  |  |   |  |   |   |     |      |   |   |    |  | /    \  |   |    |    |     |  |   |   |   |  |    |     |
  |    |   |    |    |  |  |   |  |   |   |     |      |   |   |    |  |         |   |    |    |     |  |   |   |   |  |    |     |
  |    |   |    |    | /    \  |  |   |   |     |      |   |   |    |  |         |   |    |    |     |  |   |   |   |  |    |     |
   \   |   |    |    |        /    \  |   |     |      |   |   |    |  |         |   |    |    |    /    \  |   |   |  |    |     |
      /     \   |    |                |   |     |      |   |   |    |  |         |   |    |    |            |   |   |  |    |     |
                |    |                |   |     |      |  /     \   |  |         |   |    |    |            |   |   |  |    | __  |
                |    |               /     \    |      |            |  |         |   |    |    |            |   |   |  |    ||  | |
               /      \                         |      |            |  |         |   |   /      \           |   |  /    \   ||__| |
                                                |      |            |  |         |   |                      |   |           |     |
                                                |      |            |  |         |   |                      |   |           |     |
                                                |      |            |  |         |   |                      |   |           |     |
                                                |      |           /    \        |   |                      |   |           |     |
                                                |      |                        /     \                     |   |           |     |
                                               /        \                                                  /     \          |     |
                                             /            \                                                                 |     |
                                                                                                                            |     |
                                                                                                                            |     |
                                                                                                                            |     |
                                                                                                                 *         /       \

                                                                                                                            o o
                                                                                                                           o   o
                                                                                                                             0   
          __
         |  |
        /    \
       (      )
        ------                  ''')
  print()
  print('''
You walk down the path while holding the coin between your fingers.
You aren't bothered with the thought of not returning to where you started.
Your mind is puzzled with why this coin was sitting on the ground and what it means.
Thoughts arise as you flip the coin in the air. You feel like it is time to take a rest from walking
for now.''')
  print()
  action = input("Enter action: ")
  action = action.lower()
  print()
  
  if action == "move":
    print('''
You flip the coin and catch it in the palm of your hand wondering if
you are ready to move on down the path. A deep sigh escapes you.''')
    answer = input("Would you like to move on from this area?")
    if answer.lower() == "yes":
      print("You look around and flip the coin as you know it's time to move on through your quest.")
      print()
      print()
      time.sleep(3)
      koda()
    elif answer.lower() == "no":
      print("A wave of regret comes over you as you decide to take another look around the area.")
      adventure_pathway()
    else:
      print("I have not choice but to take this as a no.")
      adventure_pathway()

      
  elif action == "take":
    sub_action = input("What would you like to take? ")
    if sub_action.lower() == "paper" and "paper" not in player_inventory:
      player_inventory += " paper"
    elif sub_aciton.lower() == "potion" and "potion" not in player_inventory:
      player_inventory += " health potion"
    elif sub_action.lower() == "square coin" and "square coin" not in player_inventory:
      player_inventory += " square coin"
    else:
      print("You can't take this item.")
      print()
      print()
      time.sleep(1)
      adventure_pathway()
    print(sub_action.title(),"has been added to your inventory.")
    print()
    print()
    time.sleep(1)
    adventure_pathway()
      
  elif action == "look":
    print('''
You look around you trying to calm down your mind. You notice a small red potion of some sort.
A glimpse of light shining off of something behind a tree trunk.
There looks to be old paw prints in the path dirt.''')
    print()
    print()
    time.sleep(5)
    adventure_pathway()



    
  elif action == "examine":
    sub_action = input("What would you like to examine? ")
    if sub_action.lower() == "paper" and "paper" in player_inventory:
      print('''
This strange piece of paper has the words:
"Wealth"
"Death"
"One may lead to the other. Greed may lead you to both."
"Compasion may be what you find along the way."
"Through those who enter the lost forest all have taken the oath."
"None have left with a word to say." ''')
    elif sub_action.lower() == "potion":
      print('''
A beaker full of a strange red liquid, you have never seen
anything like it before. The beaker is cold to the touch.''')
    elif sub_action.lower() == "tracks":
      print("The tracks match that of a wolf. A few drops of blood stain the dirt.")
    elif sub_action.lower() == "trunk":
      print('''A piece of old paper lays on top of the once mighy tree. A few words are written on the front.
The tree looks to have been hundereds of years old. A square coin was the source of the glimer found behind the trunk.''')
    elif sub_action.lower() == "square coin":
      print("A small coin tile with the word \"Hope\" engraved on the back. The coin feels heavier then the first you grabbed")
    else:
      print("You can't examine this.")
    print()
    print()
    time.sleep(1)
    adventure_pathway()



    
  elif action == "smell":
    sub_action = input("What would you like to smell? ")
    if sub_action.lower() == "square coin":
      print("A copper and gold metallic stench is emitted from the coin.")
    elif sub_actoin.lower() == "paper":
      print("The aroma of an old book comes from the piece of dusty paper.")
    elif sub_action.lower() == "potion":
      print('''The potion smells like a light cherry scent, it reminds you of somehting.
You have no idea what the memory is before it fades to nothingness.''')
    elif sub_action.lower() == "air":
      print("The air holds the smell of a lake breeze. It makes you wonder about your old life.")
    elif sub_action.lower() == "trunk":
      print("The trunk of this tree has no smell.")
    elif sub_action.lower() == "tracks":
      print("The tracks smell like wet dog.")
    else:
      print("You can't smell this.")
    print()
    print()
    time.sleep(1)
    adventure_pathway()
    
  else:
    print("This is not a valid action.")
    print()
    print()
    adventure_pathway()
    

def magic_pathway():
  global player_inventory
  print('''
  |    |   |    |    |  |  |   |  |   |   |     |      |   |   |    |  |  |  |   |   |    |    |     |  |   |   |   |  |    |    |  
  |    |   |    |    |  |  |   |  |   |   |     |      |   |   |    |  |  |  |   |   |    |    |     |  |   |   |   |  |    |    |  
  |    |   |    |    |  |  |   |  |   |   |     |      |   |   |    |  |  |  |   |   |    |    |     |  |   |   |   |  |    |    |
  |    |   |    |    |  |  |   |  |   |   |     |      |   |   |    |  | /    \  |   |    |    |     |  |   |   |   |  |    |    |
  |    |   |    |    |  |  |   |  |   |   |     |      |   |   |    |  |         |   |    |    |     |  |   |   |   |  |    |    |
  |    |   |    |    | /    \  |  |   |   |     |      |   |   |    |  |         |   |    |    |     |  |   |   |   |  |    |    |
   \   |   |    |    |        /    \  |   |     |      |   |   |    |  |         |   |    |    |    /    \  |   |   |  |    |    |
      /     \   |    |                |   |     |      |   |   |    |  |         |   |    |    |            |   |   |  |    |    |
                |    |                |   |     |      |  /     \   |  |         |   |    |    |            |   |  /    \   |    |
                |    |               /     \    |      |            |  |         |   |    |    |            |   |           |    |
               /      \                         |      |            |  |         |   |   /      \           |   |           |    |
                                                |      |            |  |         |   |                      |   |           |    |
                                                |      |            |  |         |   |                      |   |           |    |
                                                |      |            |  |         |   |                      |   |           |    |
                                                |      |           /    \        |   |                      |   |           |    |
                                                |      |                        /     \                     |   |           |    |
                                               /        \                                                  /     \          |    |
                                             /            \                                                                /      \


                                                                                      \
                                                                                       \
                                                                                        \ 
                        __
                       |  |
                      /    \
                     (      )
                      ------   ''')
  print()
  print('''
You walk done the path slowly, being aware of the fog. It seems more then just
a fog. You have the sense that you are not alone in this area.
The fog grows colder. You start to feel light headed and decide to take a break from your journey
into the mist.''')
  print()
  action = input("Enter action: ")
  action = action.lower()
  print()
  if action == "move":
    print("You take a look around and start to think if you should move on yet.")
    answer = input("Would you like to move on from this area?")
    if answer.lower() == "yes":
      print("You feel confident and decide to continue into the mist.")
      print()
      print()
      time.sleep(3)
      
    elif answer.lower() == "no":
      print("You decide to take one last look around before you continue your journey.")
      print()
      print()
      time.sleep(1)
      magic_pathway()
    else:
      print("I have no choice but to take this as a no.")
      magic_pathway()
	
  elif action == "take":
    sub_action = input("What would you like to take? ")
    if sub_action.lower() == "potion" and "healh potion" not in player_inventory:
      player_inventory += " health Potion"
    elif sub_action.lower() == "stick" and "stick" not in player_inventory: 
      player_inventory += " stick"
    elif sub_action.lower() == " empty bottle" and "empty bottle" not in player_inventory:
      player_inventory += " empty bottle"
    else:
      print("There is no reason to take",sub_action.lower()+".")
      print()
      time.sleep(1)
      magic_pathway()
    print(sub_action.title(),"has been added to your invnentory.")
    print()
    time.sleep(1)
    magic_pathway()

    
  elif action == "look":
    print('''
You take a look around the area. It seems realitively bland.
You noticed some items scatered along the ground. There is a strange red potion.
A stick unlike any you have seen before. ''')
    magic_pathway()
    
  elif action == "examine":
    sub_action = input("What would you like to examine? ")
    if sub_action.lower() == "stick":
      print('''
You look at the stick closely, nothing seems off about it
though it seems something not from nature.''')
    elif sub_action.lower() == "potion":
      print('''
A beaker full of a strange red liquid, you have never seen
anything like it before. The beaker is cold to the touch.''')
    elif sub_action.lower() == "empty bottle":
      print('''
Nothing special, just an empty bottle.''')
    else:
      print("You may not examine this item.")
    time.sleep(1)
    magic_pathway()
    
  elif action == "smell":
    sub_action = input("What would you like to smell? ")
    if sub_action.lower() == "air":
      print('''
The air smells...odd. You can't pin point what it reminds you of though.
You try to grasp the thought to no avail.''')
    elif sub_action.lower() == "potion":
      print('''
The potion smells like a light cherry scent, it reminds you of somehting.
You have no idea what the memory is before it fades to nothingness.''')
    elif sub_action.lower() == "stick":
      if "leaf" in player_inventory:
        print('''
The stick smells very similar to the leaf you found earlier.
You wonder if they have a corelation.''')
      else:
        print('''
The stick smells like nothing you have ever smelt before.''')
    elif sub_action.lower() == "ground":
      print('''
The ground smells like the air after a long rainstorm. The aroma
seems to only linger lightly above the ground''')
    elif sub_action.lower() == "senf":
      print("Senf Senf, I smell food!")
    else:
      print("You can't smell this.")
    time.sleep(1)
    magic_pathway()
  else:
    print("This is not a valid action.")
    magic_pathway()






menu()
print('''
You awaken in a clearing in the middle of a forest. You remember nothing
other than your name. As you start to become more conscious of it. You whisper
"Jade....Jade...Jade" more often to keep this knowledge in your mind. After all,
it is all you can remember.
''')

print()
print()
time.sleep(8)
starting_area()
    

  
