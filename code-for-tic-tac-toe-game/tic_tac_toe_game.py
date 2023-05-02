# Importing libraries
import numpy as np

# Create a 3x3 board having all the zero values.
def create_board():
    return np.zeros((3, 3), dtype=int)

# Place a marker (either 'X' or 'O') on the board
def place_marker(board, player, position):
    board[position] = player

# Display the board
def display_board(board):
    print("   |   |   ")
    print("-----------")
    for row in board:
        print(" {} | {} | {} ".format(row[0], row[1], row[2]))
        print("-----------")
    print("   |   |   ")

# Check if the given player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if np.all(row == player):
            return True
    # Check columns
    for col in board.T:
        if np.all(col == player):
            return True
    # Check diagonals
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

# Check if the game is a tie
def check_tie(board):
    return np.all(board != 0)

# Play a game of Tic Tac Toe
def play_game():
    board = create_board()
    players = ['X', 'O']
    current_player = players[0]
    while True:
        print("Player {}'s turn.".format(current_player))
        position = tuple(map(int, input("Enter the row and column to place your marker on position (e.g. '1 2'): ").split()))
        if board[position] != 0:
            print("That position is already occupied. Try again.")
            continue
        place_marker(board, current_player, position)
        display_board(board)
        if check_winner(board, current_player):
            print("Player {} wins!".format(current_player))
            break
        if check_tie(board):
            print("The game is a tie.")
            break
        current_player = players[(players.index(current_player) + 1) % len(players)]

play_game()
