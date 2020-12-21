'''
Fichier permettant de dessiner les bouteilles
'''

from drawingFunctions import *
from turtle import *
from math import sqrt, sin, cos, radians

def draw_bottle_body(x=0, y=0, factor=1, width=90, height=200, cornersize=20):

	bottleColor = (29, 148, 53)
 
	setheading(0)

	xBottomLeftOfNeck = cornersize*0.78 + x
	yBottomOfNeck = height + y - 1*factor - 30*factor

	# --- Draw the bottle body --- #
	draw_round_rectangle(x, y, width, height, cornersize, bottleColor)

	# --- Draw the neck --- #
	va(xBottomLeftOfNeck, yBottomOfNeck)

	begin_fill()

	neckLength = 144 *1.2 *factor
	angleStartNeck = 84

	setheading(angleStartNeck) #Valeur de l'angle choisi arbitrairement
	fd(neckLength)
	setheading(0)
	fd(20 *1.2 *factor)
	setheading((180-angleStartNeck) + 180) #Calcul avec theoreme de Thales -> faire schema dans le compte rendu
	fd(neckLength)
	setheading(180)
	fd(width - cornersize*2 *1.2)

	end_fill()

	# --- Draw the "goulot" --- #
	bottleHeight = neckLength * sin(radians(angleStartNeck)) + yBottomOfNeck #Find the height of the bottle (glass part) using trigonometry
	xForTopLeftCorner = neckLength * cos(radians(angleStartNeck)) + xBottomLeftOfNeck #Find the x value for the top left corner of the neck
	va(xForTopLeftCorner, bottleHeight)

	begin_fill()

	setheading(0)
	circle(2.5 * factor, -105)
	endOfCurveHeading = heading()
	setheading(endOfCurveHeading + 180)
	fd(9 * factor)
	setheading(0) 
	fd(20 *1.2 *factor)
	setheading(180 - endOfCurveHeading)
	fd(9.25 * factor)
	setheading(100)
	circle(2.5 * factor, -100)
	va(xForTopLeftCorner, bottleHeight)

	end_fill()

	update()

def draw_bottle_label(x=0, y=0, factor=1, width=90, height=200):

	# --- Draw an oval around the middle kind of white box --- #
	pensize(5 * factor)
	draw_oval(x + width/2, y + height/2, height/3.5, width / 2.5, (220, 220, 220))
	pensize(1)

	# --- Draw the white oval-like form in the middle of the bottle --- #
	setheading(0)
	draw_round_rectangle( (x + width * 0.25), (y + height * 0.30), (width - 2 * width * 0.25), (height - 2 * height * 0.30), 10*factor, (220, 220, 220))

	# --- Draw the holder used normaly for the beer name --- #
	va(x, y + height / 2 - 15*factor)
	setheading(0)
	draw_rectangle(width, 30*factor, (48, 41, 64))

	# --- Draw two lines at the top and bottom of the holder --- #
	va(x, y + height / 2 - 12*factor)
	setheading(0)
	draw_rectangle(width, 1.5*factor, (250, 250, 250))

	va(x, y + height / 2 + 12*factor - 1.5*factor)
	setheading(0)
	draw_rectangle(width, 1.5*factor, (250, 250, 250))

	# --- Draw the red star on the middle of the bottle --- #

	va(x + width / 2, y + height / 2 - 15*factor + 30*factor)
	
	starArmLength = 8 * factor
	draw_star(position()[0] - starArmLength * cos(radians(44)), position()[1] + 2*factor, starArmLength)

	# --- Draw the red star on the top of the bottle ---  #

	va(x + width / 2, y + height*1.35)
	draw_star(position()[0] - starArmLength * cos(radians(44)), position()[1], starArmLength + 0.75*factor, (220, 220, 220))
	va(x + width / 2, y + height*1.35)
	draw_star(position()[0] - starArmLength * cos(radians(44)) + 1.75*factor, position()[1] + 1.75*factor, starArmLength - 1*factor)

	update()

def draw_bottle(x, y, factor):

	width = 90 * factor
	height = 200 * factor
	cornersize = 20 * factor

	draw_bottle_body(x, y, factor, width, height, cornersize)
	draw_bottle_label(x, y, factor, width, height)

def test_sizes_bottle():
	draw_bottle(-600, -400, 2)
	leftCorner = -600 + 25+ 90*2
	draw_bottle(leftCorner,-400, 1.8)
	leftCorner += 25 + 90*1.8
	draw_bottle(leftCorner, -400, 1.6)
	leftCorner += 25 + 90*1.6
	draw_bottle(leftCorner, -400, 1.4)
	leftCorner += 25 + 90*1.4
	draw_bottle(leftCorner, -400, 1.2)
	leftCorner += 25 + 90*1.2
	draw_bottle(leftCorner, -400, 1)
	leftCorner += 25 + 90*1.0
	draw_bottle(leftCorner, -400, 0.8)
	leftCorner += 25 + 90*0.8
	draw_bottle(leftCorner, -400, 0.6)
	leftCorner += 25 + 90*0.6
	draw_bottle(leftCorner, -400, 0.4)