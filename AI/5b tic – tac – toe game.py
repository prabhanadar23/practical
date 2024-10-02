import os
import time

print("04_Jayprabha Nadar")

# Board for the game
board = [' '] * 10  # Create a list of 10 spaces (index 0 unused)
current_player = 1

# Game status constants
WIN = 1
DRAW = -1
RUNNING = 0

# Function to draw the game board
def draw_board():
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("___|___|___")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("___|___|___")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")

# Function to check if the position is empty
def check_position(x):
    return board[x] == ' '

# Function to check if a player has won
def check_win():
    # Check horizontal, vertical, and diagonal winning conditions
    winning_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
        (1, 5, 9), (3, 5, 7)               # Diagonal
    ]
    for a, b, c in winning_conditions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return WIN
    return DRAW if all(board[i] != ' ' for i in range(1, 10)) else RUNNING

# Function to clear the screen (works for both Windows and Unix-like systems)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Start the game
print("Tic-Tac-Toe Game")
print("Player 1 [X] --- Player 2 [O]\n")
time.sleep(1)

game_status = RUNNING

while game_status == RUNNING:
    clear_screen()
    draw_board()

    # Decide the player's turn
    mark = 'X' if current_player % 2 != 0 else 'O'
    print(f"Player {1 if mark == 'X' else 2}'s chance")

    # Get player input and validate it
    try:
        choice = int(input("Enter the position between [1-9] where you want to mark: "))
        if choice < 1 or choice > 9:
            raise ValueError("Invalid input. Please choose a number between 1 and 9.")
    except ValueError as e:
        print(e)
        time.sleep(2)
        continue

    if check_position(choice):
        board[choice] = mark
        current_player += 1
        game_status = check_win()
    else:
        print("Position already taken, try another.")
        time.sleep(2)

clear_screen()
draw_board()

# Game result output
if game_status == DRAW:
    print("Game Draw!")
else:
    print(f"Player {2 if mark == 'X' else 1} Won!")
