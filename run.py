# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

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
def place_ship(board, row, col, length, orientation):
    if orientation == 'Horizontal':
        if row < 0 or row >= len(board) or col < 0 or col + length > len(board[0]):
            return False
        
        for i in range(col, col + length):
            if board[row][i] != '!':
                return False
            
        for i in range(col, col + length):
            board[row][i] = 'X'
            
    elif orientation == 'Vertical':
        if col < 0 or col >= len(board[0]) or row < 0 or row + length > len(board):
            return False
        for i in range(row, row + length):
            if board[i][col] != '!':
                return False
        for i in range(row, row + length):
            board[i][col] = 'X'
    else:
        return False
    return True

print_board(board)