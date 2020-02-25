import turtle 
import math
polygon = turtle.Turtle()
polygon.speed(0) 
#side_length = 70
def hexagon(side_length):
    num_sides = 6
    polygon.left(90) 
    polygon.forward(math.sqrt((side_length**2)-((side_length/2)**2))) 
    polygon.right(90)
    polygon.forward(side_length/2) 

    angle = 360.0 / num_sides 
    for i in range(num_sides-1):
        polygon.right(angle)  
        polygon.forward(side_length)

    polygon.right(angle)
    polygon.forward(side_length/2) 
    polygon.goto(0,0)


hexagon(20)  
hexagon(40) 
hexagon(60) 
hexagon(80) 


polygon.left(30)
side_length = 80
for i in range(6):
    polygon.forward(math.sqrt((side_length**2)-((side_length/2)**2)))
    polygon.back(math.sqrt((side_length**2)-((side_length/2)**2)))
    polygon.left(60)

polygon.left(150)
polygon.penup()
polygon.forward(80)
polygon.right(120)
polygon.pendown()

def square(length):
    polygon.forward(length)
    polygon.right(90)
    polygon.forward(math.sqrt(((length*2)**2)-(length**2)))
    polygon.right(120)
    polygon.forward(math.sqrt(((length*2)**2)-(length**2)))
    polygon.right(90)
    polygon.forward(length)
    polygon.right(60)
    

""" square(10)
square(20)
square(30)
square(40) """

for i in range(6):
    polygon.forward(80)
    polygon.right(60)
    polygon.begin_fill()
    square(10)
    if i%2==0:
        polygon.fillcolor('black')
    else:
        polygon.fillcolor('white')
    polygon.end_fill()
    #square(20)
    l=math.sqrt(((20*2)**2)-(20**2))
    polygon.forward(10)
    polygon.begin_fill()
    polygon.forward(10)
    polygon.right(90)
    polygon.forward(l/2)
    polygon.right(90)
    polygon.forward(10)
    if i%2==0:
        polygon.fillcolor('white')
        """ bp1 = turtle.Turtle()
        bp1.penup()
        print(polygon.xcor(), polygon.ycor())
        bp1.setpos(polygon.xcor(), polygon.ycor()) """
    else:
        polygon.fillcolor('black')
    """ bp1.color("blue") """
    polygon.end_fill()
    polygon.backward(10)
    polygon.left(90)
    polygon.begin_fill()
    polygon.forward(l/2)
    polygon.right(120)
    polygon.forward(l/2)
    """ bp2 = turtle.Turtle()
    bp2.penup()
    print("x1", polygon.xcor(), polygon.ycor())
    bp2.setpos(polygon.xcor(), polygon.ycor()) 
    """
    polygon.right(90)
    polygon.fd(10) 
    if i%2==0:
        polygon.fillcolor('black')
         
        
    else:
        polygon.fillcolor('white')
    polygon.end_fill()
    """ bp2.color("blue") """
    polygon.begin_fill()
    polygon.backward(10)
    polygon.left(90)
    polygon.forward(l/2)
    polygon.right(90)
    polygon.forward(10)
    if i%2==0:
        polygon.fillcolor('white')
    else:
        polygon.fillcolor('black')
    polygon.end_fill()
    polygon.forward(10)
    polygon.right(60)
    polygon.forward(20)
    l_3 = math.sqrt(((30*2)**2)-(30**2))
   
    polygon.begin_fill()
    polygon.forward(10)
    polygon.right(90)
    
    polygon.forward(l_3/3)
    polygon.right(90)
    polygon.forward(10)
    if i%2==0:
        polygon.fillcolor('black')
    else:
        polygon.fillcolor('white')
    polygon.end_fill()
    polygon.begin_fill()
    polygon.backward(10)
    polygon.left(90)

    polygon.forward(l_3/3)
    polygon.right(90)
    polygon.forward(10)
    if i%2==0:
        polygon.fillcolor('white')
    else:
        polygon.fillcolor('black')
    polygon.end_fill()
    polygon.backward(10)
    polygon.left(90)
    
    polygon.begin_fill()
    polygon.forward(l_3/3)
    polygon.right(120)
    polygon.forward(l_3/3)
    polygon.right(90)
    polygon.forward(10)
    if i%2==0:
        polygon.fillcolor('black')
    else:
        polygon.fillcolor('white')
    polygon.end_fill()
    polygon.begin_fill()
    polygon.backward(10)
    polygon.left(90)
    
    polygon.forward(l_3/3)
    polygon.right(90)
    polygon.forward(10)
    if i%2==0:
        polygon.fillcolor('white')
        """bp3 = turtle.Turtle()
        bp3.penup()
        print(polygon.xcor(), polygon.ycor())
        bp3.setpos(polygon.xcor(), polygon.ycor()) """
    
    else:
        polygon.fillcolor('black')
    """ bp3.color('blue') """
    polygon.end_fill()
    polygon.begin_fill()
    polygon.backward(10)

    polygon.left(90)
    polygon.forward(l_3/3)
    polygon.right(90)
    if i%2==0:
        polygon.fillcolor('black')
    else:
        polygon.fillcolor('white')
    polygon.forward(10)
    polygon.end_fill()
    polygon.forward(20)
    polygon.right(60)

    polygon.forward(30)
    l_4 = math.sqrt(((40*2)**2)-(40**2))
   
    polygon.begin_fill()
    polygon.forward(10)
    polygon.right(90)
    
    polygon.forward(l_4/4)
    polygon.right(90)
    polygon.forward(10)
    if i%2==0:
        polygon.fillcolor('white')
    else:
        polygon.fillcolor('black')
    polygon.end_fill()

    polygon.begin_fill()
    polygon.backward(10)
    polygon.left(90)

    polygon.forward(l_4/4)
    polygon.right(90)
    polygon.forward(10)
    if i%2==0:
        polygon.fillcolor('black')
    else:
        polygon.fillcolor('white')
    polygon.end_fill()

    polygon.begin_fill()
    polygon.backward(10)
    polygon.left(90)

    polygon.forward(l_4/4)
    polygon.right(90)
    polygon.forward(10)
    if i%2==0:
        polygon.fillcolor('white')
    else:
        polygon.fillcolor('black')
    polygon.end_fill()

    polygon.backward(10)
    polygon.left(90)
    
    polygon.begin_fill()
    polygon.forward(l_4/4)
    polygon.right(120)
    polygon.forward(l_4/4)
    polygon.right(90)
    polygon.forward(10)
    if i%2==0:
        polygon.fillcolor('black')
    else:
        polygon.fillcolor('white')
    polygon.end_fill()
    polygon.begin_fill()
    polygon.backward(10)
    polygon.left(90)
    
    polygon.forward(l_4/4)
    polygon.right(90)
    polygon.forward(10)
    if i%2==0:
        polygon.fillcolor('white')
    else:
        polygon.fillcolor('black')
    polygon.end_fill()
    polygon.begin_fill()
    polygon.backward(10)

    polygon.left(90)
    polygon.forward(l_4/4)
    polygon.right(90)
    if i%2==0:
        polygon.fillcolor('black')
    else:
        polygon.fillcolor('white')
    polygon.forward(10)
    polygon.end_fill()
    polygon.begin_fill()
    polygon.backward(10)

    polygon.left(90)
    polygon.forward(l_4/4)
    polygon.right(90)
    if i%2==0:
        polygon.fillcolor('white')
    else:
        polygon.fillcolor('black')
    polygon.forward(10)
    polygon.end_fill()
    polygon.forward(30)
    polygon.right(60)



""" bp1 = turtle.Turtle()
bp1.penup()
bp1.shape("circle")
bp1.color("red")
bp1.setpos(-50, -20) """

turtle.done() 
