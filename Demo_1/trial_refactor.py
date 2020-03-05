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
    centro = centroid(vertex)
    bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan")
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')


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
    bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan")
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
    return centro

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
    bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan")
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
    return centro

    
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

x = 10
x_2 = 2*x
x_3 = 3*x
x_4 = 4*x
l = math.sqrt(((x*2)**2)-(x**2))
l_2=math.sqrt(((x_2*2)**2)-(x_2**2))
l_3 = math.sqrt(((x_3*2)**2)-(x_3**2))
l_4 = math.sqrt(((x_4*2)**2)-(x_4**2))

for i in range(6):

    polygon.forward(80)
    polygon.right(60)
    polygon.begin_fill()
    square(x, l)
    alternate_color_1(i)
    polygon.end_fill()
    count += 1
    print(count)

    polygon.forward(10)

    polygon.begin_fill()
    square_2(l_2/2)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    print(count)

    polygon.left(180)
    
    polygon.begin_fill()
    square(x, l)
    alternate_color_1(i)
    polygon.end_fill()
    count += 1
    print(count)

    polygon.begin_fill()
    polygon.right(120)
    square_2(l_2/2)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    print(count)

    polygon.forward(10)
    polygon.right(60)
    polygon.forward(20)

    polygon.begin_fill()
    square_2(l_3/3)
    alternate_color_1(i)
    polygon.end_fill()
    count += 1
    print(count)

    polygon.begin_fill()
    square_3(l_3/3)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    print(count)
    
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
    bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan")
    alternate_color_1(i)
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
    polygon.end_fill()
    count += 1
    print(count)

    polygon.begin_fill()
    square_3(l_3/3)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    print(count)

    polygon.begin_fill()
    square_3(l_3/3)
    alternate_color_1(i)
    polygon.end_fill()
    count += 1
    print(count)

    polygon.forward(20)
    polygon.right(60)
    polygon.forward(30)

    polygon.begin_fill()
    square_2(l_4/4)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    print(count)

    polygon.begin_fill()
    square_3(l_4/4)
    alternate_color_1(i)
    polygon.end_fill()
    count += 1
    print(count)

    polygon.begin_fill()
    square_3(l_4/4)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    print(count)

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
    bp1 = turtle.Turtle()
    bp1.penup()
    bp1.setpos(centro)
    bp1.color("cyan")
    alternate_color_1(i)
    print(f'centro {centro} p1 {p1} p2 {p2} p3 {p3} p4 {p4}')
    polygon.end_fill()
    count += 1
    print(count)

    polygon.begin_fill()
    square_3(l_4/4)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    print(count)

    polygon.begin_fill()
    square_3(l_4/4)
    alternate_color_1(i)
    polygon.end_fill()
    count += 1
    print(count)

    polygon.begin_fill()
    square_3(l_4/4)
    alternate_color_2(i)
    polygon.end_fill()
    count += 1
    print(count)

    polygon.forward(30)
    polygon.right(60)

print("count", count)
turtle.done() 
