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
