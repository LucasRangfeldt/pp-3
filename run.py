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
            if cell == 'S' or cell == 'H' or cell == 'M':
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
        board[row][col] = 'H' 
        return True
    else:
        board[row][col] = 'M'
        return False
    
# main code for board
rows, cols = 5, 5
board = create_board(rows, cols)

# Places five visible and five invisible ships S for visible and X for invis.
# The X will transform into a H if hit, or be revealed when match is over
place_random_ships(board, 5, 'S')
place_random_ships(board, 5, 'X')
print("Welcome to the Battlefield!")
print("You and the opponent(NPC) both get 5 ships each")
print("You can both see your own ships, marked S")
print("Whomever destroys all five enemy ships first, wins")
print_board(board)
player_ships_left = 5
opp_ships_left = 5

# Keeping track of already made guesses
already_guessed = []
opp_already_guessed = []
# player makes their guess
while player_ships_left > 0 and opp_ships_left > 0:
    while True:
        try:
            col = input("Enter column (A-E): ").upper()
            if col not in ['A','B','C','D','E']:
                raise ValueError("Invalid column. Please enter a letter between A and E.")
        
            col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
            col_index = col_dict[col]
        
            row = int(input("Enter row (0-4): "))
            if row < 0 or row > 4:
                raise ValueError("Invalid row. Please enter a number between 0 and 4.")
        
            if (row, col_index) in already_guessed:
                raise ValueError("You already guessed those coordinates. Try again.")

            if board[row][col_index] == 'S':
                raise ValueError("You can't target your own ship!")

            already_guessed.append((row, col_index))
            if guess(board, row, col_index, 'X'):
                print(f"You hit the opponent's ship at row {row} and column {col}!")
                opp_ships_left -= 1
            else:
                print("You missed!")
            break
        
        except ValueError as e:
            print(e)
            
    # NPC RNG guess
    opp_row = random.randint(0, len(board) - 1)
    opp_col = random.randint(0, len(board[0]) - 1)
    if (opp_row, opp_col) not in opp_already_guessed:
        opp_already_guessed.append((opp_row, opp_col))
        if guess(board, opp_row, opp_col, 'S'):
            print(f"Opponent hit your ship on on row {opp_row} and column {opp_col}!")
            player_ships_left -= 1
        else:
            print("Opponent missed!")
            
    print_board(board)
    
# Announces the winner and reveals board
if player_ships_left == 0:
    print("You lost, better luck next time!")
elif opp_ships_left == 0:
    print("You won, congratulations!")
    
print("Revealing all ships:")
for i, row in enumerate(board):
    print(i, end=" ")
    for cell in row:
        if cell == 'X':
            print('N', end=" ")
        else:
            print(cell, end=" ")
    print()
