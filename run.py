# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# This code is written by Lucas Rangfeldt
# Big thanks to ChatGPT for examples and ideas
# Also big thanks to Mike for helping me troubleshoot.
import random

# Function for creating a board
def create_board(rows, cols):
    return [['~' for _ in range(cols)] for _ in range(rows)]


# Function for printing the board

def print_board(board):
    
    # Prints labels
    print("  ", end="")
    for i in range(len(board[0])):
        print(chr(65 + i), end="  ")
    print()
    for i, row in enumerate(board):
        print(i, end=" ")

        # Prints the board row and only shows the visible ships
        for cell in row:
            if cell == 'S' or cell == 'Hit' or cell == 'Miss':
                print(cell, end="  ")
            else:
                print('~', end="  ")
        print()
            
    
# Function for randomly generating ships on the board

def place_random_ships(board, num_ships, target):
    placed_ships = 0
    while placed_ships < num_ships:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        if board[row][col] == '~':
            board[row][col] = target
            placed_ships += 1
            
# Function for guessing a position
def guess(board, row, col, target):
    if board[row][col] == target:
        board[row][col] = 'Hit' 
        return True
    else:
        board[row][col] = 'Miss'
        return False
    
# main code for board
rows, cols = 5, 5
board = create_board(rows, cols)

# Places five visible and five invisible ships S for visible and X for invis.
place_random_ships(board, 5, 'S')
place_random_ships(board, 5, 'X')

print('Your board:')
print_board(board)

player_ships_left = 5
opp_ships_left = 5


# player makes their guess
while player_ships_left > 0 and opp_ships_left > 0:
    while True:
        row = int(input("Enter row (0-4): "))
        if 0 <= row <= 4:
            break
        else:
            print("Error, please enter a number between 0 and 4.")
            
    while True:
        # Forces the input of A-E to be in uppercase
        col = input("Enter column (A-E): ").upper()
        if col in ['A','B','C', 'D', 'E']:
            break
        else:
            print("Error, please enter a letter between A and E")
            
    col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    col_index = col_dict[col]
    
    if guess(board, row, col_index, 'X'):
        print("Hit!")
        opp_ships_left -= 1
    else:
        print("Miss...")

        
# Opponents make their guess
    opp_row = random.randint(0, len(board) - 1)
    opp_col = random.randint(0, len(board[0]) - 1)
    
    if guess(board, opp_row, opp_col, 'S'):
        print(f"Opponent hit your ship on on row {opp_row} and column {opp_col}!")
        player_ships_left -= 1
    else:
        print("Opponent missed!")
        
    print_board(board)
    