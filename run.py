# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

# Function for creating a board
def create_board(rows, cols):
    return [['!' for _ in range(cols)] for _ in range(rows)]


# Function for printing the board
def print_board(board):
    for row in board:
    	print(' '.join(row))

# Function for randomly generating ships on the board
def place_random_ships(board, num_ships, target):
    placed_ships = 0
    while placed_ships < num_ships:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        if board[row][col] == '!':
            board[row][col] = target
            placed_ships += 1
            
