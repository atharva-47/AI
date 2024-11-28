###### Function to print the Tic-Tac-Toe board
def print_board(board):
    print("Current State Of Board:\n")
    
    for i in range(9):
        if i > 0 and i % 3 == 0:
            print("\n")
        if board[i] == 0:
            print("- ", end=" ")
        elif board[i] == 1:
            print("O ", end=" ")
        elif board[i] == -1:
            print("X ", end=" ")

    print("\n")

# Function to check for a winner
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != 0:
            return board[combo[0]]  # Return 1 if 'O' wins, -1 if 'X' wins
    if 0 not in board:
        return 0  # Return 0 for a draw
    return None  # Return None if the game is ongoing

# Minimax algorithm for optimal move
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner is not None:
        return winner  # Return score: 1 for O, -1 for X, 0 for draw

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = 1  # 'O' plays
                score = minimax(board, False)
                board[i] = 0
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = -1  # 'X' plays
                score = minimax(board, True)
                board[i] = 0
                best_score = min(score, best_score)
        return best_score

# Function to let the computer make the best move
def computer_move(board):
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == 0:
            board[i] = 1  # 'O' plays
            score = minimax(board, False)
            board[i] = 0
            if score > best_score:
                best_score = score
                move = i
    board[move] = 1

# Function for player's move
def player_move(board):
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] == 0:
            board[move] = -1  # 'X' plays
            break
        else:
            print("Invalid move! Try again.")

def player2_move(board):
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] == 0:
            board[move] = 1  # 'O' plays
            break
        else:
            print("Invalid move! Try again.")

# Main game loop
def play_game():
    board = [0] * 9  # Empty board: 0 means empty, 1 means 'O', -1 means 'X'
    print("Welcome to Tic-Tac-Toe!")
    mode = input("Enter 1 for single-player or 2 for two-player: ")

    if mode == '1':  # Single-player mode
        for turn in range(9):
            print_board(board)
            if turn % 2 == 0:  # Player's turn (X)
                player_move(board)
            else:  # Computer's turn (O)
                computer_move(board)
            winner = check_winner(board)
            if winner is not None:
                break
    else:  # Two-player mode
        for turn in range(9):
            print_board(board)
            if turn % 2 == 0:  # Player 1 (X)
                player_move(board)
            else:  # Player 2 (O)
                player2_move(board)
            winner = check_winner(board)
            if winner is not None:
                break

    print_board(board)
    if winner == 1:
        print("O wins!")
    elif winner == -1:
        print("X wins!")
    else:
        print("It's a draw!")

# Run the game
play_game()
