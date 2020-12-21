'''
Fichier contenant toutes les fonctions permettant de dessiner des formes
'''

from turtle import *
from math import sqrt, sin, radians

def va(x, y):
	up()
	goto(x, y)
	down()

def draw_star(x, y, length, shapeColor=(200, 15, 30)):
	va(x, y)
	color(shapeColor)
	begin_fill()

	setheading(36)
	for loop in range(5):
		forward(length)
		right(72)
		forward(length)
		left(144)

	end_fill()

def draw_oval(centerX, centerY, length, cornersize, shapeColor=(220, 220, 220)):
	setheading(270)
	color(shapeColor)
	va(centerX - cornersize, centerY - length/2)
	circle(cornersize, 180)
	fd(length)
	circle(cornersize, 180)
	fd(length)

def draw_rectangle(length, width, shapeColor):
	color(shapeColor)
	begin_fill()
	for loop in range(2):
		fd(length)
		left(90)
		fd(width)
		left(90)
	end_fill()

def draw_triangle(length1, length2, length3, angle1, angle2, angle3, color):
	begin_fill()
	setheading(angle1)
	fd(length1)
	setheading(angle2)
	fd(length2)
	setheading(angle3)
	fd(length3)
	end_fill()

def half_grid():
	color("black")
	up()
	goto(0,-500)
	down()
	setheading(90)
	fd(1000)
	up()
	setheading(0)

	goto(-500,0)
	down()
	setheading(0)
	fd(1000)
	up()
	setheading(0)

def point_color(startColor, endColor="green"):
	color(startColor)
	dot(10)
	color(endColor)
	print(position())

def draw_round_rectangle(x, y, width, height, cornersize, shapeColor):
	va(x + cornersize, y)

	color(shapeColor)

	begin_fill()

	for loop in range(2):
		fd(width - 2*cornersize)
		circle(cornersize, 90)
		fd(height - 2*cornersize)
		circle(cornersize, 90)

	end_fill()

def draw_rectangle_reversed_angle(shapeColor, signLength, signWidth, cornersize):
	va(position()[0] + cornersize, position()[1])
	color(shapeColor)
	
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