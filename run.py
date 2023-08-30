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

"""

"""
def randomly_place_ships(board, num_ships, length):
    for _ in range(num_ships):
        placed = False
        while not placed:
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - 1)
            orientation = random.choice(['Horizontal', 'Vertical'])
            placed = place_ship(board, row, col, length, orientation)       
             

"""
Deplopys one ship on the board
"""
if place_ship(board, 2, 0, 3):
    print("Ship Has Been Deployed!")
else:
    print("Couldn't Successfully Deploy...")
"""
Function for hit or miss.
"""
def guess(board, row, col):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return "Nice try, but that's not the ocean."
    if board[row][col] == 'X':
        board[row][col] = 'H'
        return "Hit!"
    else:
        if board[row][col] != 'H' and board[row][col] != 'M':
            board[row][col] = 'M'
        return "Miss..."
    

def destroyed_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column=='X':
                count+=1
    return count



print_board(board)