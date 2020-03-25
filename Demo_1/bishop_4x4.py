import turtle
from b_4x4 import draw_box, draw_chess_board

draw_chess_board()

bp1 = turtle.Turtle()
bp1.setpos(15, -15)
bp1.left(90)
bp1.color("cyan")
bp1.shape("triangle")
bp1.penup()

bp2 = turtle.Turtle()
bp2.penup()
bp2.setpos(105, 75)
bp2.right(90)
bp2.color("red")
bp2.shape("triangle")

turn = "cyan"
y = 9
while y==9:
    if turn == "cyan":
        z = int(input("Enter number of blocks for Cyan Bishop"))
        x = int(input("Enter 1, 2, 3, 4 for Cyan"))
        if x == 1:
            bp1.left(45)
            bp1.forward(z*42.42)
            bp1.right(45)
        elif x == 2:
            bp1.right(45) 
            bp1.forward(z*42.42)
            bp1.left(45) 
        elif x == 3:
            bp1.right(135)
            bp1.forward(z*42.42)
            bp1.left(135) 
        else:
            bp1.left(135)
            bp1.forward(z*42.42)
            bp1.right(135)

        turn = "red"

    if turn == "red":
        z = int(input("Enter number of blocks for Red Bishop"))
        x = int(input("Enter 1, 2, 3, 4 for Red"))
        if x == 1:
            bp2.left(45)
            bp2.forward(z*42.42)
            bp2.right(45)
        elif x == 2:
            bp2.right(45) 
            bp2.forward(z*42.42)
            bp2.left(45) 
        elif x == 3:
            bp2.right(135)
            bp2.forward(z*42.42)
            bp2.left(135) 
        else:
            bp2.left(135)
            bp2.forward(z*42.42)
            bp2.right(135)
        turn = "cyan"

    y = int(input("Enter 0 to exit 9 to continue"))
    if y == 0:
        print("Thank you")
        turtle.done()



turtle.done()