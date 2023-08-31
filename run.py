# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# This code is written by Lucas Rangfeldt
# Big thanks to ChatGPT for examples and ideas
# Also big thanks to Mikke for helping me troubleshoot.
import random

# Function for game board
def create_board(rows, cols):
    return [['~' for _ in range(cols)] for _ in range(rows)]

def print_board(board):
    """Prints the board"""
    
    # Prints coordinates
    print("  ", end="")
    for i in range(len(board[0])):
        print(chr(65 + i), end="  ")
    print()
    # Prints rows
    for i, row in enumerate(board):
        print(i, end=" ")
        for cell in row:
            if cell == 'S' or cell == 'H' or cell == 'M':
                print(cell, end="  ")
            else:
                print('~', end="  ")
        print()
#generates ships randomly on the board
def place_random_ships(board, num_ships, target):
    placed_ships = 0
    while placed_ships < num_ships:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        if board[row][col] == '~':
            board[row][col] = target
            placed_ships += 1
# Guess function
def guess(board, row, col, target):
    if board[row][col] == target:
        board[row][col] = 'H'
        return True
    else:
        board[row][col] = 'M'
        return False
# Main board code
rows, cols = 5, 5
board = create_board(rows, cols)
place_random_ships(board, 5, 'S')
place_random_ships(board, 5, 'X')

#Intro
print("Welcome to the Battlefield!")
print("You and the opponent(NPC) both get 5 ships each")
print("You can both see your own ships, marked S")
print("Whomever destroys all five enemy ships first, wins")

player_ships_left = 5
opp_ships_left = 5
already_guessed = []
opp_already_guessed = []

# Game loop
while player_ships_left > 0 and opp_ships_left > 0:
    print_board(board)
    
    # Player's guess, makes sure input is valid
    while True:
        try:
            col = input("Enter column (A-E): ").upper()
            col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
            col_index = col_dict[col]
            break
        except KeyError:
            print("Invalid coordinate. Please enter a letter between A and E.")
            continue

    while True:
        try:
            row = int(input("Enter row (0-4): "))
            if row in range(0, 5):
                break
            else:
                print("Invalid coordinate. Please enter a number between 0 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 4.")
            
    if (row, col_index) in already_guessed:
        print("You already guessed those coordinates. Try again.")
        continue
    already_guessed.append((row, col_index))
    
    if guess(board, row, col_index, 'X'):
        print(f"You hit the opponent's ship at row {row} and column {col}!")
        opp_ships_left -= 1
    else:
        print("You missed!")
    
    # NPC guess
    opp_row, opp_col = random.randint(0, rows-1), random.randint(0, cols-1)
    while (opp_row, opp_col) in opp_already_guessed:
        opp_row, opp_col = random.randint(0, rows-1), random.randint(0, cols-1)
    opp_already_guessed.append((opp_row, opp_col))

    if guess(board, opp_row, opp_col, 'S'):
        print(f"Opponent hit your ship at row {opp_row} and column {chr(65 + opp_col)}!")
        player_ships_left -= 1
    else:
        print("Opponent missed!")

# Announces winner
if player_ships_left == 0:
    print("You lost, better luck next time!")
elif opp_ships_left == 0:
    print("You won, congratulations!")
    
# Reveal entire board when finished
print("Revealing all ships:")
for i, row in enumerate(board):
    print(i, end=" ")
    for cell in row:
        if cell == 'X':
            print('N', end="  ")
        else:
            print(cell, end="  ")
    print()
