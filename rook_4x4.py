import turtle
 
def draw_box(t,x,y,size,fill_color):
    t.penup() # no drawing!
    t.goto(x,y) # move the pen to a different position
    t.pendown() # resume drawing
 
    t.fillcolor(fill_color)
    t.begin_fill()  # Shape drawn after this will be filled with this color!
 
    for i in range(0,4):
        board.forward(size) # move forward
        board.right(90) # turn pen right 90 degrees
 
    t.end_fill() # Go ahead and fill the rectangle!
 
 
def draw_chess_board():
    square_color = "black" # first chess board square is black
    start_x = 0 # starting x position of the chess board
    start_y = 0 # starting y position of the chess board
    box_size = 30 # pixel size of each square in the chess board
    for i in range(0,4): # 8x8 chess board
        for j in range(0,4):
            draw_box(board,start_x+j*box_size,start_y+i*box_size,box_size,square_color)
            square_color = 'black' if square_color == 'white' else 'white' # toggle after a column
        square_color = 'black' if square_color == 'white' else 'white' # toggle after a row!
 

board = turtle.Turtle()
board.hideturtle()
#board.register_shape('player.png')
board.speed(0)
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