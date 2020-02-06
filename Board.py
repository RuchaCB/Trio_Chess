import turtle 
import math
polygon = turtle.Turtle() 
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

turtle.done() 

