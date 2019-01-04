##Logan Douglas
##12/18
##Tic Tac Toe

##The classic game of tic tac toe that we all know and love


##Global constants
X = "X"
O = "O"
EMPTY = ""
TIE = "TIE"
NUM_SQUARES = 9


##Funcitons

#Insttucitons Function
def displayInstructions():
  print("Welcome Player to X-treme Tic Tac Toe!")

  print("""
Instructions:
The goal of the game is to get three x's or o's in a row to win.
If neither you or the computer get three in a row then the game ties.
Block off your computer enemy to keep them from getting three in a row.

  For example:



            X |   |
           ---|---|---
            X |   |
           ---|---|---
            O |   |

  You will enter your x or o at a number(0-8) based on the following  postions.


            0 | 1 | 2
           ---|---|---
            3 | 4 | 5
           ---|---|---
            6 | 7 | 8

(If you were o's then the goal would be to block off your computer enemy)


You better be ready!
""")

  print("Computer: GG EZ, give me someone worth going against!\nWhy do I have to be against this scrub\n")

############################################################################
def yesOrNo(question):
  response = None
  while response not in("y","n"):
    response = input(question).lower()
  return response
    
############################################################################
def askNumber(question,low,high):
  response = "9999"
  while True:
    if response.isdigit():
      if int(response) in range(low,high+1):
        break
      else:
         response = input(question)
    else:
      print("Must be a number")
      response = input(question)
  return int(response)
############################################################################
def pieces():
    goFirst = yesOrNo("Whould you like to go first? (y/n): ")
    if goFirst == "y":
      print("Wow the human needs to go first in order to beat me? How pathetic.")
      human = X
      ai = O
    else:
      print("Ha I go first? I wanted it to be a challenge not child's play.")
      human = O
      ai = X
    return human, ai
############################################################################
def newBoard():
  board = []
  for square in range(NUM_SQUARES):
    board.append(EMPTY)
  return board

############################################################################
def displayBoard(board):
  print(" ",board[0],"|",board[1],"|",board[2])
  print("---|---|---")
  print(" ",board[3],"|",board[4]," |",board[5])
  print("---|---|---")
  print(" ",board[6],"|",board[7]," |",board[8])
############################################################################
def legalMoves(board):
  moves = []
  for square in range(NUM_SQUARES):
    if board[square] == EMPTY:
      moves.append(square)
  return moves
############################################################################
def winner(board,human,ai):
  WAYS_TO_WIN = ((0,1,2),
                 (3,4,5),
                 (6,7,8),
                 (0,3,6),
                 (1,4,7),
                 (2,5,8),
                 (0,4,8),
                 (2,4,6))
  for row in WAYS_TO_WIN:
    if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
      winner = board[row[0]]
      return winner
    
    if EMPTY not in board:
      return TIE

    return None
############################################################################
def humanMove(board):
  moves = legalMoves(board)
  manMove = None
  while manMove not in moves:
    manMove = askNumber("Enter the number for your move(0-8).",0,NUM_SQUARES)
    if manMove not in moves:
      print("\nReally human, you are so bad. I'll let you go again for that dumb mistake.")
  print("Took you long enough.")
  return manMove
############################################################################
def nextTurn(turn):
  if turn == X:
    return O
  else:
    return X
############################################################################
def congratWinner(the_winner,human,ai):
  if winner != TIE:
    print("The winner is",winner+"'s")
  else:
    print("This game was tied")
  if winner == human:
    print("Uhg I guess you have won. THIS GAME WAS RIIIIGED")
  elif winner == ai:
    print("Ha you are a loser. LOSER. L.O.S.E.R.")
  elif winner == TIE:
    print("Ha it was a tie. I dare you to try again.")
############################################################################
def aiMove(board,ai,human):
  #Create copy of board 
  board = board[:]

  #GEt the best positions to have
  BEST_MOVES = (4,1,3,5,7,0,2,6,8)
  print("I shall take the number ",end="")
  #If the computer can win take that move
  for move in legalMoves(board):  
    board[move] = ai
    if winner(board,human,ai) == ai:
      print(move)
      return move
    
    #Done checking this move, undo it
    board[move] = EMPTY

  #If the human can win take that move
  for move in legalMoves(board):
    board[move] = human
    if winner(board,human,ai) == human:
      print(move)
      return move
  
    #Done checking this move, undo it
    board[move] = EMPTY

  #Since nobody can win on next move pick next best option.
  for move in BEST_MOVES:
    if move in legalMoves(board):
      print(move)
      return move
############################################################################
def main():
  displayInstructions()
  human,ai = pieces()
  turn = X
  board = newBoard()
  displayBoard(board)
  while not winner(board,human,ai):
    if turn == human:
      move = humanMove(board)
      board[move] = human
    else:
      move = aiMove(board,ai,human)
      board[move] = ai

    displayBoard(board)
    turn = nextTurn(turn)
  the_winner = winner(board,human,ai)
  congratWinner(the_winner,human,ai)


main()
