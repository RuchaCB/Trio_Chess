import turtle
from b_4x4 import draw_box, draw_chess_board

draw_chess_board()

bp1 = turtle.Turtle()
bp1.setpos(15, -15)
bp1.left(90)
bp1.color("cyan")
bp1.penup()
bp1.shape("circle")

bp2 = turtle.Turtle()
bp2.penup()
bp2.setpos(105, 75)
bp2.right(90)
bp2.color("red")
bp2.shape("circle")

turn = "cyan"
y = 9
while y==9:
    if turn == "cyan":
        z = int(input("Enter number of blocks for Cyan Rook"))
        x = int(input("Enter 1, 2, 3, 4 for Cyan"))
        if x == 1:
            bp1.forward(z*30)
        elif x == 2:
            bp1.right(90) 
            bp1.forward(z*30)
            bp1.left(90) 
        elif x == 3:
            bp1.backward(z*30)
        else:
            bp1.left(90)
            bp1.forward(z*30)
            bp1.right(90)

        turn = "red"

    if turn == "red":
        z = int(input("Enter number of blocks for Red Rook"))
        x = int(input("Enter 1, 2, 3, 4 for Red"))
        if x == 1:
            bp2.forward(z*30)
        elif x == 2:
            bp2.right(90) 
            bp2.forward(z*30)
            bp2.left(90) 
        elif x == 3:
            bp2.backward(z*30)
        else:
            bp2.left(90)
            bp2.forward(z*30)
            bp2.right(90)
        turn = "cyan"

    y = int(input("Enter 0 to exit 9 to continue"))
    if y == 0:
        print("Thank you")
        turtle.done()



turtle.done()