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
pawn = turtle.Turtle()
pawn.setpos(15, -15)
pawn.left(90)
pawn.pencolor("cyan")
pawn.penup()

x = int(input("Enter 1, 2 or 3"))
if x == 1:
    pawn.forward(30)
elif x == 2:
    pawn.forward(60) 
else:
    pawn.right(45)
    pawn.forward(42.42)
    pawn.left(45)



turtle.done()
