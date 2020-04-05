"""
Trio_Chess Trial
Author: Rucha_CB
"""

import turtle
import math
from centroid import centroid

"""the turtle that draws board"""
POLYGON = turtle.Turtle()

"""to add images"""
SCREEN = turtle.Screen()

"""Blue Pieces"""
BR1 = turtle.Turtle()
BN1 = turtle.Turtle()
BB1 = turtle.Turtle()
BQ = turtle.Turtle()
BK = turtle.Turtle()
BB2 = turtle.Turtle()
BN2 = turtle.Turtle()
BR2 = turtle.Turtle()
BP1 = turtle.Turtle()
BP2 = turtle.Turtle()
BP3 = turtle.Turtle()
BP4 = turtle.Turtle()
BP5 = turtle.Turtle()
BP6 = turtle.Turtle()
BP7 = turtle.Turtle()
BP8 = turtle.Turtle()
"""Red Pieces"""
RR1 = turtle.Turtle()
RN1 = turtle.Turtle()
RB1 = turtle.Turtle()
RQ = turtle.Turtle()
RK = turtle.Turtle()
RB2 = turtle.Turtle()
RN2 = turtle.Turtle()
RR2 = turtle.Turtle()
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

"""Destinations where the pices will be added at the beginig of the game"""
BLUE_DESTI = ['E4', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
              'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'
             ]
RED_DESTI = ['D4', 'K8', 'J8', 'I8', 'D8', 'C8', 'B8', 'A8',
             'L7', 'K7', 'J7', 'I7', 'D7', 'C7', 'B7', 'A7'
            ]
GREEN_DESTI = ['I9', 'G12', 'F12', 'E12', 'I12', 'J12', 'K12', 'L12',
               'H11', 'G11', 'F11', 'E11', 'I11', 'J11', 'K11', 'L11'
              ]

"""Lists defined for adding GIFs the images are stored as ex. bR1.gif"""
BLUE_STR = ['bR1', 'bN1', 'bB1', 'bQ', 'bK', 'bB2', 'bN2', 'bR2',
            'bP1', 'bP2', 'bP3', 'bP4', 'bP5', 'bP6', 'bP7', 'bP8'
           ]
RED_STR = ['rR1', 'rN1', 'rB1', 'rQ', 'rK', 'rB2', 'rN2', 'rR2',
           'rP1', 'rP2', 'rP3', 'rP4', 'rP5', 'rP6', 'rP7', 'rP8'
          ]
GREEN_STR = ['gR1', 'gN1', 'gB1', 'gQ', 'gK', 'gB2', 'gN2', 'gR2',
             'gP1', 'gP2', 'gP3', 'gP4', 'gP5', 'gP6', 'gP7', 'gP8'
            ]

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
    """ bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan") """
    sq = {'centro': centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
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
    """ bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan") """
    sq = {'centro': centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
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
    """ bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan") """
    sq = {'centro': centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
    return sq

def alternate_color_1(num):
    if num%2 == 0:
        POLYGON.fillcolor('black')
    else:
        POLYGON.fillcolor('white')

def alternate_color_2(num):
    if num%2 == 0:
        POLYGON.fillcolor('white')
    else:
        POLYGON.fillcolor('black')

def user_input():
    y = input("enter destination ")
    BR1.goto(square_dict[y]['centro'])
    y = input("enter destination ")
    RR1.goto(square_dict[y]['centro'])
    y = input("enter destination ")
    GR1.goto(square_dict[y]['centro'])

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

group_1 = row["row_3"], column["column_3"]
group_2 = column["column_3"], row["row_2"]
group_3 = row["row_2"], column["column_1"]
group_4 = column["column_1"], row["row_1"]
group_5 = row["row_1"], column["column_2"]
group_6 = column["column_2"], row["row_3"]

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
    print(COUNT)
    print(naming[i][0][0], naming[i][1][0])
    print('\n')

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
    #square_dict[naming[i][0][1]+naming[i][1][0]] = sq
    print(COUNT)
    print(naming[i][0][1], naming[i][1][0])
    print('\n')

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
    print(COUNT)
    print(naming[i][0][1], naming[i][1][1])
    print('\n')


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
    print(COUNT)
    print(naming[i][0][0], naming[i][1][1])
    print('\n')

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
    print(COUNT)
    print(naming[i][0][2], naming[i][1][0])
    print('\n')
    POLYGON.begin_fill()
    sq = square_3(length_3/3, side)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][1]+naming[i][0][2]] = sq
    else:
        square_dict[naming[i][0][2]+naming[i][1][1]] = sq
    print(COUNT)
    print(naming[i][0][2], naming[i][1][1])
    print('\n')
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
    """ bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan") """
    alternate_color_1(i)
    sq = {'centro':centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][2]+naming[i][0][2]] = sq
    else:
        square_dict[naming[i][0][2]+naming[i][1][2]] = sq
    print(naming[i][0][2], naming[i][1][2])
    print('\n')
    POLYGON.begin_fill()
    sq = square_3(length_3/3, side)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][2]+naming[i][0][1]] = sq
    else:
        square_dict[naming[i][0][1]+naming[i][1][2]] = sq
    print(COUNT)
    print(naming[i][0][1], naming[i][1][2])
    print('\n')
    POLYGON.begin_fill()
    sq = square_3(length_3/3, side)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][2]+naming[i][0][0]] = sq
    else:
        square_dict[naming[i][0][0]+naming[i][1][2]] = sq
    print(COUNT)
    print(naming[i][0][0], naming[i][1][2])
    print('\n')
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
    print(COUNT)
    print(naming[i][0][3], naming[i][1][0])
    print('\n')
    POLYGON.begin_fill()
    sq = square_3(length_4/4, side)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][1]+naming[i][0][3]] = sq
    else:
        square_dict[naming[i][0][3]+naming[i][1][1]] = sq
    print(naming[i][0][3], naming[i][1][1])
    print('\n')
    POLYGON.begin_fill()
    sq = square_3(length_4/4, side)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][2]+naming[i][0][3]] = sq
    else:
        square_dict[naming[i][0][3]+naming[i][1][2]] = sq
    print(COUNT)
    print(naming[i][0][3], naming[i][1][2])
    print('\n')
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
    """ bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan") """
    alternate_color_1(i)
    sq = {'centro':centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][3]+naming[i][0][3]] = sq
    else:
        square_dict[naming[i][0][3]+naming[i][1][3]] = sq
    print(COUNT)
    print(naming[i][0][3], naming[i][1][3])
    print('\n')
    POLYGON.begin_fill()
    sq = square_3(length_4/4, side)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][3]+naming[i][0][2]] = sq
    else:
        square_dict[naming[i][0][2]+naming[i][1][3]] = sq
    print(COUNT)
    print(naming[i][0][2], naming[i][1][3])
    print('\n')
    POLYGON.begin_fill()
    sq = square_3(length_4/4, side)
    alternate_color_1(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][3]+naming[i][0][1]] = sq
    else:
        square_dict[naming[i][0][1]+naming[i][1][3]] = sq
    print(COUNT)
    print(naming[i][0][1], naming[i][1][3])
    print('\n')
    POLYGON.begin_fill()
    sq = square_3(length_4/4, side)
    alternate_color_2(i)
    POLYGON.end_fill()
    COUNT += 1
    if i%2 != 0:
        square_dict[naming[i][1][3]+naming[i][0][0]] = sq
    else:
        square_dict[naming[i][0][0]+naming[i][1][3]] = sq
    print(COUNT)
    print(naming[i][0][0], naming[i][1][3])
    print('\n')
    POLYGON.forward(side*3)
    POLYGON.right(60)

print("COUNT", COUNT)
print(square_dict)
#---------------------BLUE

def start_pos(clr, destination, gif):
    """starting position of the pieces"""
    for piece, desti, pic in zip(clr, destination, gif):
        piece.shape(pic +'.gif')
        piece.penup()
        piece.setpos(square_dict[desti]['centro'])

start_pos(BLUE, BLUE_DESTI, BLUE_STR)
start_pos(RED, RED_DESTI, RED_STR)
start_pos(GREEN, GREEN_DESTI, GREEN_STR)
print("---------------", square_dict)

def rook_validate(piece, desti):
    """validates the rook moves"""
    loc = piece.pos()
    for key, value in square_dict.items():
        if value['centro'] == (loc):
            print("1111111111111111",key[0],desti[0])
            print("22222222222",key[1],desti[1])
            if key[0] == desti[0]:
                print("1111111111111111",key[0],desti[0])
                return True
            elif key[1:] == desti[1:]:
                print("22222222222",key[1:],desti[1:])
                return True
            else:
                print("Haddd")
                return False
    print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
     
def bishop_validate():
    """validates the bishop moves"""
def knight_validate():
    """validates the knight moves"""

def queen_validate():
    """validates the queen moves"""

def king_validate():
    """validates the king moves"""

def pawn_validate():
    """validates the pawn moves"""
    


def move(user_input, desti, clr, gif):
    #print('user_input++++++++++++++++++++++++++++++++++++++++++', user_input)
    for piece, pic in zip(clr, PIECES):
        if "R1" or "R2" in user_input:
            if rook_validate(piece, desti)==True:
                piece.setpos(square_dict[desti]['centro'])
                break
            else:
                print("input AGAIN")
            break
        """ if "B1" or "B2" in user_input:
            bishop_validate()
        if "N1" or "N2" in user_input:
            knight_validate()
        if "Q" in user_input:
            queen_validate()
        if "K" in user_input:
            king_validate()
        if "P" in user_input:
            pawn_validate() """

con = 1
ex = 0
while ex != 'y':

    if con%3 == 1 or con == 1:
        print("BLUE plays")
        b = input("select piece")#R1.....R2
        bb = input('destination')#bR1
        p = 'b'+b
        move(p, bb, BLUE, BLUE_STR)
    elif con%3 == 2 or con == 2:
        print("RED plays")
        b = input("select piece")
        bb = input('destination')
        p = 'r'+b
        move(p, bb, RED, RED_STR)
    elif con%3 == 0:
        print("GREEN plays")
        b = input("select piece")
        bb = input('destination')
        p = 'g'+b
        move(p, bb, GREEN, GREEN_STR)
        ex = input('exit? ---> y/n')
    con += 1

user_input()
turtle.done()
