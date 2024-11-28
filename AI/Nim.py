def print_pile(pile):
    print(f"Current Pile: {pile} objects")

def player_turn(pile, player):
   
    print(f"\n{player}'s turn.")
    print_pile(pile)
    
    # Get valid number of objects to remove
    while True:
        try:
            num_objects = int(input("How many objects to remove (1, 2, or 3)? "))
            if num_objects not in [1, 2, 3] or num_objects > pile:
                print("Invalid input. You can only remove 1, 2, or 3 objects.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Remove objects from the pile
    pile -= num_objects
    return pile

def minimax(pile, is_maximizing_player):
   
    # If the game is over (pile is empty), return the result (loss = -1, win = +1)
    if pile == 0:
        return 1 if is_maximizing_player else -1  # The player who takes the last object loses

    if is_maximizing_player:
        best_score = -float('inf')  # Maximizing player's best score (AI)
        for move in [1, 2, 3]:
            if pile - move >= 0:
                score = minimax(pile - move, False)  # Opponent's turn to minimize
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')  # Minimizing player's best score (opponent)
        for move in [1, 2, 3]:
            if pile - move >= 0:
                score = minimax(pile - move, True)  # AI's turn to maximize
                best_score = min(best_score, score)
        return best_score

def best_move(pile):
    
    best_score = -float('inf')
    move = None
    for num_objects in [1, 2, 3]:
        if pile - num_objects >= 0:
            score = minimax(pile - num_objects, False)  # Minimize for opponent
            if score > best_score:
                best_score = score
                move = num_objects
    return move

def nim_game_single_pile_with_ai_misere():
    # Initial pile size
    pile = 20

    # Players take turns
    current_player = "Player 1"
    while pile > 0:
        if current_player == "Player 1":
            pile = player_turn(pile, current_player)
            if pile == 0:
                print(f"\n{current_player} takes the last object!")
                print(f"{current_player} loses!")
                break
            current_player = "Player 2"  # Switch to AI
        else:
            # AI's turn (Player 2)
            print("\nAI's turn:")
            move = best_move(pile)
            pile -= move
            print(f"AI removed {move} objects. Remaining pile: {pile}")
            if pile == 0:
                print("\nAI takes the last object!")
                print("AI loses!")
                break
            current_player = "Player 1"  # Switch to player 1

# Start the game with AI (Misère version: Last Object Loses)
nim_game_single_pile_with_ai_misere()
