# boter_kaas_eieren.py
#
# Sogyo Progammeeropdracht: Boter Kaas en Eieren
# Shan Shan Huang
# 30 maart 2019
#
# The bke board class contains attributes and methods to play the game
# 'Boter Kaas en Eieren'.

BOARDSIZE = 3


class Bke_board(object):
    """ Contains attributes and methods for the game 'Boter Kaas en Eieren'.

    """

    def __init__(self):
        """
            Initializes a game board (2D array of size 3x3).
        """

        self.board = []
        counter = 1

        for i in range(BOARDSIZE):
            self.board.append([])
            for j in range(BOARDSIZE):
                self.board[i].append(counter)
                counter += 1

    def enter_choice_player(self, position, player):
        """ Enters a mark on a chosen position on the board. An 'X'-mark for
            player1 and an 'O'-mark for player2.

            Args:
                position (int): chosen position to place a mark.
                player (string): player1 ('X'-mark) or player2 ('O-mark').

        """

        for i in range(BOARDSIZE):
            for j in range(BOARDSIZE):

                if self.board[i][j] == position:

                    if player == "player1":
                        self.board[i][j] = "X"
                    else:
                        self.board[i][j] = "O"

    def print_board(self):
        """ Prints a game board with gridlines and padding of 10.

        """

        for i in range(BOARDSIZE):

            print("{:>10}".format("|") * (BOARDSIZE - 1))

            for j in range(BOARDSIZE):

                mark = self.board[i][j]

                if mark == "X" or mark == "O":
                    print("{:^9}".format(mark), end="")

                # print empty space when no mark
                else:
                    print("{:^9}".format(" "), end="")

                if j != BOARDSIZE - 1:
                    print("{:}".format("|"), end="")

            print("\n"+"{:>10}".format("|") * (BOARDSIZE - 1))

            if i != BOARDSIZE - 1:
                print("-" * 10 * BOARDSIZE)

        print("\n")

    def print_instruction(self):
        """ Prints instruction of the game 'Boter Kaas en Eieren'.

        """

        print("\nWelcome to the game 'Boter Kaas en Eieren!'\
               \nGet three in a row to win this game.\
               \nChoose a position on the board by choosing a number.\
               \nPositions are numbered from 1-9 from left-right, top-bottom.\
               \n\n")

    def __len__(self):
        """ Overrides len() functions.

            Returns:
                The size of the game board.

        """

        return len(self.board)

    def __iter__(self):
        """ Makes object iterable.

            Returns:
                Iterable game board

        """
        return self.board

    def __getitem__(self, index):
        """ Makes indexing of object possible.

            Returns:
                Index of game board

        """

        return self.board[index]
