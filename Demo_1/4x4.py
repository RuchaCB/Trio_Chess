import turtle
from b_4x4 import draw_box, draw_chess_board

draw_chess_board()

bp1 = turtle.Turtle()
bp1.setpos(15, -15)
bp1.left(90)
bp1.color("cyan")
bp1.penup()

bp2 = turtle.Turtle()
bp2.penup()
bp2.setpos(105, 75)
bp2.right(90)
bp2.color("red")

turn = "cyan"
y = 9
while y==9:
    if turn == "cyan":
        x = int(input("Enter 1, 2 or 3 for Cyan"))
        if x == 1:
            bp1.forward(30)
        elif x == 2:
            bp1.forward(60) 
        else:
            bp1.right(45)
            bp1.forward(42.42)
            bp1.left(45)
        turn = "red"

    if turn == "red":
        x = int(input("Enter 1, 2 or 3 for Red"))
        if x == 1:
            bp2.forward(30)
        elif x == 2:
            bp2.forward(60) 
        else:
            bp2.right(45)
            bp2.forward(42.42)
            bp2.left(45)
        turn = "cyan"

    y = int(input("Enter 0 to exit 9 to continue"))
    if y == 0:
        print("Thank you")
        turtle.done()



turtle.done()