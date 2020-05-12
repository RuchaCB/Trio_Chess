"""
Trio_Chess Trial
Author: Rucha_CB
"""
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

def square(side, length):
    POLYGON.forward(side)
    POLYGON.right(90)
    p1 = POLYGON.pos()
    POLYGON.forward(length)
    POLYGON.right(120)
    p2 = POLYGON.pos()
    POLYGON.forward(length)
    POLYGON.right(90)
    p3 = POLYGON.pos()
    POLYGON.forward(side)
    POLYGON.right(60)
    p4 = POLYGON.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex) #being called from centroid.py
    sq = {'centro': centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    return sq


def square_2(length, side):
    p1 = POLYGON.pos()
    POLYGON.forward(side)
    p2 = POLYGON.pos()
    POLYGON.right(90)
    POLYGON.forward(length)
    p3 = POLYGON.pos()
    POLYGON.right(90)
    POLYGON.forward(side)
    p4 = POLYGON.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex)
    sq = {'centro': centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    return sq

def square_3(length, side):
    p1 = POLYGON.pos()
    POLYGON.backward(side)
    p2 = POLYGON.pos()
    POLYGON.left(90)
    POLYGON.forward(length)
    p3 = POLYGON.pos()
    POLYGON.right(90)
    POLYGON.forward(side)
    p4 = POLYGON.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex)
    sq = {'centro': centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    return sq

def alternate_color_1(num):
    if num%2 == 0:
        POLYGON.fillcolor('white')
    else:
        POLYGON.fillcolor('black')

def alternate_color_2(num):
    if num%2 == 0:
        POLYGON.fillcolor('black')
    else:
        POLYGON.fillcolor('white')


side = 40 #changing side will change the size of board
side_2 = 2*side
side_3 = 3*side
side_4 = 4*side
length = math.sqrt(((side*2)**2)-(side**2))
length_2 = math.sqrt(((side_2*2)**2)-(side_2**2))
length_3 = math.sqrt(((side_3*2)**2)-(side_3**2))
length_4 = math.sqrt(((side_4*2)**2)-(side_4**2))

POLYGON.setpos(-side*4, side*8)

row = dict
column = dict
group = dict

row = {"row_1": ("A", "B", "C", "D"),
       "row_2": ("H", "G", "F", "E"),
       "row_3": ("L", "K", "J", "I")
      }

column = {"column_1" :("1", "2", "3", "4"),
          "column_2" :("8", "7", "6", "5"),
          "column_3" :("12", "11", "10", "9")
         }

extreme_row = ('E', 'D', 'I')
extreme_column = ('4', '5', '9')

matrix_1 = []
matrix_2 = []
matrix_3 = []
matrix_4 = []
matrix_5 = []
matrix_6 = []

grouping = {}

for x in row["row_3"]:
    for y in column["column_3"]:
        matrix_1.append(x+y)
grouping["g_1"] = matrix_1

for x in row["row_2"]:
    for y in column["column_3"]:
        matrix_2.append(x+y)
grouping["g_2"] = matrix_2

for x in row["row_2"]:
    for y in column["column_1"]:
        matrix_3.append(x+y)
grouping["g_3"] = matrix_3

for x in row["row_1"]:
    for y in column["column_1"]:
        matrix_4.append(x+y)
grouping["g_4"] = matrix_4

for x in row["row_1"]:
    for y in column["column_2"]:
        matrix_5.append(x+y)
grouping["g_5"] = matrix_5

for x in row["row_3"]:
    for y in column["column_2"]:
        matrix_6.append(x+y)
grouping["g_6"] = matrix_6

group_1 = row["row_3"], column["column_3"]
group_1_star = "I9"
group_2 = column["column_3"], row["row_2"]
group_2_star = "E9"
group_3 = row["row_2"], column["column_1"]
group_3_star = "E4"
group_4 = column["column_1"], row["row_1"]
group_4_star = "D4"
group_5 = row["row_1"], column["column_2"]
group_5_star = "D5"
group_6 = column["column_2"], row["row_3"]
group_6_star = "I5"

star_squares = {"g_1":"I9", "g_2":"E9", "g_3":"E4", "g_4":"D4", "g_5":"D5", "g_6":"I5"}

for_rook = {"g_1":"g_4", "g_2":"g_5", "g_3":"g_6", "g_4":"g_1", "g_5":"g_2", "g_6":"g_3"}

for_bishop_row_1 = ["A", "B", "C", "D", "E", "F", "G", "H"]
for_bishop_row_2 = ["H", "G", "F", "E", "I", "J", "K", "L"]
for_bishop_row_3 = ["L", "K", "J", "I", "D", "C", "B", "A"]
for_bishop_column_1 = ["1", "2", "3", "4", "9", "10", "11", "12"]
for_bishop_column_2 = ["12", "11", "10", "9", "5", "6", "7", "8"]
for_bishop_column_3 = ["8", "7", "6", "5", "4", "3", "2", "1"]

for_bishop = {
    ("g_2", "g_3", "g_4"):(for_bishop_row_1, for_bishop_column_1),
    ("g_3", "g_4", "g_5"):(for_bishop_row_1, for_bishop_column_3),
    ("g_1", "g_2", "g_3"):(for_bishop_row_2, for_bishop_column_1),
    ("g_1", "g_2", "g_6"):(for_bishop_row_2, for_bishop_column_2),
    ("g_1", "g_5", "g_6"):(for_bishop_row_3, for_bishop_column_2),
    ("g_4", "g_5", "g_6"):(for_bishop_row_3, for_bishop_column_3)
}

naming = group_1, group_2, group_3, group_4, group_5, group_6
square_dict = {}

for i in range(6):

    POLYGON.forward(8*side)
    POLYGON.right(60)
    POLYGON.begin_fill()
    sq = square(side, length)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][0]+naming[i][0][0]] = sq
    else:
        square_dict[naming[i][0][0]+naming[i][1][0]] = sq

    POLYGON.forward(side)

    POLYGON.begin_fill()
    sq = square_2(length_2/2, side)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][0]+naming[i][0][1]] = sq
    else:
        square_dict[naming[i][0][1]+naming[i][1][0]] = sq

    POLYGON.left(180)

    POLYGON.begin_fill()
    sq = square(side, length)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][1]+naming[i][0][1]] = sq
    else:
        square_dict[naming[i][0][1]+naming[i][1][1]] = sq

    POLYGON.begin_fill()
    POLYGON.right(120)
    sq = square_2(length_2/2, side)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][1]+naming[i][0][0]] = sq
    else:
        square_dict[naming[i][0][0]+naming[i][1][1]] = sq

    POLYGON.forward(side)
    POLYGON.right(60)
    POLYGON.forward(2*side)

    POLYGON.begin_fill()
    sq = square_2(length_3/3, side)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][0]+naming[i][0][2]] = sq
    else:
        square_dict[naming[i][0][2]+naming[i][1][0]] = sq

    POLYGON.begin_fill()
    sq = square_3(length_3/3, side)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][1]+naming[i][0][2]] = sq
    else:
        square_dict[naming[i][0][2]+naming[i][1][1]] = sq

    POLYGON.backward(side)
    POLYGON.left(90)

    POLYGON.begin_fill()
    p1 = POLYGON.pos()
    POLYGON.forward(length_3/3)
    p2 = POLYGON.pos()
    POLYGON.right(120)
    POLYGON.forward(length_3/3)
    p3 = POLYGON.pos()
    POLYGON.right(90)
    POLYGON.forward(side)
    p4 = POLYGON.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex)

    alternate_color_1(i)
    sq = {'centro':centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}

    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][2]+naming[i][0][2]] = sq
    else:
        square_dict[naming[i][0][2]+naming[i][1][2]] = sq

    POLYGON.begin_fill()
    sq = square_3(length_3/3, side)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][2]+naming[i][0][1]] = sq
    else:
        square_dict[naming[i][0][1]+naming[i][1][2]] = sq

    POLYGON.begin_fill()
    sq = square_3(length_3/3, side)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][2]+naming[i][0][0]] = sq
    else:
        square_dict[naming[i][0][0]+naming[i][1][2]] = sq

    POLYGON.forward(side*2)
    POLYGON.right(60)
    POLYGON.forward(side*3)

    POLYGON.begin_fill()
    sq = square_2(length_4/4, side)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][0]+naming[i][0][3]] = sq
    else:
        square_dict[naming[i][0][3]+naming[i][1][0]] = sq

    POLYGON.begin_fill()
    sq = square_3(length_4/4, side)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][1]+naming[i][0][3]] = sq
    else:
        square_dict[naming[i][0][3]+naming[i][1][1]] = sq

    POLYGON.begin_fill()
    sq = square_3(length_4/4, side)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][2]+naming[i][0][3]] = sq
    else:
        square_dict[naming[i][0][3]+naming[i][1][2]] = sq

    POLYGON.backward(side)
    POLYGON.left(90)

    POLYGON.begin_fill()
    p1 = POLYGON.pos()
    POLYGON.forward(length_4/4)
    p2 = POLYGON.pos()
    POLYGON.right(120)
    POLYGON.forward(length_4/4)
    p3 = POLYGON.pos()
    POLYGON.right(90)
    POLYGON.forward(side)
    p4 = POLYGON.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex)
    alternate_color_1(i)
    sq = {'centro':centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][3]+naming[i][0][3]] = sq
    else:
        square_dict[naming[i][0][3]+naming[i][1][3]] = sq

    POLYGON.begin_fill()
    sq = square_3(length_4/4, side)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][3]+naming[i][0][2]] = sq
    else:
        square_dict[naming[i][0][2]+naming[i][1][3]] = sq

    POLYGON.begin_fill()
    sq = square_3(length_4/4, side)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][3]+naming[i][0][1]] = sq
    else:
        square_dict[naming[i][0][1]+naming[i][1][3]] = sq

    POLYGON.begin_fill()
    sq = square_3(length_4/4, side)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][3]+naming[i][0][0]] = sq
    else:
        square_dict[naming[i][0][0]+naming[i][1][3]] = sq

    POLYGON.forward(side*3)
    POLYGON.right(60)

star = {"R":{"bR1":(BR1, {"checked":0}), "bR2":(BR2, {"checked":0}),
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
        piece.setpos(square_dict[desti]['centro'])

start_pos(BLUE, BLUE_DESTI, BLUE_STR)
start_pos(RED, RED_DESTI, RED_STR)
start_pos(GREEN, GREEN_DESTI, GREEN_STR)

def get_pos(piece):
    """takes piece and returns its location by terating throuh square_dict"""
    loc = piece.pos()
    for key, value in square_dict.items():
        if value['centro'] == loc:
            return key

def rook_validate(piece, initial_pos, desti):
    """validates the rook moves"""
    #step_1: get matrix of initial pos
    #step_2: get matrix of desti pos
    #step_3: get the star position of initial matrix
    #step_4: get the star position of destination matrix
    #step_5: get star combo according to piece type and initial matrix ka star position
    for key, value in grouping.items():
        if initial_pos in value:
            ini_pos_matrix = key
        if desti in value:
            desti_pos_matrix = key

    if for_rook[ini_pos_matrix] == desti_pos_matrix:
        if (initial_pos[1:] in extreme_column) and (desti[1:] in extreme_column):
            return True
        elif (initial_pos[0] in extreme_row) and (desti[0] in extreme_row):
            return True
        else:
            return False

    if initial_pos[0] == desti[0]:
        return True
    elif initial_pos[1:] == desti[1:]:
        return True
    else:
        return False

def triangle(orignal_row, column):
    row = orignal_row[:]
    triangle = []
    for i in column:
        row.pop(0)
        row.pop(-1)
        for j in row:
            try:
                int(j)
                triangle.append(i+j)
            except:
                triangle.append(j+i)
    return tuple(triangle)

triangle_61 = triangle(for_bishop_column_2, row['row_3'])
triangle_34 = triangle(for_bishop_row_1, column['column_1'])

triangle_45 = triangle(for_bishop_column_3, row['row_1'])
triangle_12 = triangle(for_bishop_row_2, column['column_3'])

triangle_56 = triangle(for_bishop_row_3, column['column_2'])
triangle_23 = triangle(for_bishop_column_1, row['row_2'])

triangles = {
    triangle_61:triangle_34,
    triangle_45:triangle_12,
    triangle_56:triangle_23
    }

def bishop_validate(piece, initial_pos, desti):
    """validates the rook moves"""
    for key, value in grouping.items():
        if initial_pos in value:
            ini_pos_matrix = key #g_1,g_2,
        if desti in value:
            desti_pos_matrix = key #g_1,g_2

    for key, value in triangles.items():
        if (initial_pos in key) and (desti in value) or (initial_pos in value) and (desti in key):
            return False
    for key, value in for_bishop.items():
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
    elif (initial_pos[0] in extreme_row) and (desti[0] in extreme_row) and ((int(initial_pos[1]) == int(desti[1]))or(int(initial_pos[1])+1 == int(desti[1]))or(int(initial_pos[1])-1 == int(desti[1]))):
        return True
    elif (initial_pos[1] in extreme_column) and (desti[1] in extreme_column) and ((ord(initial_pos[0]) == ord(desti[0]))or(ord(initial_pos[0])+1 == int(ord(desti[0])))or(ord(initial_pos[0])-1 == int(ord(desti[0])))):
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
    """ for i in i_ini_pos_1:
        if rook_validate(piece, initial_pos, i)==True:
            initial_pos_02 = i[0]+str(int(i[1:])+2)
            initial_pos_0_2 = i[0]+str(int(i[1:])-2)
            new_ini_pos_2 = (initial_pos_02, initial_pos_0_2)
            for j in new_ini_pos_2:
                if rook_validate(piece, i, j )==True:
                    if j == desti:
                        return True
    for i in i_ini_pos_2:
        if rook_validate(piece, initial_pos, i )==True:
            initial_pos_20 = chr(ord(i[0])+2)+i[1:]
            initial_pos__20 = chr(ord(i[0])-2)+i[1:]
            new_ini_pos_2 =  (initial_pos_20, initial_pos__20)
            for j in new_ini_pos_2:
                if rook_validate(piece, i, j )==True:
                    if j == desti:
                        return True
    return False """

for_pawn = ('E4', 'E9'), ('E4', 'I5'), ('E9', 'D5'), ('I9', 'I5'), ('I9', 'D4'), ('D5', 'D4')
def pawn_validate(color, piece, initial_pos, desti):
    """validates the pawn moves"""
    for tup in for_pawn:
        if (initial_pos in tup)and (desti in tup):
            return True

    checked = star['P'][piece][1]["checked"]

    for key, value in grouping.items():
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
                
updated = {}

def update():   
    for key, value in star.items():
        for k, v in value.items():
            try:
                if v[0].isvisible() is True:
                    updated[v[0]] = get_pos(v[0])
            except:
                if v.isvisible() is True:
                    updated[v] = get_pos(v)

    return updated       

def move(p, desti):
    """ p = 'b'+b #bR1"""
    if p[1] == "R":
        initial_pos = get_pos(star['R'][p][0])
        if initial_pos != desti and rook_validate(star['R'][p][0], initial_pos, desti):
            capture(desti)
            star['R'][p][0].setpos(square_dict[desti]['centro'])
            star['R'][p][1]["checked"] += 1
            return True
        else:
            print("Error")
            return False
    if p[1] == "B":
        initial_pos = get_pos(star['B'][p])
        if initial_pos != desti and bishop_validate(star['B'][p], initial_pos, desti):
            capture(desti)
            star['B'][p].setpos(square_dict[desti]['centro'])
            return True
        else:
            print("Error")
            return False
    if p[1] == "N":
        initial_pos = get_pos(star['N'][p])
        if initial_pos != desti and knight_validate(star['N'][p], initial_pos, desti):
            capture(desti)
            star['N'][p].setpos(square_dict[desti]['centro'])
            return True
        else:
            print("Error")
            return False
    if p[1] == "K":
        initial_pos = get_pos(star['K'][p][0])
        if initial_pos != desti and king_validate(star['K'][p][0], initial_pos, desti):
            capture(desti)
            star['K'][p][0].setpos(square_dict[desti]['centro'])
            star['K'][p][1]["checked"] += 1
            return True
        else:
            print("Error")
            return False
    if p[1] == "Q":
        initial_pos = get_pos(star['Q'][p])
        if initial_pos != desti and king_validate(star['Q'][p], initial_pos, desti):
            capture(desti)
            star['Q'][p].setpos(square_dict[desti]['centro'])
            return True
        else:
            print("Error")
            return False
    if p[1] == "P":
        initial_pos = get_pos(star['P'][p][0])
        if initial_pos != desti and pawn_validate(p[0], p, initial_pos, desti):
            capture(desti)
            star['P'][p][0].setpos(square_dict[desti]['centro'])
            star['P'][p][1]["checked"] += 1
            return True
        else:
            print("Error")
            return False

def validate_piece(piece):
    if piece in PIECES:
        return True
    else:
        print("Enter a valid piece tag")
        return False

def validate_desti(desti):
    new = []
    for x in grouping.values():
        new = new+x
    if desti in new:
        return True
            
def capture(desti):
    for key, value in updated.items():
        if value == desti:
            key.hideturtle()
            return True

def take_inputs():
    con = 1
    ex = 'n'
    while ex != 'y':
        update()
        if con%3 == 1 or con == 1:
            print("BLUE plays")
            piece = input("select piece ")#R1.....R2
            if validate_piece(piece):
                desti = input('destination ')#H4
                if validate_desti(desti):
                    p = 'b'
                    FINAL_PIECE = p+piece
                    if move(FINAL_PIECE, desti) is False:
                        con -= 1
                else:
                    print("Please enter a valid destination")
                    con -= 1
            else:
                con -= 1
        elif con%3 == 2 or con == 2:
            print("RED plays")
            piece = input("select piece ")
            if validate_piece(piece):
                desti = input('destination ')
                if validate_desti(desti):
                    p = 'r'
                    FINAL_PIECE = p+piece
                    if move(FINAL_PIECE, desti) is False:
                        con -= 1
                else:
                    print("Please enter a valid destination")
                    con -= 1
            else:
                con -= 1
            
        elif con%3 == 0:
            print("GREEN plays")
            piece = input("select piece ")
            if validate_piece(piece):
                desti = input('destination ')
                if validate_desti(desti):
                    p = 'g'
                    FINAL_PIECE = p+piece
                    if move(FINAL_PIECE, desti) is False:
                        con -= 1
                    ex = input('exit? ---> y/n')
                else:
                    print("Please enter a valid destination")
                    con -= 1
            else:
                con -= 1
        con += 1
    turtle.done()

import unittest

class TestTrioChess(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test_queen_validate(self):
        self.assertEqual(queen_validate(BB1, 'C1', 'A3'), True)

    def test_bishop_validate(self):
        self.assertEqual(bishop_validate(BB1, 'C1', 'A3'), True)
        
    def test_blue_rooks_validate(self):
        self.assertEqual(rook_validate(BR1, 'A1', 'L12'), False)#False
        self.assertEqual(rook_validate(BR1, 'G10', 'H10'), True)#Back
        self.assertEqual(rook_validate(BR1, 'G10', 'G3'), True)#Left
        self.assertEqual(rook_validate(BR1, 'G10', 'G12'), True)#Right
        self.assertEqual(rook_validate(BR1, 'G10', 'I10'), True)#Front

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

    def test_king_validate_different_group(self):
        """validate the king moves in the different group 3 directions"""
        self.assertEqual(king_validate(BK, 'E11', 'I11'), True)#Right
        self.assertEqual(king_validate(BK, 'E11', 'I12'), True)#Front_Right
        self.assertEqual(king_validate(BK, 'E11', 'I10'), True)#Back_Right 
    
    def test_blue_pawn_validate(self):
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