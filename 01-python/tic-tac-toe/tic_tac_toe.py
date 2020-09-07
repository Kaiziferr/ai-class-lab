import re
import random
_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    tab = self.board
    winn = None
    if tab[0] == tab[4] and tab[8] == tab[4] and tab[0] != None:
      if _PLAYER_SYMBOL in str(tab[0]):
        winn = _PLAYER
      else:
        winn = _MACHINE

    if tab[6] == tab[4] and tab[2] == tab[4] and tab[6] != None:
      if _PLAYER_SYMBOL in str(tab[6]):
        winn = _PLAYER
      else:
        winn = _MACHINE
    
    for i in range(len(tab)):
      n=0
      if i ==0 or i == 3 or i==6:
        n = 1
      if i >=0 and i<3:
        n = 3
      if n == 3 or n==1:
        if tab[i] == tab[i+n] and tab[(i+n)] == tab[(i+n)+n] and tab[i] != None:
          if _PLAYER_SYMBOL in str(tab[i]):
            winn = _PLAYER
          else:
            winn = _MACHINE
    self.winner = winn
    return self.board.count(None) == 0 or self.winner != None

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied
    while(1==1):
      n = random.randint(0, 8)
      print(n)
      if None is self.board[n]:
        self.board[n] = _MACHINE_SYMBOL
        break
    

  def format_board(self):
    # TODO: Implement this function, it must be able to print the board in the following format:
    #  x|o| 
    #   | | 
    #   | |
    tablero = ''
    j = 0 
    for i in self.board:
      if i is None:
        i = ' '
      if j == 1 or j == 4 or j == 7:
        i = f"|{i}|"
      
      if j == 2 or j == 5 or j == 8:
        i+= "\n"
       
      j+=1
      tablero += i
    print(self.board)
      
    return tablero

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner
    print(f"the winner is {self.winner}")