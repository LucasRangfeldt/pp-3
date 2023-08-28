# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""Function for creating a board
"""
def create_board(rows, cols):
  board = []
  for i in range(rows):
    board.append(['!'] * cols)
  return board

def print_board(board):
  for row in board:
    	print(' '.join(row))
    
rows, cols = 5, 5
board = create_board(rows, cols)

print_board(board)