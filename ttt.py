"""--------------------Tic Tac Toe--------------------"""

import random  # Import the random module for computer move generation

# Initialize the board
board = [' ' for _ in range(9)]  # Create a list of 9 empty spaces representing the Tic-Tac-Toe board

def print_board():
    # Print the current state of the board
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('--+---+--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--+---+--')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def check_winner(player):
    # Check rows, columns, and diagonals for a winning combination
    for i in range(0, 7, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def is_full():
    # Check if the board is full
    return ' ' not in board

def get_computer_move():
    # Get a random empty position for the computer's move
    empty_positions = [i for i in range(9) if board[i] == ' ']
    return random.choice(empty_positions)

def play_game():
    current_player = 'X'  # Start with player 'X'
    print("Welcome to Tic-Tac-Toe!")  # Welcome message
    print_board()  # Print the initial empty board

    while True:
        if current_player == 'X':
            # If it's the player's turn, get input
            move = int(input("Player X, enter your move (1-9): ")) - 1
        else:
            # If it's the computer's turn, get a random move
            move = get_computer_move()
            print(f"Computer O chooses position {move + 1}")

        if board[move] == ' ':
            # If the chosen position is empty, place the player's mark
            board[move] = current_player
            print_board()

            if check_winner(current_player):
                # Check if the current player has won
                if current_player == 'X':
                    print("Player X wins!")
                else:
                    print("Computer O wins!")
                break

            if is_full():
                # Check if the board is full (tie game)
                print("It's a tie!")
                break

            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")  # If the move is invalid (position already taken)

play_game()  # Start the game
