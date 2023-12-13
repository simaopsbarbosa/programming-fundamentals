def string_to_matrix(board):
    '''
    aux function to transform a string board
    into a list of lists for better visibilty
    '''
    # ' xx\n o \noxo'
    return [[board[0], board[1], board[2]],
            [board[4], board[5], board[6]],
            [board[8], board[9], board[10]]]


def tic_tac_toe(board: str, player):

    # winning move only

    # check sides and diagonals

    board.split("\n")
    "".join(board)
    return board


print(tic_tac_toe(" xx\n o \noxo", 1))
