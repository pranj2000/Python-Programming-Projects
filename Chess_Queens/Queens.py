#  File: Queens.py

#  Description: All queen positions without them attacking each other

#  Student Name: Pranjal Jain 

#  Student UT EID: pj5775

#  Partner's Name: Maurya Atluri

#  Partner's UT EID: ma57744

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 3/13/20

#  Date Last Modified: 3/13/20


num = 1
user = None
class Queens (object):
  # initialize the board
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  
  def print_board (self):
    global num
    num += 1

    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()

  # check if no queen captures another
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # do a recursive backtracking solution
  def recursive_solve (self, col):
    if (col == self.n):
      self.print_board()
      print()
      return True
    else:
      repeat = False
      for i in range (self.n):
        if (self.is_valid(i, col)):
          self.board[i][col] = 'Q'
          
          if (self.recursive_solve (col + 1)) :
            repeat = True
          self.board[i][col] = '*'
          
      return repeat

  # if the problem has a solution print the board
  def solve (self):
    for i in range (self.n):
      if (self.recursive_solve(i)):
        self.print_board()
    
def main():
  global user
  
  user = int(input('Enter the size of board: '))
  while user > 8 or user < 1:
    user = int(input('Enter the size of board: '))
  print()
  # create a regular chess board
  game = Queens (user)

  #place queens on board
  if (game.recursive_solve(0) == False):
    print('No possible solutions.')
    return
  return

  

main()
num = num-1
print('There are', num, 'solutions for a ' + str(user)+'x'+ str(user)+ ' board.')
