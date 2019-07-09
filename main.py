# main.py
#
# Sogyo Progammeeropdracht: Boter Kaas en Eieren
# Shan Shan Huang
# 30 maart 2019
#
# Implementes the game 'Boter Kaas en Eieren'.

import boter_kaas_eieren
import time

used_positions_board = []


def main():

    # creates game board for 'Boter Kaas en Eieren'
    board = boter_kaas_eieren.Bke_board()
    board.print_instruction()
    board.print_board()

    victory = False

    while True:

        # asks player1 to choose position to place mark
        ask_user_input(board, "player1")

        boardsize = len(board)

        # checks if game is won by player1
        for x in range(boardsize):
            for y in range(boardsize):
                if game_won(board, x, y):
                    print("Congratulations! Game is won by player1.")
                    victory = True
                    break
            if victory:
                break
        if victory:
            break

        # checks if game ends as draw
        if len(used_positions_board) == 9:
            print("The game ended in a draw.")
            break

        # asks player2 to choose position to place mark
        ask_user_input(board, "player2")

        # checks if game is won by player2
        for x in range(boardsize):
            for y in range(boardsize):
                if game_won(board, x, y):
                    print("Congratulations! Game is won by player2.")
                    victory = True
                    break
            if victory:
                break
        if victory:
            break


def ask_user_input(board, player):
    """ Checks and validates user input to place a mark on board.

        Args:
            board (2D array): gaming board for 'Boter Kaas en Eieren'.
            player (string): player1/ player2.

    """

    while True:

        position = ""

        # Parses 'X'-mark for player1, 'O'-mark for player2
        if player == "player1":
            position = input("{}, please choose a number to place 'X'.\n"
                             .format(player))
        else:
            position = input("{}, please choose a number to place 'O'.\n"
                             .format(player))

        try:
            position = int(position)

            # checks if user chose empty space
            if position in used_positions_board:
                print("Please enter a mark on an empty space.")
                time.sleep(0.5)
                continue

            # enters 'X' or 'O' on position on board and prints board
            elif 0 < position < 10:
                board.enter_choice_player(position, player)
                board.print_board()
                used_positions_board.append(position)
                break

            # checks if user input is valid
            else:
                print("Please enter a number between 1-9.")
                time.sleep(0.5)
                continue

        except ValueError:
            print("Please enter a number.")
            time.sleep(0.5)
            continue


def game_won(board, m, n):
    """ Checks if game is won when three of the same mark in a row.

        Args:
            board (2D array): game board for 'Boter Kaas en Eieren'.
            m (int): index on game board.
            n (int): index on game board.

    """

    # check if three in row on horizontal lines
    if (board[m][0] == board[m][1] == board[m][2] or

        # check if three in row on vertical lines
        board[0][n] == board[1][n] == board[2][n] or

        # check if three in row on diagonal topleft to bottomright
        board[0][0] == board[1][1] == board[2][2] or

        # check if three in row on diagonal topright to bottomleft
        board[0][2] == board[1][1] == board[2][0]):

        return True

    return False


if __name__ == "__main__":
    main()
