import turtle 
import math
from centroid import centroid

polygon = turtle.Turtle()
screen = turtle.Screen()

screen.addshape("rR1.gif")
screen.addshape("rR2.gif")
screen.addshape("rN1.gif")
screen.addshape("rN2.gif")
screen.addshape("rB1.gif")
screen.addshape("rB2.gif")
screen.addshape("rK.gif")
screen.addshape("rQ.gif")
screen.addshape("rP1.gif")
screen.addshape("rP2.gif")
screen.addshape("rP3.gif")
screen.addshape("rP4.gif")
screen.addshape("rP5.gif")
screen.addshape("rP6.gif")
screen.addshape("rP7.gif")
screen.addshape("rP8.gif")

screen.addshape("gR1.gif")
screen.addshape("gR2.gif")
screen.addshape("gN1.gif")
screen.addshape("gN2.gif")
screen.addshape("gB1.gif")
screen.addshape("gB2.gif")
screen.addshape("gK.gif")
screen.addshape("gQ.gif")
screen.addshape("gP1.gif")
screen.addshape("gP2.gif")
screen.addshape("gP3.gif")
screen.addshape("gP4.gif")
screen.addshape("gP5.gif")
screen.addshape("gP6.gif")
screen.addshape("gP7.gif")
screen.addshape("gP8.gif")

screen.addshape("bR1.gif")
screen.addshape("bR2.gif")
screen.addshape("bN1.gif")
screen.addshape("bN2.gif")
screen.addshape("bB1.gif")
screen.addshape("bB2.gif")
screen.addshape("bK.gif")
screen.addshape("bQ.gif")
screen.addshape("bP1.gif")
screen.addshape("bP2.gif")
screen.addshape("bP3.gif")
screen.addshape("bP4.gif")
screen.addshape("bP5.gif")
screen.addshape("bP6.gif")
screen.addshape("bP7.gif")
screen.addshape("bP8.gif")



polygon.speed(0) 
count = 0

def square(x, l):
    polygon.forward(x)
    polygon.right(90)
    p1 = polygon.pos()
    polygon.forward(l)
    polygon.right(120)
    p2 = polygon.pos()
    polygon.forward(l)
    polygon.right(90)
    p3 = polygon.pos()
    polygon.forward(x)
    polygon.right(60)
    p4 = polygon.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex)
    """ bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan") """
    sq={'centro': centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
    return sq


def square_2(l, x):
    p1 = polygon.pos()
    polygon.forward(x)
    p2 = polygon.pos()    
    polygon.right(90)
    polygon.forward(l)
    p3 = polygon.pos()
    polygon.right(90)
    polygon.forward(x)
    p4 = polygon.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex)
    """ bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan") """
    sq={'centro': centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
    return sq

def square_3(l, x):
    p1 = polygon.pos()
    polygon.backward(x)
    p2 = polygon.pos()    
    polygon.left(90)
    polygon.forward(l)
    p3 = polygon.pos()
    polygon.right(90)
    polygon.forward(x)
    p4 = polygon.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex)
    """ bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan") """
    sq={'centro': centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
    return sq

    
def alternate_color_1 (num):
    if num%2==0:
        polygon.fillcolor('black')
    else:
        polygon.fillcolor('white')

def alternate_color_2 (num):
    if num%2==0:
        polygon.fillcolor('white')
    else:
        polygon.fillcolor('black')

def user_input():
    y=input("enter destination ")
    bR1.goto(chaukon[y]['centro'])
    y=input("enter destination ")
    rR1.goto(chaukon[y]['centro'])
    y=input("enter destination ")
    gR1.goto(chaukon[y]['centro'])

x = 40
x_2 = 2*x
x_3 = 3*x
x_4 = 4*x
l = math.sqrt(((x*2)**2)-(x**2))
l_2 = math.sqrt(((x_2*2)**2)-(x_2**2))
l_3 = math.sqrt(((x_3*2)**2)-(x_3**2))
l_4 = math.sqrt(((x_4*2)**2)-(x_4**2))

polygon.setpos(-x*4, x*8)

row = dict
column = dict
group = dict

row = { "row_1": ("A","B","C","D"),
        "row_2": ("H","G","F","E"),
        "row_3": ("L","K","J","I")
        }

column = { "column_1" :("1","2","3","4"),
            "column_2" :("8","7","6","5"),
            "column_3" :("12","11","10","9")
        }

group_1 = row["row_3"], column["column_3"]
group_2 = column["column_3"], row["row_2"] 
group_3 = row["row_2"], column["column_1"]
group_4 =  column["column_1"], row["row_1"]
group_5 = row["row_1"], column["column_2"]
group_6 = column["column_2"], row["row_3"] 

naming = group_1, group_2, group_3, group_4, group_5, group_6
chaukon = {}

for i in range(6):

    polygon.forward(8*x)
    polygon.right(60)
    polygon.begin_fill()
    sq = square(x, l)
    alternate_color_1(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][0]+naming[i][0][0]] = sq 
    else:   
        chaukon[naming[i][0][0]+naming[i][1][0]] = sq
    print(count)
    print(naming[i][0][0],naming[i][1][0])
    print('\n')
   
    polygon.forward(x)

    polygon.begin_fill()
    sq = square_2(l_2/2, x)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][0]+naming[i][0][1]] = sq 
    else:   
        chaukon[naming[i][0][1]+naming[i][1][0]] = sq
    #chaukon[naming[i][0][1]+naming[i][1][0]] = sq
    print(count)
    print(naming[i][0][1],naming[i][1][0])
    print('\n')
    
    polygon.left(180)
    
    polygon.begin_fill()
    sq = square(x, l)
    alternate_color_1(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][1]+naming[i][0][1]] = sq 
    else:   
        chaukon[naming[i][0][1]+naming[i][1][1]] = sq
    print(count)
    print(naming[i][0][1]+naming[i][1][1])
    print('\n')


    polygon.begin_fill()
    polygon.right(120)
    sq = square_2(l_2/2, x)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][1]+naming[i][0][0]] = sq 
    else:   
        chaukon[naming[i][0][0]+naming[i][1][1]] = sq
    print(count)
    print(naming[i][0][0],naming[i][1][1])
    print('\n')

    polygon.forward(x)
    polygon.right(60)
    polygon.forward(2*x)

    polygon.begin_fill()
    sq = square_2(l_3/3, x)
    alternate_color_1(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][0]+naming[i][0][2]] = sq 
    else:   
        chaukon[naming[i][0][2]+naming[i][1][0]] = sq
    print(count)
    print(naming[i][0][2],naming[i][1][0])
    print('\n')
    polygon.begin_fill()
    sq = square_3(l_3/3, x)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][1]+naming[i][0][2]] = sq 
    else:   
        chaukon[naming[i][0][2]+naming[i][1][1]] = sq
    print(count)
    print(naming[i][0][2],naming[i][1][1])
    print('\n')    
    polygon.backward(x)
    polygon.left(90) 

    polygon.begin_fill()
    p1 = polygon.pos()
    polygon.forward(l_3/3)
    p2 = polygon.pos()
    polygon.right(120)
    polygon.forward(l_3/3)
    p3 = polygon.pos()
    polygon.right(90)
    polygon.forward(x)
    p4 = polygon.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex)
    """ bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan") """
    alternate_color_1(i)
    sq={'centro':centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][2]+naming[i][0][2]] = sq 
    else:   
        chaukon[naming[i][0][2]+naming[i][1][2]] = sq
    print(naming[i][0][2],naming[i][1][2])
    print('\n')
    polygon.begin_fill()
    sq = square_3(l_3/3, x)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][2]+naming[i][0][1]] = sq 
    else:   
        chaukon[naming[i][0][1]+naming[i][1][2]] = sq
    print(count)
    print(naming[i][0][1],naming[i][1][2])
    print('\n')
    polygon.begin_fill()
    sq = square_3(l_3/3, x)
    alternate_color_1(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][2]+naming[i][0][0]] = sq 
    else:   
        chaukon[naming[i][0][0]+naming[i][1][2]] = sq
    print(count)
    print(naming[i][0][0],naming[i][1][2])
    print('\n')
    polygon.forward(x*2)
    polygon.right(60)
    polygon.forward(x*3)

    polygon.begin_fill()
    sq = square_2(l_4/4, x)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][0]+naming[i][0][3]] = sq 
    else:   
        chaukon[naming[i][0][3]+naming[i][1][0]] = sq
    print(count)
    print(naming[i][0][3],naming[i][1][0])
    print('\n')
    polygon.begin_fill()
    sq = square_3(l_4/4, x)
    alternate_color_1(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][1]+naming[i][0][3]] = sq 
    else:   
        chaukon[naming[i][0][3]+naming[i][1][1]] = sq
    print(naming[i][0][3],naming[i][1][1])
    print('\n')
    polygon.begin_fill()
    sq = square_3(l_4/4, x)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][2]+naming[i][0][3]] = sq 
    else:   
        chaukon[naming[i][0][3]+naming[i][1][2]] = sq
    print(count)
    print(naming[i][0][3],naming[i][1][2])
    print('\n')
    polygon.backward(x)
    polygon.left(90)

    polygon.begin_fill()
    p1 = polygon.pos()
    polygon.forward(l_4/4)
    p2 = polygon.pos()
    polygon.right(120)
    polygon.forward(l_4/4)
    p3 = polygon.pos()
    polygon.right(90)
    polygon.forward(x)
    p4 = polygon.pos()
    vertex = (p1, p2, p3, p4)
    centro = centroid(vertex)
    """ bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan") """
    alternate_color_1(i)
    sq={'centro':centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][3]+naming[i][0][3]] = sq 
    else:   
        chaukon[naming[i][0][3]+naming[i][1][3]] = sq
    print(count)
    print(naming[i][0][3],naming[i][1][3])
    print('\n')
    polygon.begin_fill()
    sq = square_3(l_4/4, x)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][3]+naming[i][0][2]] = sq 
    else:   
        chaukon[naming[i][0][2]+naming[i][1][3]] = sq
    print(count)
    print(naming[i][0][2],naming[i][1][3])
    print('\n')
    polygon.begin_fill()
    sq = square_3(l_4/4, x)
    alternate_color_1(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][3]+naming[i][0][1]] = sq 
    else:   
        chaukon[naming[i][0][1]+naming[i][1][3]] = sq
    print(count)
    print(naming[i][0][1],naming[i][1][3])
    print('\n')
    polygon.begin_fill()
    sq = square_3(l_4/4, x)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    if i%2 != 0:
        chaukon[naming[i][1][3]+naming[i][0][0]] = sq 
    else:   
        chaukon[naming[i][0][0]+naming[i][1][3]] = sq
    print(count)
    print(naming[i][0][0],naming[i][1][3])
    print('\n')
    polygon.forward(x*3)
    polygon.right(60)

print("count", count)
print(chaukon)
#---------------------BLUE
bR1 = turtle.Turtle()
bN1 = turtle.Turtle()
bB1 = turtle.Turtle()
bQ = turtle.Turtle()
bK = turtle.Turtle()
bB2 = turtle.Turtle()
bN2 = turtle.Turtle()
bR2 = turtle.Turtle()
bP1 = turtle.Turtle()
bP2 = turtle.Turtle()
bP3 = turtle.Turtle()
bP4 = turtle.Turtle()
bP5 = turtle.Turtle()
bP6 = turtle.Turtle()
bP7 = turtle.Turtle()
bP8 = turtle.Turtle()
#---------------RED
rR1 = turtle.Turtle()
rN1 = turtle.Turtle()
rB1 = turtle.Turtle()
rQ = turtle.Turtle()
rK = turtle.Turtle()
rB2 = turtle.Turtle()
rN2 = turtle.Turtle()
rR2 = turtle.Turtle()
rP1 = turtle.Turtle()
rP2 = turtle.Turtle()
rP3 = turtle.Turtle()
rP4 = turtle.Turtle()
rP5 = turtle.Turtle()
rP6 = turtle.Turtle()
rP7 = turtle.Turtle()
rP8 = turtle.Turtle()
#----------------GREEN
gR1 = turtle.Turtle()
gN1 = turtle.Turtle()
gB1 = turtle.Turtle()
gQ = turtle.Turtle()
gK = turtle.Turtle()
gB2 = turtle.Turtle()
gN2 = turtle.Turtle()
gR2 = turtle.Turtle()
gP1 = turtle.Turtle()
gP2 = turtle.Turtle()
gP3 = turtle.Turtle()
gP4 = turtle.Turtle()
gP5 = turtle.Turtle()
gP6 = turtle.Turtle()
gP7 = turtle.Turtle()
gP8 = turtle.Turtle()

blue = [bR1, bN1, bB1, bQ, bK, bB2, bN2, bR2, bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8]
red = [rR1, rN1, rB1, rQ, rK, rB2, rN2, rR2, rP1, rP2, rP3, rP4, rP5, rP6, rP7, rP8]
green = [gR1, gN1, gB1, gQ, gK, gB2, gN2, gR2, gP1, gP2, gP3, gP4, gP5, gP6, gP7, gP8]
blue_desti = ['A1', 'B1','C1','D1','E1','F1','G1','H1','A2','B2','C2','D2','E2','F2','G2','H2']
red_desti=['L8','K8','J8','I8','D8','C8','B8','A8','L7','K7','J7','I7','D7','C7','B7','A7']
green_desti=['H12','G12','F12','E12','I12','J12','K12','L12','H11','G11','F11','E11','I11','J11','K11','L11']
pices = ['R1', 'N1', 'B1', 'Q', 'K', 'B2', 'N2', 'R2', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']
blue_str = ['bR1', 'bN1', 'bB1', 'bQ', 'bK', 'bB2', 'bN2', 'bR2', 'bP1', 'bP2', 'bP3', 'bP4', 'bP5', 'bP6', 'bP7', 'bP8']
red_str = ['rR1', 'rN1', 'rB1', 'rQ', 'rK', 'rB2', 'rN2', 'rR2', 'rP1', 'rP2', 'rP3', 'rP4', 'rP5', 'rP6', 'rP7', 'rP8']
green_str = ['gR1', 'gN1', 'gB1', 'gQ', 'gK', 'gB2', 'gN2', 'gR2', 'gP1', 'gP2', 'gP3', 'gP4', 'gP5', 'gP6', 'gP7', 'gP8']

def start_pos(clr,destination, gif):
    for piece, desti, pic in zip(clr, destination, gif):
        piece.shape(pic +'.gif')
        piece.penup()
        piece.setpos(chaukon[desti]['centro'])

start_pos(blue, blue_desti, blue_str)
start_pos(red, red_desti, red_str)
start_pos(green, green_desti, green_str)
print("---------------", chaukon)

def move(x,y,clr, gif):
    for piece, pic in zip(clr, gif):
        if x == pic:
            piece.setpos(chaukon[y]['centro'])



con = 1
ex = 0
while ex!='y':
#------------Blue

    if con%3==1 or con==1:
        print("Blue plays")
        b=input("select piece")
        bb=input('destination')
        p='b'+b
        move(p, bb,blue, blue_str)
    elif con%3==2 or con==2:
        print("Red plays")
        b=input("select piece")
        bb=input('destination')
        p='r'+b
        move(p, bb,red, red_str)
    elif con%3==0:
        print("Green plays")
        b=input("select piece")
        bb=input('destination')
        p='g'+b
        move(p, bb,green, green_str)
        ex = input('exit? ---> y/n')
    con+=1

user_input()
turtle.done() 
