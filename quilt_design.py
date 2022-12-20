import math
import turtle

"""
  Initialize for drawing the patterns.  (-15, -25) is in the lower left and
  (750, 250) is in the upper right.
  :pre: pos (-15,-25), heading (east), down
  :post: pos (-15,-25), heading (east), up
  :return: None
  """
turtle.setup(700, 200)
turtle.setworldcoordinates(-15, -25, 750, 250)

"""
  Draw Rectangular blocks at 4 corners
  :pre: (relative) pos (0,0), heading (east), pen down
  :post: (relative) pos (10,190), heading (south), pen down
  """


def draw_rectangularBlocks():
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.penup()
    turtle.forward(200)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.penup()
    turtle.forward(200)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(10)

    """
  Draw  first Triangle.
  :pre: (relative) pos (100,100), heading (east), pen down
  :post: (relative) pos (100,100), heading (north), pen down
"""


def draw_triangle1(length1=80):
    x = length1 / math.sqrt(2)
    turtle.forward(length1)
    turtle.left(135)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.right(135)


"""
  Draw Second Triangle .
  :pre: (relative) pos (100,100), heading (north), pen down
  :post: (relative) pos (100,190), heading (south), pen down
   """


def draw_triangle2(length1=30):
    y = length1 / 2
    turtle.penup()
    turtle.right(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(length1 + y)
    turtle.left(180)
    turtle.pendown()


"""
  Draw Quilt Patterns
  :pre: pos (-15, -25), heading (east), pen down
  :post: pos (570, 110 ), heading (south), pen down
  """


def main():
    turtle.penup()
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.pendown()
    turtle.color("black")


"""
 To Draw the Rectangular Blocks at all 4 corners
  :pre: pos (0, 0), heading (east), pen down
  :post: pos (100, 190), heading (north), pen down
  """

draw_rectangularBlocks()

"""
 To Draw Pattern for block 1, i.e., Windmill
  :pre: pos (100, 190), heading (north), pen down
  :post: pos (100, 100 ), heading (south), pen down
  """
turtle.penup()
turtle.right(180)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.pendown()

for x in range(4):
    turtle.fillcolor("red")
    turtle.begin_fill()
    draw_triangle1()
    turtle.right(180)
    turtle.end_fill()
turtle.left(45)

for x in range(4):
    turtle.fillcolor("purple")
    turtle.begin_fill()
    draw_triangle1(40 * (math.sqrt(2)))
    turtle.end_fill()
turtle.right(45)

"""
 To Draw the rectangular blocks at all 4 corners for block 2
  :pre: pos (220, 0), heading (south), pen down
  :post: pos (230, 190 ), heading (north), pen down
  """

turtle.penup()
turtle.right(180)
turtle.forward(100)
turtle.left(90)
turtle.forward(120)
turtle.pendown()
draw_rectangularBlocks()

"""
To Draw Pattern for block 2, i.e., Triangles
  :pre: pos (230, 190), heading (north), pen down
  :post: pos (200, 30  ), heading (west), pen down
  """
turtle.fillcolor("blue")
turtle.penup()
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.right(180)
turtle.forward(120)
turtle.left(90)
turtle.forward(30)
turtle.pendown()
for i in range(4):
    turtle.begin_fill()
    draw_triangle1(60)
    turtle.end_fill()
    draw_triangle2(60)
turtle.fillcolor("yellow")
turtle.penup()
turtle.right(90)
turtle.forward(30)
turtle.left(90)
turtle.pendown()
turtle.begin_fill()
draw_triangle1(60)
turtle.end_fill()
for i in range(3):
    turtle.fillcolor("yellow")
    turtle.penup()
    turtle.forward(120)
    turtle.left(180)
    turtle.pendown()
    turtle.begin_fill()
    draw_triangle1(60)
    turtle.end_fill()

"""
 To Draw the rectangular blocks on all 4 corners for block 3
  :pre: pos (380, 30), heading (west), pen down
  :post: pos (450, 190 ), heading (north), pen down
  """

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(70)
turtle.pendown()
draw_rectangularBlocks()
"""
 To Draw 4 circles inside the square border
  :pre: pos (450, 180), heading (south), pen down
  :post: pos (450, 180 ), heading (west), pen down
    """
turtle.penup()
turtle.right(180)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.pendown()
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.fillcolor("grey")
turtle.begin_fill()
turtle.left(90)
turtle.right(180)
turtle.circle(20)
turtle.end_fill()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.left(180)
turtle.circle(20)
turtle.end_fill()
turtle.left(90)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.done()

