
board = [' ' for _ in range(9)] # Initialize the game board

def print_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def check_win():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False

def play_game():
    current_player = 'X'
    while True:
        print_board()
        move = input("Player {}, enter your move (1-9): ".format(current_player))
        if board[int(move) - 1] == ' ':
            board[int(move) - 1] = current_player
            if check_win():
                print_board()
                print("Player {} wins! Congratulations!".format(current_player))
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move, try again.")

play_game()
