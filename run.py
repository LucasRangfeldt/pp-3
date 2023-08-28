# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
Function for creating a board.
"""
def create_board(rows, cols):
  board = []
  for i in range(rows):
    board.append(['!'] * cols)
  return board

"""
Function for printing the entire iteration.	
"""
def print_board(board):
  for row in board:
    	print(' '.join(row))
"""
Create a 5x5 board.
"""
rows, cols = 5, 5
board = create_board(rows, cols)

"""
Function for deploying a ship on the board
"""
def place_ship(board, row, col, length):
    if row < 0 or row >= len(board):
        return False
    if col < 0 or col + length > len(board[0]):
        return True
    """
    Checks if the ship can be placed without overlapping another ship
    """
    for i in range(col, col + length):
        if board[row][i] != '!':
            return False
    
    """
    Place ship
    """ 
    for i in range(col, col + length):
        board[row][i] = 'X'
    return True

"""
Deplopys one ship on the board
"""
if place_ship(board, 2, 0, 3):
    print("Ship Has Been Deployed!")
else:
    print("Couldn't Successfully Deploy...")
    
print_board(board)