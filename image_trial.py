import turtle
#from Turtle import addshape 

screen = turtle.Screen()
pawn1 = turtle.Turtle()
pawn2 = turtle.Turtle()
pawn3 = turtle.Turtle()
pawn4 = turtle.Turtle()
pawn5 = turtle.Turtle()
pawn6 = turtle.Turtle()
pawn7 = turtle.Turtle()
pawn8 = turtle.Turtle()

# click the image icon in the top right of the code window to see
# which images are available in this trinket
image = "big_hex_b.gif"
p = "Pawn.gif"
screen.bgpic(image)
pawn1.shape("circle")
pawn1.color("white")
pawn2.shape("square")
pawn2.color("white")
pawn3.shape("arrow")
pawn3.color("white")
pawn4.shape("turtle")
pawn4.color("white")
pawn5.shape("classic")
pawn5.color("white")
pawn6.shape("circle")
pawn6.color("white")
pawn7.shape("circle")
pawn7.color("white")
pawn8.shape("circle")
pawn8.color("white")
pawn1.setpos(50,50)
pawn2.setpos(-50,50)
pawn3.setpos(50,-50)
pawn4.setpos(-50,-50)
pawn5.setpos(70,70)
pawn6.setpos(70,-70)
pawn7.setpos(-70,70)
pawn8.setpos(-70,-70)
#screen.screensize(2000,2000)
#(400, 300)
# add the shape first then set the turtle shape
#screen.addshape(image)
#pawn.shape(image)
turtle.done()

