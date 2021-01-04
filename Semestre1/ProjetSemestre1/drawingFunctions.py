'''
Fichier contenant toutes les fonctions permettant de dessiner des formes
'''

from turtle import *
from math import sqrt, sin, radians

def va(x, y):
	up()
	goto(x, y)
	down()

def draw_star(x, y, length, shapeColor):

	# --- Initialize the position and color of the turtle --- #
	va(x, y)
	color(shapeColor)

	# --- Start drawing --- #
	begin_fill()

	setheading(36)
	for loop in range(5):
		forward(length)
		right(72)
		forward(length)
		left(144)

	end_fill()
	# --- End drawing --- #

<<<<<<< Updated upstream
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
	
=======
def draw_oval(centerX, centerY, length, cornersize, shapeColor):
>>>>>>> Stashed changes
	# --- Initialize the position, orientation and color of the turtle --- #
	setheading(270)
	color(shapeColor)
	va(centerX - cornersize, centerY - length/2)

	# --- Start drawing --- #
	circle(cornersize, 180)
	fd(length)
	circle(cornersize, 180)
	fd(length)
	# --- End drawing --- #

def draw_rectangle(length, width, shapeColor, fill=True):

	# --- Initialize color of the turtle --- #
	color(shapeColor)

	# --- Start drawing --- #
	if fill:
		begin_fill()

	for loop in range(2):
		fd(length)
		left(90)
		fd(width)
		left(90)
	
	if fill:
		end_fill()
	# --- End drawing --- #
    
def draw_triangle_isocele(x, y, base, hauteur, couleur="black"):
	# --- Initialize the position and color of the turtle --- #
	va(x,y)
	color(couleur)

	# --- Start drawing --- #
	begin_fill()

	goto(x+base,y)
	goto(x+(base/2),y+hauteur)
	goto(x,y)

	end_fill()
	# --- End drawing --- #

def draw_round_rectangle(x, y, width, height, cornersize, shapeColor):
	
	# --- Initialize the position and color of the turtle --- #
	va(x + cornersize, y)
	color(shapeColor)

	# --- Start drawing --- #
	begin_fill()
    
	for loop in range(2):
		fd(width - 2*cornersize)
		circle(cornersize, 90)
		fd(height - 2*cornersize)
		circle(cornersize, 90)
	
	end_fill()
	# --- End drawing --- #
    

def draw_rectangle_reversed_angle(shapeColor, signLength, signWidth, cornersize):

	# --- Initialize the position and color of the turtle --- #
	va(position()[0] + cornersize, position()[1])
	colormode(255)
	color(shapeColor)
	
	# --- Start drawing --- #
	begin_fill()

	fd(signLength - 2*cornersize)
	setheading(270)
	circle(cornersize, -90)
	setheading(90)
	fd(signWidth - 2*cornersize)
	setheading(0)
	circle(cornersize, -90)
	setheading(180)
	fd(signLength - 2*cornersize)
	setheading(90)
	circle(cornersize, -90)
	setheading(270)
	fd(signWidth - 2*cornersize)
	setheading(180)
	circle(cornersize, -90)

	end_fill()
	# --- End drawing --- #
