import turtle
import math
from centroid import centroid

polygon = turtle.Turtle()
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
    centro = 0
    centro = centroid(vertex)
    """ bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan") """
    sq={'centro': centro, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
    return sq


def square_2(l):
    p1 = polygon.pos()
    polygon.forward(10)
    p2 = polygon.pos()    
    polygon.right(90)
    polygon.forward(l)
    p3 = polygon.pos()
    polygon.right(90)
    polygon.forward(10)
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

def square_3(l):
    p1 = polygon.pos()
    polygon.backward(10)
    p2 = polygon.pos()    
    polygon.left(90)
    polygon.forward(l)
    p3 = polygon.pos()
    polygon.right(90)
    polygon.forward(10)
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
    cR1.goto(chaukon[y]['centro'])
    y=input("enter destination ")
    rR1.goto(chaukon[y]['centro'])
    y=input("enter destination ")
    gR1.goto(chaukon[y]['centro'])

x = 10
x_2 = 2*x
x_3 = 3*x
x_4 = 4*x
l = math.sqrt(((x*2)**2)-(x**2))
l_2 = math.sqrt(((x_2*2)**2)-(x_2**2))
l_3 = math.sqrt(((x_3*2)**2)-(x_3**2))
l_4 = math.sqrt(((x_4*2)**2)-(x_4**2))

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

    polygon.forward(80)
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
   
    polygon.forward(10)

    polygon.begin_fill()
    sq = square_2(l_2/2)
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
    sq = square_2(l_2/2)
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

    polygon.forward(10)
    polygon.right(60)
    polygon.forward(20)

    polygon.begin_fill()
    sq = square_2(l_3/3)
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
    sq = square_3(l_3/3)
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
    polygon.backward(10)
    polygon.left(90) 

    polygon.begin_fill()
    p1 = polygon.pos()
    polygon.forward(l_3/3)
    p2 = polygon.pos()
    polygon.right(120)
    polygon.forward(l_3/3)
    p3 = polygon.pos()
    polygon.right(90)
    polygon.forward(10)
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
    sq = square_3(l_3/3)
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
    sq = square_3(l_3/3)
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
    polygon.forward(20)
    polygon.right(60)
    polygon.forward(30)

    polygon.begin_fill()
    sq = square_2(l_4/4)
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
    sq = square_3(l_4/4)
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
    sq = square_3(l_4/4)
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
    polygon.backward(10)
    polygon.left(90)

    polygon.begin_fill()
    p1 = polygon.pos()
    polygon.forward(l_4/4)
    p2 = polygon.pos()
    polygon.right(120)
    polygon.forward(l_4/4)
    p3 = polygon.pos()
    polygon.right(90)
    polygon.forward(10)
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
    sq = square_3(l_4/4)
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
    sq = square_3(l_4/4)
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
    sq = square_3(l_4/4)
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
    polygon.forward(30)
    polygon.right(60)

print("count", count)

print(chaukon)
print(chaukon['H1']['centro'])
cR1 = turtle.Turtle()
cR1.penup()
cR1.setpos(chaukon['H1']['centro'])
cR1.color("cyan")#Rook

print(chaukon['A1']['centro'])
cR2 = turtle.Turtle()
cR2.penup()
cR2.setpos(chaukon['A1']['centro'])
cR2.color("cyan")#Rook

print(chaukon['L8']['centro'])
rR1 = turtle.Turtle()
rR1.penup()
rR1.setpos(chaukon['L8']['centro'])
rR1.color("red")#Rook

print(chaukon['A8']['centro'])
rR2 = turtle.Turtle()
rR2.penup()
rR2.setpos(chaukon['A8']['centro'])
rR2.color("red")#Rook

print(chaukon['L12']['centro'])
gR1 = turtle.Turtle()
gR1.penup()
gR1.setpos(chaukon['L12']['centro'])
gR1.color("green")#Rook

print(chaukon['H1']['centro'])
gR2 = turtle.Turtle()
gR2.penup()
gR2.setpos(chaukon['H12']['centro'])
gR2.color("green")#Rook
user_input()
turtle.done()
