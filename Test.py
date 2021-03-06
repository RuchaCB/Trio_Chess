"""
Trio_Chess Trial
Author: Rucha_CB
"""
import unittest
import turtle
import math
from centroid import centroid


POLYGON = turtle.Turtle()

"""to add images"""
SCREEN = turtle.Screen()

"""Blue Pieces"""
BR2 = turtle.Turtle()
BR1 = turtle.Turtle()
BN1 = turtle.Turtle()
BB1 = turtle.Turtle()
BQ = turtle.Turtle()
BK = turtle.Turtle()
BB2 = turtle.Turtle()
BN2 = turtle.Turtle()
BP1 = turtle.Turtle()
BP2 = turtle.Turtle()
BP3 = turtle.Turtle()
BP4 = turtle.Turtle()
BP5 = turtle.Turtle()
BP6 = turtle.Turtle()
BP7 = turtle.Turtle()
BP8 = turtle.Turtle()
"""Red Pieces"""
RR2 = turtle.Turtle()
RR1 = turtle.Turtle()
RN1 = turtle.Turtle()
RB1 = turtle.Turtle()
RQ = turtle.Turtle()
RK = turtle.Turtle()
RB2 = turtle.Turtle()
RN2 = turtle.Turtle()
RP1 = turtle.Turtle()
RP2 = turtle.Turtle()
RP3 = turtle.Turtle()
RP4 = turtle.Turtle()
RP5 = turtle.Turtle()
RP6 = turtle.Turtle()
RP7 = turtle.Turtle()
RP8 = turtle.Turtle()
"""Green Pieces"""
GR1 = turtle.Turtle()
GN1 = turtle.Turtle()
GB1 = turtle.Turtle()
GQ = turtle.Turtle()
GK = turtle.Turtle()
GB2 = turtle.Turtle()
GN2 = turtle.Turtle()
GR2 = turtle.Turtle()
GP1 = turtle.Turtle()
GP2 = turtle.Turtle()
GP3 = turtle.Turtle()
GP4 = turtle.Turtle()
GP5 = turtle.Turtle()
GP6 = turtle.Turtle()
GP7 = turtle.Turtle()
GP8 = turtle.Turtle()

"""Lists of all the turtle objects"""
BLUE = [BR1, BN1, BB1, BQ, BK, BB2, BN2, BR2, BP1, BP2, BP3, BP4, BP5, BP6, BP7, BP8]
RED = [RR1, RN1, RB1, RQ, RK, RB2, RN2, RR2, RP1, RP2, RP3, RP4, RP5, RP6, RP7, RP8]
GREEN = [GR1, GN1, GB1, GQ, GK, GB2, GN2, GR2, GP1, GP2, GP3, GP4, GP5, GP6, GP7, GP8]

PIECES = ['R1', 'N1', 'B1', 'Q', 'K', 'B2', 'N2', 'R2',
          'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'
         ]

BLUE_DESTI = ['A1', 'B1', 'C1', 'D1', 'D4', 'F3', 'G1', 'H1',
              'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'
             ]
RED_DESTI = ['L8', 'K8', 'J6', 'I8', 'E9', 'C6', 'B8', 'A8',
             'L7', 'K7', 'J7', 'I7', 'D7', 'C7', 'B7', 'A7'
            ]
GREEN_DESTI = ['H12', 'G12', 'F10', 'E12', 'I5', 'J10', 'K12', 'L12',
               'H11', 'G11', 'F11', 'E11', 'I11', 'J11', 'K11', 'L11'
              ]
PIECES = ['R1', 'N1', 'B1', 'Q', 'K', 'B2', 'N2', 'R2',
          'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'
         ]
BLUE_STR = ['bR1', 'bN1', 'bB1', 'bQ', 'bK', 'bB2', 'bN2', 'bR2',
            'bP1', 'bP2', 'bP3', 'bP4', 'bP5', 'bP6', 'bP7', 'bP8'
           ]
RED_STR = ['rR1', 'rN1', 'rB1', 'rQ', 'rK', 'rB2', 'rN2', 'rR2',
           'rP1', 'rP2', 'rP3', 'rP4', 'rP5', 'rP6', 'rP7', 'rP8'
          ]
GREEN_STR = ['gR1', 'gN1', 'gB1', 'gQ', 'gK', 'gB2', 'gN2', 'gR2',
             'gP1', 'gP2', 'gP3', 'gP4', 'gP5', 'gP6', 'gP7', 'gP8'
            ]

CENTER_STAR = ('D4', 'D5', 'I5', 'I9', 'E9', 'E4')

for b, r, g in zip(BLUE_STR, RED_STR, GREEN_STR):
    SCREEN.addshape(b+'.gif')
    SCREEN.addshape(r+'.gif')
    SCREEN.addshape(g+'.gif')

POLYGON.speed(0)
"""Will count till 96 for squares"""
COUNT = 0

def square(SIDE, LENGTH):
    """To draw square"""
    POLYGON.forward(SIDE)
    POLYGON.right(90)
    p1 = POLYGON.pos()
    POLYGON.forward(LENGTH)
    POLYGON.right(120)
    p2 = POLYGON.pos()
    POLYGON.forward(LENGTH)
    POLYGON.right(90)
    p3 = POLYGON.pos()
    POLYGON.forward(SIDE)
    POLYGON.right(60)
    p4 = POLYGON.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex) #being called from centroid.py
    sq = {'centro': centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    return sq


def square_2(LENGTH, SIDE):
    """To draw square type 2"""
    p1 = POLYGON.pos()
    POLYGON.forward(SIDE)
    p2 = POLYGON.pos()
    POLYGON.right(90)
    POLYGON.forward(LENGTH)
    p3 = POLYGON.pos()
    POLYGON.right(90)
    POLYGON.forward(SIDE)
    p4 = POLYGON.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex)
    sq = {'centro': centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    return sq

def square_3(LENGTH, SIDE):
    """To draw square type 3"""
    p1 = POLYGON.pos()
    POLYGON.backward(SIDE)
    p2 = POLYGON.pos()
    POLYGON.left(90)
    POLYGON.forward(LENGTH)
    p3 = POLYGON.pos()
    POLYGON.right(90)
    POLYGON.forward(SIDE)
    p4 = POLYGON.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex)
    sq = {'centro': centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    return sq

def alternate_color_1(num):
    """To fill alternate color type 1"""
    if num%2 == 0:
        POLYGON.fillcolor('white')
    else:
        POLYGON.fillcolor('black')

def alternate_color_2(num):
    """To fill alternate color type 2"""
    if num%2 == 0:
        POLYGON.fillcolor('black')
    else:
        POLYGON.fillcolor('white')


SIDE = 40 #changing SIDE will change the size of board
SIDE_2 = 2*SIDE
SIDE_3 = 3*SIDE
SIDE_4 = 4*SIDE
LENGTH = math.sqrt(((SIDE*2)**2)-(SIDE**2))
LENGTH_2 = math.sqrt(((SIDE_2*2)**2)-(SIDE_2**2))
LENGTH_3 = math.sqrt(((SIDE_3*2)**2)-(SIDE_3**2))
LENGTH_4 = math.sqrt(((SIDE_4*2)**2)-(SIDE_4**2))

POLYGON.setpos(-SIDE*4, SIDE*8)

ROW = dict
COLUMN = dict
group = dict

ROW = {"ROW_1": ("A", "B", "C", "D"),
       "ROW_2": ("H", "G", "F", "E"),
       "ROW_3": ("L", "K", "J", "I")
      }

COLUMN = {"COLUMN_1" :("1", "2", "3", "4"),
          "COLUMN_2" :("8", "7", "6", "5"),
          "COLUMN_3" :("12", "11", "10", "9")
         }

EXTREME_ROW = ('E', 'D', 'I')
EXTREME_COLUMN = ('4', '5', '9')

MATRIX_1 = []
MATRIX_2 = []
MATRIX_3 = []
MATRIX_4 = []
MATRIX_5 = []
MATRIX_6 = []

GROUPING = {}

for x in ROW["ROW_3"]:
    for y in COLUMN["COLUMN_3"]:
        MATRIX_1.append(x+y)
GROUPING["g_1"] = MATRIX_1

for x in ROW["ROW_2"]:
    for y in COLUMN["COLUMN_3"]:
        MATRIX_2.append(x+y)
GROUPING["g_2"] = MATRIX_2

for x in ROW["ROW_2"]:
    for y in COLUMN["COLUMN_1"]:
        MATRIX_3.append(x+y)
GROUPING["g_3"] = MATRIX_3

for x in ROW["ROW_1"]:
    for y in COLUMN["COLUMN_1"]:
        MATRIX_4.append(x+y)
GROUPING["g_4"] = MATRIX_4

for x in ROW["ROW_1"]:
    for y in COLUMN["COLUMN_2"]:
        MATRIX_5.append(x+y)
GROUPING["g_5"] = MATRIX_5

for x in ROW["ROW_3"]:
    for y in COLUMN["COLUMN_2"]:
        MATRIX_6.append(x+y)
GROUPING["g_6"] = MATRIX_6

GROUP_1 = ROW["ROW_3"], COLUMN["COLUMN_3"]
GROUP_1_STAR = "I9"
GROUP_2 = COLUMN["COLUMN_3"], ROW["ROW_2"]
GROUP_2_STAR = "E9"
GROUP_3 = ROW["ROW_2"], COLUMN["COLUMN_1"]
GROUP_3_STAR = "E4"
GROUP_4 = COLUMN["COLUMN_1"], ROW["ROW_1"]
GROUP_4_STAR = "D4"
GROUP_5 = ROW["ROW_1"], COLUMN["COLUMN_2"]
GROUP_5_STAR = "D5"
GROUP_6 = COLUMN["COLUMN_2"], ROW["ROW_3"]
GROUP_6_STAR = "I5"

FOR_ROOK = {"g_1":"g_4", "g_2":"g_5", "g_3":"g_6", "g_4":"g_1", "g_5":"g_2", "g_6":"g_3"}

FOR_BISHOP_ROW_1 = ["A", "B", "C", "D", "E", "F", "G", "H"]
FOR_BISHOP_ROW_2 = ["H", "G", "F", "E", "I", "J", "K", "L"]
FOR_BISHOP_ROW_3 = ["L", "K", "J", "I", "D", "C", "B", "A"]
FOR_BISHOP_COLUMN_1 = ["1", "2", "3", "4", "9", "10", "11", "12"]
FOR_BISHOP_COLUMN_2 = ["12", "11", "10", "9", "5", "6", "7", "8"]
FOR_BISHOP_COLUMN_3 = ["8", "7", "6", "5", "4", "3", "2", "1"]

FOR_BISHOP = {
    ("g_2", "g_3", "g_4"):(FOR_BISHOP_ROW_1, FOR_BISHOP_COLUMN_1),
    ("g_3", "g_4", "g_5"):(FOR_BISHOP_ROW_1, FOR_BISHOP_COLUMN_3),
    ("g_1", "g_2", "g_3"):(FOR_BISHOP_ROW_2, FOR_BISHOP_COLUMN_1),
    ("g_1", "g_2", "g_6"):(FOR_BISHOP_ROW_2, FOR_BISHOP_COLUMN_2),
    ("g_1", "g_5", "g_6"):(FOR_BISHOP_ROW_3, FOR_BISHOP_COLUMN_2),
    ("g_4", "g_5", "g_6"):(FOR_BISHOP_ROW_3, FOR_BISHOP_COLUMN_3)
}

NAMING = GROUP_1, GROUP_2, GROUP_3, GROUP_4, GROUP_5, GROUP_6
SQUARE_DICT = {}

for i in range(6):

    POLYGON.forward(8*SIDE)
    POLYGON.right(60)
    POLYGON.begin_fill()
    sq = square(SIDE, LENGTH)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][0]+NAMING[i][0][0]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][0]+NAMING[i][1][0]] = sq

    POLYGON.forward(SIDE)

    POLYGON.begin_fill()
    sq = square_2(LENGTH_2/2, SIDE)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][0]+NAMING[i][0][1]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][1]+NAMING[i][1][0]] = sq

    POLYGON.left(180)

    POLYGON.begin_fill()
    sq = square(SIDE, LENGTH)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][1]+NAMING[i][0][1]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][1]+NAMING[i][1][1]] = sq

    POLYGON.begin_fill()
    POLYGON.right(120)
    sq = square_2(LENGTH_2/2, SIDE)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][1]+NAMING[i][0][0]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][0]+NAMING[i][1][1]] = sq

    POLYGON.forward(SIDE)
    POLYGON.right(60)
    POLYGON.forward(2*SIDE)

    POLYGON.begin_fill()
    sq = square_2(LENGTH_3/3, SIDE)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][0]+NAMING[i][0][2]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][2]+NAMING[i][1][0]] = sq

    POLYGON.begin_fill()
    sq = square_3(LENGTH_3/3, SIDE)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][1]+NAMING[i][0][2]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][2]+NAMING[i][1][1]] = sq

    POLYGON.backward(SIDE)
    POLYGON.left(90)

    POLYGON.begin_fill()
    p1 = POLYGON.pos()
    POLYGON.forward(LENGTH_3/3)
    p2 = POLYGON.pos()
    POLYGON.right(120)
    POLYGON.forward(LENGTH_3/3)
    p3 = POLYGON.pos()
    POLYGON.right(90)
    POLYGON.forward(SIDE)
    p4 = POLYGON.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex)

    alternate_color_1(i)
    sq = {'centro':centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}

    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][2]+NAMING[i][0][2]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][2]+NAMING[i][1][2]] = sq

    POLYGON.begin_fill()
    sq = square_3(LENGTH_3/3, SIDE)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][2]+NAMING[i][0][1]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][1]+NAMING[i][1][2]] = sq

    POLYGON.begin_fill()
    sq = square_3(LENGTH_3/3, SIDE)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][2]+NAMING[i][0][0]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][0]+NAMING[i][1][2]] = sq

    POLYGON.forward(SIDE*2)
    POLYGON.right(60)
    POLYGON.forward(SIDE*3)

    POLYGON.begin_fill()
    sq = square_2(LENGTH_4/4, SIDE)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][0]+NAMING[i][0][3]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][3]+NAMING[i][1][0]] = sq

    POLYGON.begin_fill()
    sq = square_3(LENGTH_4/4, SIDE)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][1]+NAMING[i][0][3]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][3]+NAMING[i][1][1]] = sq

    POLYGON.begin_fill()
    sq = square_3(LENGTH_4/4, SIDE)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][2]+NAMING[i][0][3]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][3]+NAMING[i][1][2]] = sq

    POLYGON.backward(SIDE)
    POLYGON.left(90)

    POLYGON.begin_fill()
    p1 = POLYGON.pos()
    POLYGON.forward(LENGTH_4/4)
    p2 = POLYGON.pos()
    POLYGON.right(120)
    POLYGON.forward(LENGTH_4/4)
    p3 = POLYGON.pos()
    POLYGON.right(90)
    POLYGON.forward(SIDE)
    p4 = POLYGON.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex)
    alternate_color_1(i)
    sq = {'centro':centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][3]+NAMING[i][0][3]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][3]+NAMING[i][1][3]] = sq

    POLYGON.begin_fill()
    sq = square_3(LENGTH_4/4, SIDE)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][3]+NAMING[i][0][2]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][2]+NAMING[i][1][3]] = sq

    POLYGON.begin_fill()
    sq = square_3(LENGTH_4/4, SIDE)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][3]+NAMING[i][0][1]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][1]+NAMING[i][1][3]] = sq

    POLYGON.begin_fill()
    sq = square_3(LENGTH_4/4, SIDE)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        SQUARE_DICT[NAMING[i][1][3]+NAMING[i][0][0]] = sq
    else:
        SQUARE_DICT[NAMING[i][0][0]+NAMING[i][1][3]] = sq

    POLYGON.forward(SIDE*3)
    POLYGON.right(60)

STAR = {"R":{"bR1":(BR1, {"checked":0}), "bR2":(BR2, {"checked":0}),
             "rR1":(RR1, {"checked":0}), "rR2":(RR2, {"checked":0}),
             "gR1":(GR1, {"checked":0}), "gR2":(GR2, {"checked":0})},
        "B":{"bB1":BB1, "bB2":BB2, "rB1":RB1, "rB2":RB2, "gB1":GB1, "gB2":GB2},
        "N":{"bN1":BN1, "bN2":BN2, "rN1":RN1, "rN2":RN2, "gN1":GN1, "gN2":GN2},
        "K":{"bK":(BK, {"checked":0}), "rK":(RK, {"checked":0}), "gK":(GK, {"checked":0})},
        "Q":{"bQ":BQ, "rQ":RQ, "gQ":GQ},
        "P":{"bP1":(BP1, {"checked":0}), "bP2":(BP2, {"checked":0}),
             "bP3":(BP3, {"checked":0}), "bP4":(BP4, {"checked":0}),
             "bP5":(BP5, {"checked":0}), "bP6":(BP6, {"checked":0}),
             "bP7":(BP7, {"checked":0}), "bP8":(BP8, {"checked":0}),
             "gP1":(GP1, {"checked":0}), "gP2":(GP2, {"checked":0}),
             "gP3":(GP3, {"checked":0}), "gP4":(GP4, {"checked":0}),
             "gP5":(GP5, {"checked":0}), "gP6":(GP6, {"checked":0}),
             "gP7":(GP7, {"checked":0}), "gP8":(GP8, {"checked":0}),
             "rP1":(RP1, {"checked":0}), "rP2":(RP2, {"checked":0}),
             "rP3":(RP3, {"checked":0}), "rP4":(RP4, {"checked":0}),
             "rP5":(RP5, {"checked":0}), "rP6":(RP6, {"checked":0}),
             "rP7":(RP7, {"checked":0}), "rP8":(RP8, {"checked":0})
            }
        }

def start_pos(clr, destination, gif):
    """starting position of the pieces"""
    for piece, desti, pic in zip(clr, destination, gif):
        piece.shape(pic +'.gif')
        piece.penup()
        piece.setpos(SQUARE_DICT[desti]['centro'])

start_pos(BLUE, BLUE_DESTI, BLUE_STR)
start_pos(RED, RED_DESTI, RED_STR)
start_pos(GREEN, GREEN_DESTI, GREEN_STR)

def get_pos(piece):
    """takes piece and returns its location by terating throuh SQUARE_DICT"""
    loc = piece.pos()
    for key, value in SQUARE_DICT.items():
        if value['centro'] == loc:
            return key

def rook_validate(piece, initial_pos, desti):
    """validates the rook moves"""
    #step_1: get matrix of initial pos
    #step_2: get matrix of desti pos
    #step_3: get the star position of initial matrix
    #step_4: get the star position of destination matrix
    #step_5: get star combo according to piece type and initial matrix ka star position
    for key, value in GROUPING.items():
        if initial_pos in value:
            ini_pos_matrix = key
        if desti in value:
            desti_pos_matrix = key

    if FOR_ROOK[ini_pos_matrix] == desti_pos_matrix:
        if (initial_pos[1:] in EXTREME_COLUMN) and (desti[1:] in EXTREME_COLUMN):
            return True
        elif (initial_pos[0] in EXTREME_ROW) and (desti[0] in EXTREME_ROW):
            return True
        else:
            return False

    if initial_pos[0] == desti[0]:
        return True
    elif initial_pos[1:] == desti[1:]:
        return True
    else:
        return False

def triangle(ORIGNAL_ROW, COLUMN):
    ROW = ORIGNAL_ROW[:]
    triangle = []
    for i in COLUMN:
        ROW.pop(0)
        ROW.pop(-1)
        for j in ROW:
            try:
                int(j)
                triangle.append(i+j)
            except:
                triangle.append(j+i)
    return tuple(triangle)

TRIANGLE_61 = triangle(FOR_BISHOP_COLUMN_2, ROW['ROW_3'])
TRIANGLE_34 = triangle(FOR_BISHOP_ROW_1, COLUMN['COLUMN_1'])

TRIANGLE_45 = triangle(FOR_BISHOP_COLUMN_3, ROW['ROW_1'])
TRIANGLE_12 = triangle(FOR_BISHOP_ROW_2, COLUMN['COLUMN_3'])

TRIANGLE_56 = triangle(FOR_BISHOP_ROW_3, COLUMN['COLUMN_2'])
TRIANGLE_23 = triangle(FOR_BISHOP_COLUMN_1, ROW['ROW_2'])

TRIANGLES = {
    TRIANGLE_61:TRIANGLE_34,
    TRIANGLE_45:TRIANGLE_12,
    TRIANGLE_56:TRIANGLE_23
    }

def bishop_validate(piece, initial_pos, desti):
    """validates the rook moves"""
    for key, value in GROUPING.items():
        if initial_pos in value:
            ini_pos_matrix = key #g_1,g_2,
        if desti in value:
            desti_pos_matrix = key #g_1,g_2

    for key, value in TRIANGLES.items():
        if (initial_pos in key) and (desti in value) or (initial_pos in value) and (desti in key):
            return False
    for key, value in FOR_BISHOP.items():
        if (ini_pos_matrix in key) and (desti_pos_matrix in key):
            a = value[0].index(initial_pos[0]) - value[1].index(initial_pos[1:])
            b = value[0].index(desti[0]) - value[1].index(desti[1:])
            if a == b:
                return True
    return False


def queen_validate(piece, initial_pos, desti):
    """validates the queen moves"""
    if rook_validate(piece, initial_pos, desti) or bishop_validate(piece, initial_pos, desti):
        return True
    else:
        return False


def king_validate(piece, initial_pos, desti):
    """validates the king moves"""

    if initial_pos[0] == desti[0] and (str(int(initial_pos[1:])+1) == desti[1:] or str(int(initial_pos[1:])-1) == desti[1:]):# C3 -> C2 or C3 -> C4
        return True
    elif initial_pos[1:] == desti[1:] and ((ord(initial_pos[0])+1) == ord(desti[0]) or (ord(initial_pos[0])-1) == ord(desti[0])): #C3->D3 or C3->B3
        return True
    elif (str(int(initial_pos[1:])+1) == desti[1:] or str(int(initial_pos[1:])-1) == desti[1:]) and ((ord(initial_pos[0])+1) == ord(desti[0]) or (ord(initial_pos[0])-1) == ord(desti[0])): #C3->D3 or C3->B3
        return True
    elif (initial_pos in CENTER_STAR) and (desti in CENTER_STAR):
        return True
    elif (initial_pos[0] in EXTREME_ROW) and (desti[0] in EXTREME_ROW) and ((int(initial_pos[1]) == int(desti[1]))or(int(initial_pos[1])+1 == int(desti[1]))or(int(initial_pos[1])-1 == int(desti[1]))):
        return True
    elif (initial_pos[1] in EXTREME_COLUMN) and (desti[1] in EXTREME_COLUMN) and ((ord(initial_pos[0]) == ord(desti[0]))or(ord(initial_pos[0])+1 == int(ord(desti[0])))or(ord(initial_pos[0])-1 == int(ord(desti[0])))):
        return True
    else:
        return False


def knight_validate(piece, initial_pos, desti):
    """validates the knight moves"""
    """     initial_pos_10 = chr(ord(initial_pos[0])+1)+initial_pos[1:]
    initial_pos__10 = chr(ord(initial_pos[0])-1)+initial_pos[1:]

    initial_pos_01 = initial_pos[0]+str(int(initial_pos[1:])+1)
    initial_pos_0_1 = initial_pos[0]+str(int(initial_pos[1:])-1)

    i_ini_pos_1 = (initial_pos_10, initial_pos__10)
    i_ini_pos_2= (initial_pos_01, initial_pos_0_1)
    
    """
    if ord(initial_pos[0])+1 == ord(desti[0]) and int(initial_pos[1:])+2 == int(desti[1:]):
        return True
    elif ord(initial_pos[0])-1 == ord(desti[0]) and int(initial_pos[1:])-2 == int(desti[1:]):
        return True
    elif ord(initial_pos[0])+1 == ord(desti[0]) and int(initial_pos[1:])-2 == int(desti[1:]):
        return True
    elif ord(initial_pos[0])-1 == ord(desti[0]) and int(initial_pos[1:])+2 == int(desti[1:]):
        return True
    elif ord(initial_pos[0])+2 == ord(desti[0]) and int(initial_pos[1:])+1 == int(desti[1:]):
        return True
    elif ord(initial_pos[0])-2 == ord(desti[0]) and int(initial_pos[1:])-1 == int(desti[1:]):
        return True
    elif ord(initial_pos[0])-2 == ord(desti[0]) and int(initial_pos[1:])+1 == int(desti[1:]):
        return True
    elif ord(initial_pos[0])+2 == ord(desti[0]) and int(initial_pos[1:])-1 == int(desti[1:]):
        return True 
    else:
        return False 
    

FOR_PAWN = ('E4', 'E9'), ('E4', 'I5'), ('E9', 'D5'), ('I9', 'I5'), ('I9', 'D4'), ('D5', 'D4')
def pawn_validate(color, piece, initial_pos, desti):
    """validates the pawn moves"""
    for tup in FOR_PAWN:
        if (initial_pos in tup)and (desti in tup):
            return True

    checked = STAR['P'][piece][1]["checked"]

    for key, value in GROUPING.items():
        if initial_pos in value:
            ini_pos_matrix = key #g_1, g_2,
        if desti in value:
            desti_pos_matrix = key

    if color == 'b':
        if ini_pos_matrix == desti_pos_matrix:
            if initial_pos[0] == desti[0]:
                if checked == 0:
                    if str(int(initial_pos[1:])+1) == desti[1:] or str(int(initial_pos[1:])+2) == desti[1:]:
                        return True
                    else:
                        return False
                elif checked != 0:
                    if str(int(initial_pos[1:])+1) == desti[1:]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif (initial_pos[1] == '4')and((desti[1] == '5')or(desti[1] == '9')) and (initial_pos[0] == desti[0]):
            return True
        else:
            return False

    elif color == 'r':
        if(ini_pos_matrix in ('g_1', 'g_2', 'g_5', 'g_6')) and (ini_pos_matrix == desti_pos_matrix):
            if initial_pos[0] == desti[0]:
                if checked == 0:
                    if str(int(initial_pos[1:])-1) == desti[1:] or str(int(initial_pos[1:])-2) == desti[1:]:
                        return True
                    else:
                        return False
                elif checked != 0:
                    if str(int(initial_pos[1:])-1) == desti[1:]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif (ini_pos_matrix in ('g_3', 'g_4')) and (ini_pos_matrix == desti_pos_matrix):
            if initial_pos[0] == desti[0]:
                if str(int(initial_pos[1:])+1) == desti[1:]:
                    return True
                else:
                    return False
            else:
                return False
        elif (initial_pos[1] == '5')and((desti[1] == '4')or(desti[1] == '9')) and (initial_pos[0] == desti[0]):
            return True
        else:
            return False       
        
    elif color == 'g':
        if (ini_pos_matrix in ('g_1', 'g_2', 'g_3', 'g_4')) and (ini_pos_matrix == desti_pos_matrix):
            if initial_pos[0] != desti[0]:
                return False
            elif initial_pos[0] == desti[0]:
                if checked == 0:
                    if str(int(initial_pos[1:])-1) == desti[1:] or str(int(initial_pos[1:])-2) == desti[1:]:
                        return True
                    else:
                        return False
                elif checked != 0:
                    if str(int(initial_pos[1:])-1) == desti[1:]:
                        return True
                    else:
                        return False
                else:
                    return False
            

        elif (ini_pos_matrix in ('g_5', 'g_6')) and (ini_pos_matrix == desti_pos_matrix):
            if initial_pos[0] == desti[0]:
                if str(int(initial_pos[1:])+1) == desti[1:]:
                    return True
                else:
                    return False
            else:
                return False
        elif (initial_pos[1] == '9')and((desti[1] == '4')or(desti[1] == '5')) and (initial_pos[0] == desti[0]):
            return True
        else:
            return False
                
UPDATED = {}

def update():
    """To update"""   
    for key, value in STAR.items():
        for k, v in value.items():
            try:
                if v[0].isvisible() is True:
                    UPDATED[v[0]] = get_pos(v[0])
            except:
                if v.isvisible() is True:
                    UPDATED[v] = get_pos(v)

    return UPDATED       

def move(p, desti):
    """ p = 'b'+b #bR1"""
    if p[1] == "R":
        initial_pos = get_pos(STAR['R'][p][0])
        if initial_pos != desti and rook_validate(STAR['R'][p][0], initial_pos, desti):
            capture(desti)
            STAR['R'][p][0].setpos(SQUARE_DICT[desti]['centro'])
            STAR['R'][p][1]["checked"] += 1
            return True
        else:
            print("Error")
            return False
    if p[1] == "B":
        initial_pos = get_pos(STAR['B'][p])
        if initial_pos != desti and bishop_validate(STAR['B'][p], initial_pos, desti):
            capture(desti)
            STAR['B'][p].setpos(SQUARE_DICT[desti]['centro'])
            return True
        else:
            print("Error")
            return False
    if p[1] == "N":
        initial_pos = get_pos(STAR['N'][p])
        if initial_pos != desti and knight_validate(STAR['N'][p], initial_pos, desti):
            capture(desti)
            STAR['N'][p].setpos(SQUARE_DICT[desti]['centro'])
            return True
        else:
            print("Error")
            return False
    if p[1] == "K":
        initial_pos = get_pos(STAR['K'][p][0])
        if initial_pos != desti and king_validate(STAR['K'][p][0], initial_pos, desti):
            capture(desti)
            STAR['K'][p][0].setpos(SQUARE_DICT[desti]['centro'])
            STAR['K'][p][1]["checked"] += 1
            return True
        else:
            print("Error")
            return False
    if p[1] == "Q":
        initial_pos = get_pos(STAR['Q'][p])
        if initial_pos != desti and king_validate(STAR['Q'][p], initial_pos, desti):
            capture(desti)
            STAR['Q'][p].setpos(SQUARE_DICT[desti]['centro'])
            return True
        else:
            print("Error")
            return False
    if p[1] == "P":
        initial_pos = get_pos(STAR['P'][p][0])
        if initial_pos != desti and pawn_validate(p[0], p, initial_pos, desti):
            capture(desti)
            STAR['P'][p][0].setpos(SQUARE_DICT[desti]['centro'])
            STAR['P'][p][1]["checked"] += 1
            return True
        else:
            print("Error")
            return False

def validate_piece(piece):
    """To validate piece name input"""
    if piece in PIECES:
        return True
    else:
        print("Enter a valid piece tag")
        return False

def validate_desti(desti):
    """To validate destination input"""
    new = []
    for x in GROUPING.values():
        new = new+x
    if desti in new:
        return True
            
def capture(desti):
    """To captur"""
    for key, value in UPDATED.items():
        if value == desti:
            key.hideturtle()
            return True
ex = 'n'

def ask(p, con):
    """To ask"""
    piece = input("select piece ")
    if validate_piece(piece):
        desti = input('destination ')
        if validate_desti(desti):
            final_piece = p+piece
            if move(final_piece, desti) is False:
                con -= 1
            if p == 'g':
                ex = input('exit? ---> y/n')
        else:
            print("Please enter a valid destination")
            con -= 1
    else:
        con -= 1
    return con

def take_inputs():
    """To take user inputs"""
    con = 1
    while ex != 'y':
        update()
        if con%3 == 1 or con == 1:
            print("BLUE plays")
            con = ask('b', con)
        elif con%3 == 2 or con == 2:
            print("RED plays")
            con = ask('r', con)
        elif con%3 == 0:
            print("GREEN plays")
            con = ask('g', con)
        con += 1
    turtle.done()

class TestTrioChess(unittest.TestCase):
    """define multiple sets of tests as functions with names that begin"""

    def test_knight_validate(self):
        """To test knight_validate function"""
        self.assertEqual(knight_validate(BN1, 'G1', 'H3'), True)
        self.assertEqual(knight_validate(BN1, 'G1', 'F3'), True)
        self.assertEqual(knight_validate(BN1, 'F3', 'E1'), True)
        self.assertEqual(knight_validate(BN1, 'F3', 'H4'), True)
        self.assertEqual(knight_validate(BN1, 'G3', 'H1'), True)
        self.assertEqual(knight_validate(BN1, 'D2', 'B1'), True)
        self.assertEqual(knight_validate(BN1, 'B2', 'D1'), True)
        self.assertEqual(knight_validate(BN1, 'D2', 'B3'), True)
        self.assertEqual(knight_validate(BN1, 'G1', 'G3'), False)

    def test_queen_validate(self):
        """To test queen_validate function"""
        self.assertEqual(queen_validate(BQ, 'C1', 'A3'), True)
        self.assertEqual(queen_validate(BQ, 'D3', 'E9'), False)

    def test_bishop_validate(self):
        """To test bishop_validate function"""
        self.assertEqual(bishop_validate(BB1, 'C1', 'A3'), True)
        self.assertEqual(bishop_validate(BB1, 'C1', 'E3'), True)
        self.assertEqual(bishop_validate(BB1, 'C1', 'H10'), True)
        self.assertEqual(bishop_validate(BB1, 'E4', 'C2'), True)
        self.assertEqual(bishop_validate(BB1, 'E4', 'F3'), True)
        self.assertEqual(bishop_validate(BB1, 'E4', 'H11'), True)
        self.assertEqual(bishop_validate(BB1, 'E4', 'J10'), True)
        self.assertEqual(bishop_validate(BB1, 'E4', 'D5'), True)
        self.assertEqual(bishop_validate(BB1, 'E4', 'I5'), False)
        self.assertEqual(bishop_validate(BB1, 'E4', 'E3'), False)
        self.assertEqual(bishop_validate(BB1, 'E4', 'D4'), False)
        self.assertEqual(bishop_validate(BB1, 'B1', 'L7'), False)
        
    def test_blue_rooks_validate(self):
        """To test rook_validate function with blue"""
        self.assertEqual(rook_validate(BR1, 'A1', 'L12'), False)#False
        self.assertEqual(rook_validate(BR1, 'G10', 'H10'), True)#Back
        self.assertEqual(rook_validate(BR1, 'G10', 'G3'), True)#Left
        self.assertEqual(rook_validate(BR1, 'G10', 'G12'), True)#Right
        self.assertEqual(rook_validate(BR1, 'G10', 'I10'), True)#Front
        self.assertEqual(rook_validate(BR1, 'A4', 'D4'), True)#extreme COLUMN
        self.assertEqual(rook_validate(BR1, 'E1', 'E4'), True)#extreme ROW
        self.assertEqual(rook_validate(BR1, 'A4', 'H4'), True)
        self.assertEqual(rook_validate(BR1, 'A4', 'L9'), True)
        self.assertEqual(rook_validate(BR1, 'E1', 'I7'), True)
        self.assertEqual(rook_validate(BR1, 'E1', 'E11'), True)
        self.assertEqual(rook_validate(BR1, 'E4', 'E2'), True)
        self.assertEqual(rook_validate(BR1, 'E4', 'G4'), True)
        self.assertEqual(rook_validate(BR1, 'E4', 'B4'), True)
        self.assertEqual(rook_validate(BR1, 'E4', 'K5'), True)
        self.assertEqual(rook_validate(BR1, 'E4', 'I6'), True)
        self.assertEqual(rook_validate(BR1, 'E4', 'E10'), True)

    def test_king_validate_same_group(self):
        """validate the king moves in the same group 8 directions"""
        self.assertEqual(king_validate(BK, 'C3', 'C4'), True)#Front
        self.assertEqual(king_validate(BK, 'C3', 'C2'), True)#Back
        self.assertEqual(king_validate(BK, 'C3', 'B3'), True)#Left
        self.assertEqual(king_validate(BK, 'C3', 'D3'), True)#Right
        self.assertEqual(king_validate(BK, 'C3', 'B4'), True)#Front_Left
        self.assertEqual(king_validate(BK, 'C3', 'D4'), True)#Front_Right
        self.assertEqual(king_validate(BK, 'C3', 'B2'), True)#Back_Left
        self.assertEqual(king_validate(BK, 'C3', 'D2'), True)#Back_Right   
        self.assertEqual(king_validate(BK, 'C3', 'C5'), False)

    def test_king_validate_center_star(self):
        """In the star position in 10 dircetions"""
        self.assertEqual(king_validate(BK, 'D4', 'E4'), True)
        self.assertEqual(king_validate(BK, 'D4', 'E9'), True)
        self.assertEqual(king_validate(BK, 'D4', 'I9'), True)
        self.assertEqual(king_validate(BK, 'D4', 'I5'), True)
        self.assertEqual(king_validate(BK, 'D4', 'D5'), True)
        self.assertEqual(king_validate(BK, 'D4', 'C5'), True)
        self.assertEqual(king_validate(BK, 'D4', 'E3'), True)
        self.assertEqual(king_validate(BK, 'D4', 'C4'), True)
        self.assertEqual(king_validate(BK, 'D4', 'D3'), True)
        self.assertEqual(king_validate(BK, 'D4', 'C3'), True)
        self.assertEqual(king_validate(BK, 'K5', 'K9'), True)

    def test_king_validate_different_group(self):
        """validate the king moves in the different group 3 directions"""
        self.assertEqual(king_validate(BK, 'E11', 'I11'), True)#Right
        self.assertEqual(king_validate(BK, 'E11', 'I12'), True)#Front_Right
        self.assertEqual(king_validate(BK, 'E11', 'I10'), True)#Back_Right 
    
    def test_blue_pawn_validate(self):
        """To test pawn_validate function with blue"""
        self.assertEqual(pawn_validate('b', 'bP1', 'A2', 'A1'), False)#reverse
        self.assertEqual(pawn_validate('b', 'bP1', 'A2', 'A3'), True)#one step at the begining
        self.assertEqual(pawn_validate('b', 'bP1', 'A2', 'A4'), True)#two steps at the begining
        self.assertEqual(pawn_validate('b', 'bP1', 'A2', 'B3'), False)#diagonal
        self.assertEqual(pawn_validate('b', 'bP1', 'A4', 'A5'), True)#cross group
        self.assertEqual(pawn_validate('b', 'bP1', 'A4', 'B5'), False)#cross group diagonal
        self.assertEqual(pawn_validate('b', 'bP4', 'D4', 'D5'), True)#star
        self.assertEqual(pawn_validate('b', 'bP4', 'D4', 'I9'), True)#star diagonal
        self.assertEqual(pawn_validate('b', 'bP4', 'D4', 'E4'), False)#star False

    def test_red_pawn_validate(self):
        """To test pawn_validate function with red"""
        self.assertEqual(pawn_validate('r', 'rP1', 'L7', 'L8'), False)#reverse
        self.assertEqual(pawn_validate('r', 'rP1', 'L7', 'L6'), True)#one step at the begining
        self.assertEqual(pawn_validate('r', 'rP1', 'L7', 'L5'), True)#two steps at the begining
        self.assertEqual(pawn_validate('r', 'rP1', 'L7', 'K5'), False)#diagonal
        self.assertEqual(pawn_validate('r', 'rP1', 'L5', 'L9'), True)#cross group
        self.assertEqual(pawn_validate('r', 'rP1', 'L5', 'K9'), False)#cross group diagonal
        self.assertEqual(pawn_validate('r', 'rP4', 'I5', 'I9'), True)#star
        self.assertEqual(pawn_validate('r', 'rP4', 'I5', 'E4'), True)#star diagonal
        self.assertEqual(pawn_validate('r', 'rP4', 'I5', 'E9'), False)#star False
    
    def test_green_pawn_validate(self):
        """To test pawn_validate function with green"""
        self.assertEqual(pawn_validate('g', 'gP1', 'H11', 'H12'), False)#reverse
        self.assertEqual(pawn_validate('g', 'gP1', 'H11', 'H10'), True)#one step at the begining
        self.assertEqual(pawn_validate('g', 'gP1', 'H11', 'H9'), True)#two steps at the begining
        self.assertEqual(pawn_validate('g', 'gP1', 'H11', 'G9'), False)#diagonal
        self.assertEqual(pawn_validate('g', 'gP1', 'H9', 'H4'), True)#cross group
        self.assertEqual(pawn_validate('g', 'gP1', 'H9', 'G4'), False)#cross group diagonal
        self.assertEqual(pawn_validate('g', 'gP4', 'E9', 'E4'), True)#star
        self.assertEqual(pawn_validate('g', 'gP4', 'E9', 'D5'), True)#star diagonal
        self.assertEqual(pawn_validate('g', 'gP4', 'E9', 'I5'), False)#star False

if __name__ == '__main__':
    print('Running Trio Chess Game unit tests')
    unittest.main()
    take_inputs()