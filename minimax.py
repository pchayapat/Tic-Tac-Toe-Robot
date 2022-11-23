#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system
import numpy as np
import cv2

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)
"""

print('Welcome to Tic Tac Toe!\nPlease wait for the camera to calibrate...')

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
boundArr = []
cX, cY = 0, 0
move = -1
calibratedBoard = False
cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)
urTXT = 'E:\\ur\\omz\\Ai.txt'

def center(frame, contours, bound=False):
    global cX, cY
    global boundArr
    # calculate moments for each contour
    for c in contours:
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0
        cv2.circle(frame, (cX, cY), 2, (0, 0, 0), -1) #make a dot at the center of the object 
        boundArr.append((cX, cY)) if bound else None

def redFilter(frame, kernel):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower1 = np.array([0, 70, 50])
    upper1 = np.array([10, 255, 255])
    lower2 = np.array([170, 70, 50])
    upper2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower1, upper1)
    mask2 = cv2.inRange(hsv, lower2, upper2)
    mask = mask1 | mask2

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations = 2)
    output = cv2.bitwise_and(frame, frame, mask=opening)
    return output, opening

def purpleFilter(frame, kernel):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([120, 40, 25])
    upper = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations = 1)
    output = cv2.bitwise_and(frame, frame, mask=opening)
    return output, opening

def getBoundary(frame):
    kernel = np.ones((5, 5), np.uint8)
    _, opening = redFilter(frame, kernel)
    ctrs, _ = cv2.findContours(opening.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    center(frame, ctrs, True)

def checkHumanMove(frame):
    global cX, cY, board
    kernel = np.ones((5, 5), np.uint8)

    for rowcnt, row in enumerate(board):
        for elecnt, element in enumerate(row):
            if element in [-1, 1]:
                if rowcnt == 0 and elecnt == 0:
                    cv2.rectangle(frame, (boundArr[0][0], boundArr[1][0]), (boundArr[0][1], boundArr[1][1]), (0, 0, 0), -1)
                elif rowcnt == 0 and elecnt == 1:
                    cv2.rectangle(frame, (boundArr[0][1], boundArr[1][0]), (boundArr[0][2], boundArr[1][1]), (0, 0, 0), -1)
                elif rowcnt == 0 and elecnt == 2:
                    cv2.rectangle(frame, (boundArr[0][2], boundArr[1][0]), (boundArr[0][3], boundArr[1][1]), (0, 0, 0), -1)
                elif rowcnt == 1 and elecnt == 0:
                    cv2.rectangle(frame, (boundArr[0][0], boundArr[1][1]), (boundArr[0][1], boundArr[1][2]), (0, 0, 0), -1)
                elif rowcnt == 1 and elecnt == 1:
                    cv2.rectangle(frame, (boundArr[0][1], boundArr[1][1]), (boundArr[0][2], boundArr[1][2]), (0, 0, 0), -1)
                elif rowcnt == 1 and elecnt == 2:
                    cv2.rectangle(frame, (boundArr[0][2], boundArr[1][1]), (boundArr[0][3], boundArr[1][2]), (0, 0, 0), -1)
                elif rowcnt == 2 and elecnt == 0:
                    cv2.rectangle(frame, (boundArr[0][0], boundArr[1][2]), (boundArr[0][1], boundArr[1][3]), (0, 0, 0), -1)
                elif rowcnt == 2 and elecnt == 1:
                    cv2.rectangle(frame, (boundArr[0][1], boundArr[1][2]), (boundArr[0][2], boundArr[1][3]), (0, 0, 0), -1)
                elif rowcnt == 2 and elecnt == 2:
                    cv2.rectangle(frame, (boundArr[0][2], boundArr[1][2]), (boundArr[0][3], boundArr[1][3]), (0, 0, 0), -1)
            
    _, opening = purpleFilter(frame, kernel)
    ctrs, _ = cv2.findContours(opening.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    center(frame, ctrs)

    if len(boundArr) == 2 and len(boundArr[0]) == 4:
        if boundArr[0][0] < cX < boundArr[0][1] and boundArr[1][0] < cY < boundArr[1][1] and board[0][0] == 0:
            return 1
        if boundArr[0][1] < cX < boundArr[0][2] and boundArr[1][0] < cY < boundArr[1][1] and board[0][1] == 0:
            return 2
        if boundArr[0][2] < cX < boundArr[0][3] and boundArr[1][0] < cY < boundArr[1][1] and board[0][2] == 0:
            return 3
        if boundArr[0][0] < cX < boundArr[0][1] and boundArr[1][1] < cY < boundArr[1][2] and board[1][0] == 0:
            return 4
        if boundArr[0][1] < cX < boundArr[0][2] and boundArr[1][1] < cY < boundArr[1][2] and board[1][1] == 0:
            return 5
        if boundArr[0][2] < cX < boundArr[0][3] and boundArr[1][1] < cY < boundArr[1][2] and board[1][2] == 0:
            return 6
        if boundArr[0][0] < cX < boundArr[0][1] and boundArr[1][2] < cY < boundArr[1][3] and board[2][0] == 0:
            return 7
        if boundArr[0][1] < cX < boundArr[0][2] and boundArr[1][2] < cY < boundArr[1][3] and board[2][1] == 0:
            return 8
        if boundArr[0][2] < cX < boundArr[0][3] and boundArr[1][2] < cY < boundArr[1][3] and board[2][2] == 0:
            return 9
    return -1

def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        if player == COMP:
            if(x==0 and y==0):
                with open(urTXT, 'w') as f:
                    f.write("Robot00")

            elif(x==0 and y == 1):
                with open(urTXT, 'w') as f:
                    f.write("Robot01")

            elif(x==0 and y == 2):
                with open(urTXT, 'w') as f:
                    f.write("Robot02")

            elif(x==1 and y == 0):
                with open(urTXT, 'w') as f:
                    f.write("Robot10")

            elif(x==1 and y == 1):
                with open(urTXT, 'w') as f:
                    f.write("Robot11")

            elif(x==1 and y == 2):
                with open(urTXT, 'w') as f:
                    f.write("Robot12")

            elif(x==2 and y == 0):
                with open(urTXT, 'w') as f:
                    f.write("Robot20")
                
            elif(x==2 and y == 1):
                with open(urTXT, 'w') as f:
                    f.write("Robot21")

            elif(x==2 and y == 2):
                with open(urTXT, 'w') as f:
                    f.write("Robot22")
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(state, c_choice, h_choice):
    """
    Print the board on console
    :param state: current state of the board
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)


def human_turn(c_choice, h_choice, cam):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            frame = VideoCapture(cam)
            move = checkHumanMove(frame)
            print(move, end=" ")
            # move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)
            if not can_move:
                # print('Bad move')
                move = -1
            print(board)
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            pass
    
    cv2.destroyAllWindows()

def VideoCapture(cam):
    scale = 30
    moveCamX, moveCamY = 80, -60

    (_, frame) = cam.read()

    height, width, _ = frame.shape
    camCentX, camCentY = int(width/2) + moveCamX, int(height/2) + moveCamY
    radX, radY = int(scale*width/100), int(scale*height/100)

    minX, maxX = camCentX - radX, camCentX + radX
    minY, maxY = camCentY - radY, camCentY + radY

    roi = frame[minY:maxY, minX:maxX]
    frame = cv2.resize(roi, (width, height))
    return frame

def main():
    """
    Main function that calls all functions
    """
    global board, boundArr, cX, cY, calibratedBoard, cam
    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first
    reset = ''

    while not calibratedBoard:
        frame = VideoCapture(cam)
        getBoundary(frame)
        boundArr = np.array(list(set(boundArr))).T
        boundArr[0], boundArr[1] = sorted(boundArr[0]), sorted(boundArr[1])
        tempX = np.delete(boundArr[0], range(1, len(boundArr[0]), 2))
        tempY = np.delete(boundArr[1], range(1, len(boundArr[1]), 2))
        boundArr = np.array([tempX, tempY]).tolist()
        print('Calibrated!')
        calibratedBoard = True

    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X' and calibratedBoard:
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Human may starts first
    clean()
    while first != 'Y' and first != 'N' and calibratedBoard:
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board) and calibratedBoard:
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        with open('board.txt', 'w') as f:
            f.write(f"{board[0]}\n{board[1]}\n{board[2]}")

        time.sleep(2)

        human_turn(c_choice, h_choice, cam)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMAN):
        clean()
        print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, COMP):
        clean()
        print(f'Computer turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('DRAW!')

    # Restarting the game
    while reset == '':
        reset = input('Play again? [y/n]: ').upper()
        if reset == 'Y':
            with open (urTXT, 'w') as f:
                f.write('clear') # reset ur
            board = np.zeros((3, 3), int).tolist()
            cX, cY = 0, 0
            main()
        elif reset == 'N':
            exit()
        else:
            print('Bad choice')
            reset = ''
    
    # while True:
    #     clean()
    #     print('Camera ON')
    #     trackColor(frame, kernel, 'purple')
    #     trackColor(frame, kernel, 'red')
    #     cv2.imshow('frame', frame)
    #     cv2.waitKey(0)
    #     break

    # exit()


if __name__ == '__main__':
    # run main and camera
    main()
