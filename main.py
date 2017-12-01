#!/usr/bin/python3
import pdb
from logic import is_win, best_next_move

board = "---------"

def init():
    print("Welcome to this XO game. You will be playing against an automated player.\nYou will be X and the computer will be O. Good luck!\n\n")

def print_board():
    print("Current state of the game:")

    for i in range(len(board)):
        print("{}:{}\t".format(i, board[i]), end='')
        if i % 3 == 2:
            print()

def move(next_move, player):
    global board
    res = []
    for i in range(next_move):
        res.append(board[i])

    res.append(player)

    for i in range(next_move + 1, len(board)):
        res.append(board[i])

    board = ''.join(res)


def user_input():
    """
    This function will prompt the user to play their turn.
    """

    print_board()
    user_input_okay = False
    next_move = None

    while not user_input_okay:
        try:
            next_move = int(input("It's your turn! Enter your next move:"))
            if not (next_move <= 9 and next_move >= 0):
                raise Exception("Your move should be a number between 0 and 9")

            if board[next_move] == "-":
                user_input_okay = True

            else:
                print("That cell is already full!")

        except Exception:
            print("Error: Enter an integer indicating the index of one of the empty cells.")

    return next_move


def check_state():
    global board

    if is_win(board.replace("X", "-")):
            print("\nComputer wins! You should be ashamed!")
            return True

    elif is_win(board.replace("O", "-")):
        print("You win! The age of AI is not here yet.")
        return True


    for i in board:
        if i == "-":
            return False

    if not is_win(board):
        print("It's a draw!\n")
        return True




def main():
    global board
    init()
    current_player = "X"

    while True:
        if current_player == "X":
            next_move = user_input()
            move(next_move, "X")

        else:
            res, best_next = best_next_move(board, "O")
            print("The computer has decided. Next move: {}".format(best_next))
            if best_next == -1:
                for i in range(len(board)):
                    if board[i] == "-":
                        move(i, "O")
            else:
                move(best_next, "O")


        game_is_finished = check_state()

        if game_is_finished:
            print("\nThank you for playing!")
            return

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


if __name__=="__main__":
    main()