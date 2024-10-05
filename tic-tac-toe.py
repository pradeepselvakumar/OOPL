def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))

def continue_game(board, player):
    if board.count(player) < 3:
        return True

    win_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]

    # get all the indices that player is currently occupying
    player_tiles = [i for i in range(len(board)) if board[i] == player]

    # if the list of tiles the player is occupying is a super set of a
    # win pattern, the player has won
    for pattern in win_patterns:
        if set(pattern).issubset(player_tiles):
            print(f"{player} wins!")
            return False

    if (board.count('X') + board.count('O')) == 9:
        print("It's a Draw!")
        return False
    
    return True

def run_game():
    board = [f"{i}" for i in range(1, 10)]
    player = 'X'

    while True:
        print_board(board)
        num = int(input(f"Enter your choice, {player}: "))
        if board[num - 1] in ['X', 'O']:
            print("Invalid move!")
            continue
        board[num - 1] = player
        if not continue_game(board, player):
            break
        player = 'X' if player == 'O' else 'O'

while True:
    run_game()
    command = input("Do you want to continue (y/n)? ")
    if (command == 'n'):
        break;
