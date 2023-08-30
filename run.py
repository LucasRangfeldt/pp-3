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

# Places five visible and five invisible ships (V) and (I)
place_random_ships(board, 5, 'V')
place_random_ships(board, 5, 'I')

print('Your board:')
print_board(board)

player_ships_left = 5
opp_ships_left = 5

while player_ships_left > 0 and opp_ships_left > 0:
    # player makes their guess
    row = int(input("Enter row: "))
    col = int(input("Enter column:"))
    
    if guess(board, row, col, 'I'):
        print("Hit!")
        opp_ships_left -=1
    else:
        print("Miss...")
        