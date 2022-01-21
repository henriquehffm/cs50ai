"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return 0
    count_x = 0
    count_o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_x += 1
            elif board[i][j] == O:
                count_o += 1
    if count_x > count_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action in actions(board):
        boardx = board
        boardx[action[0]][action[1]] = player(board)
        return boardx
    else:
        raise NotValidAction


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    """horizontally"""
    for i in range(3):
        count = 0
        for j in range(1,3):
            if board[i][0] == board[i][j]:
                count += 1
                if count == 2:
                    return board[i][0]
    """vertically"""
    for j in range(3):
        count = 0
        for i in range(1,3):
            if board[0][j] == board[i][j]:
                count += 1
                if count == 2:
                    return board[i][0]
    """diagonally"""
    count = 0
    countx = 0
    for x in range(1,3):
        if board[0][0] == board[x][x]:
            count += 1
            if count == 2:
                return board[x][x]
        if board[0][2] == board[x][2-x]:
            countx += 1
            if countx == 2:
                return board[x][x]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
                else:
                    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
