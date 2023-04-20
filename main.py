X = "X"
O = "O"
POSITIONS = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
BOARD = {key: " " for key in POSITIONS}


def print_board():
    """Print the game board with the current state of the positions."""
    board = f"""        1       2       3
     _______________________
a   |       |       |       |
    |   {BOARD['a1']}   |   {BOARD["a2"]}   |   {BOARD["a3"]}   |
    |_______|_______|_______|
b   |       |       |       |
    |   {BOARD["b1"]}   |   {BOARD["b2"]}   |   {BOARD["b3"]}   |
    |_______|_______|_______|
c   |       |       |       |
    |   {BOARD["c1"]}   |   {BOARD["c2"]}   |   {BOARD["c3"]}   |
    |_______|_______|_______|
"""
    print(board)


def make_move(player):
    """Prompt the player to make a move and print the updated board."""
    while True:
        move = input(f"Player {player}, please choose where to put your {player}: ").lower()
        if move in POSITIONS:
            if BOARD[move] != " ":
                print("Position already taken. Please try again. 😳")
            else:
                BOARD[move] = player
                return
        else:
            print("Invalid position. Please try again. 😵")


def check_winner():
    """If a player has won, the function will return the player, otherwise it will return None."""
    if BOARD['a1'] == BOARD['b2'] == BOARD['c3'] != " " or BOARD['b1'] == BOARD['b2'] == BOARD['b3'] != " " or BOARD['c1'] == BOARD['b2'] == BOARD[
        'a3'] != " " or BOARD[
        'a2'] == BOARD['b2'] == BOARD['c2'] != " ":
        return BOARD['b2']
    elif BOARD["a1"] == BOARD["a2"] == BOARD["a3"] != " " or BOARD['a1'] == BOARD['b1'] == BOARD['c1'] != " ":
        return BOARD['a1']
    elif BOARD['c1'] == BOARD['c2'] == BOARD['c3'] != " " or BOARD['a3'] == BOARD['b3'] == BOARD['c3'] != " ":
        return BOARD['c3']
    return None


def play_again():
    """Ask the player whether to play again and start a new game if yes."""
    while True:
        answer = input("Do you want to play again? Type Y for yes, N for no. 🤓\n").upper()
        if answer == "Y":
            global BOARD
            BOARD = {key: " " for key in BOARD}
            play_game()
            return
        elif answer == "N":
            print('Goodbye. 😘')
            return
        else:
            print("Invalid answer. Please try again. 🤔")


def play_game():
    """Start the game with X plays first then O plays until a player wins or board full."""
    print_board()
    current_player = X
    while True:
        make_move(current_player)
        print_board()
        if check_winner() is not None:
            print(f'Winner is Player {check_winner()}. 🥳')

        elif " " not in BOARD.values():
            print("It's a tie. 😑")

        else:
            if current_player == X:
                current_player = O
            else:
                current_player = X
            continue
        play_again()
        break


print("Welcome! Let's play a Tic Tac Toe game! ❌ 🆚 ⭕")
play_game()
