game_list = []
while True:
  option = int(input("""
  1: Add to game list
  2: Remove from game list
  3: Insert game into list
  4: Quit
  Enter Choice:"""))
  if option == 1:
    new_game = input("Enter the game you would like to add: ")
    game_list.append(new_game)
  elif option == 2:
    print(game_list)
    del_game = input("Which game would you like to remove: ")
    while True:
      if del_game
      in game_list:
        confirm = input("Would you like to remove this game?(y/n)")
        if confirm == "y":
          game_list.remove(del_game)
          break
        else:
          print("You chose to keep the game on your list.")
      else:
        print("The game",del_game,"was not found in your list")
  elif option == 3:
    print(game_list)
    ins_game = input("What game would you like to insert to your list: ")
    pos = int(input("What postion would you like to make this game? "))
    pos-=1

    while True:
      if pos < len(game_list):
        game_list.insert(pos,ins_game)
        break
      else:
        print("You can not insert a game into this position")

  elif option == 4:
    input("[Enter to quit]")
    break
  else:
    print("You can't do this")
  print(game_list)
