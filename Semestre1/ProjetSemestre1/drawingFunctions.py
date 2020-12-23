'''
Fichier contenant toutes les fonctions permettant de dessiner des formes
'''

from turtle import *
from math import sqrt, sin, radians

def va(x, y, turtleDrawing):
	'''
	-----------
	Description
	-----------
	This function is used to go from the actual position (A) of the turtle,
	to a point B(x, y), without leaving a line on the canva.
	
	----------
	Parameters
	----------
	x : integer / float
		Abscissa of the target.
	y : integer / float
		Ordinate of the target.
	turtleDrawing : class 'turtle.Turtle'
		The turtle going from point A to point B(x,y).
		
	-------
	Returns
	-------
	None.

	'''
	
	turtleDrawing.up()
	turtleDrawing.goto(x, y)
	turtleDrawing.down()

def draw_star(x, y, length, shapeColor, turtleDrawing):
	'''
	-----------
	Description
	-----------
	Function used to make a specified turtle draw a star filled with a certain color.
	
	----------
	Parameters
	----------
	x : integer / float
		Abscissa of the point at the end of the first branch drawn.
	y : integer / float
		Ordinate of the point at the end of the first branch drawn.
	length : integer / float
		Length of one arm of the star.
	shapeColor : string / tuple
		Color used by the turtle to draw the star.
	turtleDrawing : class 'turtle.Turtle'
		Turtle used to draw the star.

	-------
	Returns
	-------
	None.
	
	'''

	# --- Initialize the position and color of the turtle --- #
	va(x, y, turtleDrawing)
	turtleDrawing.color(shapeColor)

	# --- Start drawing --- #
	turtleDrawing.begin_fill()

	turtleDrawing.setheading(36)
	for loop in range(5):
		turtleDrawing.forward(length)
		turtleDrawing.right(72)
		turtleDrawing.forward(length)
		turtleDrawing.left(144)

	turtleDrawing.end_fill()
	# --- End drawing --- #

def draw_oval(centerX, centerY, length, cornersize, shapeColor, turtleDrawing):
	'''
	-----------
	Description
	-----------
	Function to make a specified turtle draw an oval in a certain color.
	
	----------
	Parameters
	----------
	centerX : integer / float
		Abscissa of the center of the oval.
	centerY : integer / float
		Ordinate of the center of the oval.
	length : integer / float
		Length of the straight part of the oval.
	diameter : integer / float
		Width of the oval determined as the diameter of the circle used to make the round part.
	shapeColor : string / tuple
		Color used by the turtle to draw the outline of the oval.
	turtleDrawing : class 'turtle.Turtle'
		Turtle used to draw the oval.
		
	-------
	Returns
	-------
	None.
	
	'''
	
	# --- Initialize the position, orientation and color of the turtle --- #
	turtleDrawing.setheading(270)
	turtleDrawing.color(shapeColor)
	va(centerX - diameter, centerY - length/2, turtleDrawing)

	# --- Start drawing --- #
	turtleDrawing.circle(diameter, 180)
	turtleDrawing.fd(length)
	turtleDrawing.circle(diameter, 180)
	turtleDrawing.fd(length)
	# --- End drawing --- #

def draw_rectangle(length, width, shapeColor, turtleDrawing):
	'''
	-----------
	Description
	-----------
	Function to make a specified turtle draw a rectangle filled with a certain color.    

	----------
	Parameters
	----------
	length : integer / float
		Lenght of the longest side the rectangle.
	width : TYPE
		Lenght of the shortest side the rectangle.
	shapeColor : string / tuple
		Color used by the turtle to fill the rectangle.
	turtleDrawing : class 'turtle.Turtle'
		Turtle used to draw the rectangle.

	-------
	Returns
	-------
	None.

	'''
	
	# --- Initialize the color of the turtle --- #
	turtleDrawing.color(shapeColor)

	# --- Start drawing --- #
	turtleDrawing.begin_fill()

	for loop in range(2):
		turtleDrawing.fd(length)
		turtleDrawing.left(90)
		turtleDrawing.fd(width)
		turtleDrawing.left(90)

	turtleDrawing.end_fill()
	# --- End drawing --- #

def draw_triangle(length1, length2, length3, angle1, angle2, angle3, color, turtleDrawing):

	# --- Start drawing --- #
	turtleDrawing.begin_fill()

	turtleDrawing.setheading(angle1)
	turtleDrawing.fd(length1)
	turtleDrawing.setheading(angle2)
	turtleDrawing.fd(length2)
	turtleDrawing.setheading(angle3)
	turtleDrawing.fd(length3)

	turtleDrawing.end_fill()
	# --- End drawing --- #

def half_grid(turtleDrawing):

	# --- Initialize the color of the turtle --- #
	turtleDrawing.color("black")

	# --- Start drawing --- #
	turtleDrawing.up()
	turtleDrawing.goto(0,-500)
	turtleDrawing.down()
	turtleDrawing.setheading(90)
	turtleDrawing.fd(1000)
	turtleDrawing.up()
	turtleDrawing.setheading(0)

	turtleDrawing.goto(-500,0)
	turtleDrawing.down()
	turtleDrawing.setheading(0)
	turtleDrawing.fd(1000)
	turtleDrawing.up()
	turtleDrawing.setheading(0)
	# --- End drawing --- #

def point_color(startColor, endColor, turtleDrawing):

	# --- Start drawing --- #
	turtleDrawing.color(startColor)
	turtleDrawing.dot(10)
	turtleDrawing.color(endColor)
	# --- End drawing --- #

def draw_round_rectangle(x, y, width, height, cornersize, shapeColor, turtleDrawing):
	
	# --- Initialize the position and color of the turtle --- #
	va(x + cornersize, y, turtleDrawing)
	turtleDrawing.color(shapeColor)

	# --- Start drawing --- #
	turtleDrawing.begin_fill()

	for loop in range(2):
		turtleDrawing.fd(width - 2*cornersize)
		turtleDrawing.circle(cornersize, 90)
		turtleDrawing.fd(height - 2*cornersize)
		turtleDrawing.circle(cornersize, 90)

	turtleDrawing.end_fill()
	# --- End drawing --- #

def draw_rectangle_reversed_angle(shapeColor, signLength, signWidth, cornersize, turtleDrawing):

	# --- Initialize the position and color of the turtle --- #
	va(turtleDrawing.position()[0] + cornersize, turtleDrawing.position()[1], turtleDrawing)
	turtleDrawing.color(shapeColor)
	
	# --- Start drawing --- #
	turtleDrawing.begin_fill()

	turtleDrawing.fd(signLength - 2*cornersize)
	turtleDrawing.setheading(270)
	turtleDrawing.circle(cornersize, -90)
	turtleDrawing.setheading(90)
	turtleDrawing.fd(signWidth - 2*cornersize)
	turtleDrawing.setheading(0)
	turtleDrawing.circle(cornersize, -90)
	turtleDrawing.setheading(180)
	turtleDrawing.fd(signLength - 2*cornersize)
	turtleDrawing.setheading(90)
	turtleDrawing.circle(cornersize, -90)
	turtleDrawing.setheading(270)
	turtleDrawing.fd(signWidth - 2*cornersize)
	turtleDrawing.setheading(180)
	turtleDrawing.circle(cornersize, -90)

	turtleDrawing.end_fill()
	# --- End drawing --- #
