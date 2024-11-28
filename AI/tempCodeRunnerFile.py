def print_board(board):
    
    for i in range(9):
        if i % 3 == 0 and i > 0:
            print("\n")
        if board[i] == 0:
            print("_ ", end = " ")
        elif board[i] == 1:
            print("O ", end = " ")
        elif board[i] == -1:
            print("X ", end = " ")
    print("\n")

def player_turn(board):
    while True:
        move = int(input("Enter the number of box where you want to put X : (1-9)")) -1
        if board[move] == 0:
            board[move] = -1
            break
        else:
            print("Invalid . Try Again")

def comp_turn(board):
    move = 0
    best_score = -float('inf')
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            score = minimax(board,False)
            board[i] = 0 
            if score > best_score:
                best_score = score
                move = i
    board[move] = 1

def check_winner(board):
    winning_combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] !=0:
            return board[combo[0]]
        
    if 0 not in board:
        return 0 
    return None

def minimax(board,is_max):
    winner = check_winner(board)
    if winner is not None:
        return winner
    
    if is_max:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] == 1
                score = minimax(board,False)
                board[i] = 0
                best_score = max(score,best_score)
        return best_score
    
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] == -1
                score = minimax(board,True)
                board[i] = 0
                best_score = min(score,best_score)
        return best_score



def play_game():

    board = [0] * 9
    

    for i in range(9):
        print_board(board)
        if i % 2 == 0 :
            player_turn(board)
        else:
            comp_turn(board)
        winner = check_winner(board)
        if winner is not None:
            break

play_game()