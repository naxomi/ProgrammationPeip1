'''
Fichier permettant de dessiner les bouteilles
'''

from drawingFunctions import *
from turtle import *
from math import sqrt, sin, cos, radians

def draw_bottle_body(x, y, factor, width, height, cornersize, bottleTurtle):
	
	# --- Initaliaze the color of the bottle and the orientation of the turtle --- #
	bottleColor = (29, 148, 53)
	bottleTurtle.setheading(0)

	# --- Draw the bottle body --- #
	draw_round_rectangle(x, y, width, height, cornersize, bottleColor, bottleTurtle)

	# --- Draw the neck --- #

	xBottomLeftOfNeck = cornersize*0.78 + x
	yBottomOfNeck = height + y - 1*factor - 30*factor
	neckLength = 144 *1.2 *factor
	angleStartDrawingNeck = 84

	va(xBottomLeftOfNeck, yBottomOfNeck, bottleTurtle)

	bottleTurtle.begin_fill()

	bottleTurtle.setheading(angleStartDrawingNeck) #Valeur de l'angle choisi arbitrairement
	bottleTurtle.fd(neckLength)
	bottleTurtle.setheading(0)
	bottleTurtle.fd(20 *1.2 *factor)
	bottleTurtle.setheading((180-angleStartDrawingNeck) + 180) #Calcul avec theoreme de Thales -> faire schema dans le compte rendu
	bottleTurtle.fd(neckLength)
	bottleTurtle.setheading(180)
	bottleTurtle.fd(width - cornersize*2 *1.2)

	bottleTurtle.end_fill()

	# --- Draw the "goulot" --- #
	bottleHeight = neckLength * sin(radians(angleStartDrawingNeck)) + yBottomOfNeck 	#Find the height of the bottle (glass part) using trigonometry
	xForTopLeftCorner = neckLength * cos(radians(angleStartDrawingNeck)) + xBottomLeftOfNeck 	#Find the x value for the top left corner of the neck
	va(xForTopLeftCorner, bottleHeight, bottleTurtle)

	bottleTurtle.begin_fill()

	bottleTurtle.setheading(0)
	bottleTurtle.circle(2.5 * factor, -105)
	endOfCurveHeading = bottleTurtle.heading()
	bottleTurtle.setheading(endOfCurveHeading + 180)
	bottleTurtle.fd(9 * factor)
	bottleTurtle.setheading(0) 
	bottleTurtle.fd(20 *1.2 *factor)
	bottleTurtle.setheading(180 - endOfCurveHeading)
	bottleTurtle.fd(9.25 * factor)
	bottleTurtle.setheading(100)
	bottleTurtle.circle(2.5 * factor, -100)
	va(xForTopLeftCorner, bottleHeight, bottleTurtle)

	bottleTurtle.end_fill()

	update()

def draw_bottle_label(x, y, factor, width, height, bottleTurtle):

	# --- Draw an oval around the middle kind of white box --- #
	bottleTurtle.pensize(5 * factor)
	draw_oval(x + width/2, y + height/2, height/3.5, width / 2.5, (220, 220, 220), bottleTurtle)
	bottleTurtle.pensize(1)

	# --- Draw the white oval-like form in the middle of the bottle --- #
	bottleTurtle.setheading(0)
	draw_round_rectangle( (x + width * 0.25), (y + height * 0.30), (width - 2 * width * 0.25), (height - 2 * height * 0.30), 10*factor, (220, 220, 220), bottleTurtle)

	# --- Draw the holder used normaly for the beer name --- #
	va(x, y + height / 2 - 15*factor, bottleTurtle)
	bottleTurtle.setheading(0)
	draw_rectangle(width, 30*factor, (48, 41, 64), bottleTurtle)

	# --- Draw two lines at the top and bottom of the holder --- #
	va(x, y + height / 2 - 12*factor, bottleTurtle)
	bottleTurtle.setheading(0)
	draw_rectangle(width, 1.5*factor, (250, 250, 250), bottleTurtle)

	va(x, y + height / 2 + 12*factor - 1.5*factor, bottleTurtle)
	bottleTurtle.setheading(0)
	draw_rectangle(width, 1.5*factor, (250, 250, 250), bottleTurtle)

	# --- Draw the red star on the middle of the bottle --- #
	va(x + width / 2, y + height / 2 - 15*factor + 30*factor, bottleTurtle)
	starArmLength = 8 * factor
	draw_star(bottleTurtle.position()[0] - starArmLength * cos(radians(44)), bottleTurtle.position()[1] + 2*factor, starArmLength, (200, 15, 30), bottleTurtle)

	# --- Draw the red star with a white star as background on the top of the bottle ---  #
	va(x + width / 2, y + height*1.35, bottleTurtle)
	draw_star(bottleTurtle.position()[0] - starArmLength * cos(radians(44)), bottleTurtle.position()[1], starArmLength + 0.75*factor, (220, 220, 220), bottleTurtle)
	va(x + width / 2, y + height*1.35, bottleTurtle)
	draw_star(bottleTurtle.position()[0] - starArmLength * cos(radians(44)) + 1.75*factor, bottleTurtle.position()[1] + 1.75*factor, starArmLength - 1*factor, (200, 15, 30), bottleTurtle)

	# --- #
	update()

def draw_bottle(x, y, factor, bottleTurtle):

	# --- Initialize variables --- #
	width = 90 * factor
	height = 200 * factor
	cornersize = 20 * factor

	# --- Draw the bottle by making the body first and then the label on it --- #
	draw_bottle_body(x, y, factor, width, height, cornersize, bottleTurtle)
	draw_bottle_label(x, y, factor, width, height, bottleTurtle)

def test_sizes_bottle(bottleTurtle):
	# --- Function used to test if the bottle design is working in multiple sizes --- # 
	draw_bottle(-600, -400, 2, bottleTurtle)
	leftCorner = -600 + 25+ 90*2
	draw_bottle(leftCorner,-400, 1.8, bottleTurtle)
	leftCorner += 25 + 90*1.8
	draw_bottle(leftCorner, -400, 1.6, bottleTurtle)
	leftCorner += 25 + 90*1.6
	draw_bottle(leftCorner, -400, 1.4, bottleTurtle)
	leftCorner += 25 + 90*1.4
	draw_bottle(leftCorner, -400, 1.2, bottleTurtle)
	leftCorner += 25 + 90*1.2
	draw_bottle(leftCorner, -400, 1, bottleTurtle)
	leftCorner += 25 + 90*1.0
	draw_bottle(leftCorner, -400, 0.8, bottleTurtle)
	leftCorner += 25 + 90*0.8
	draw_bottle(leftCorner, -400, 0.6, bottleTurtle)
	leftCorner += 25 + 90*0.6
	draw_bottle(leftCorner, -400, 0.4, bottleTurtle)