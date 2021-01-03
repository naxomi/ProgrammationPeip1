'''
Fichier permettant de dessiner les bouteilles
'''

from drawingFunctions import *
from turtle import *
from math import sqrt, sin, cos, radians

def draw_bottle_body(x, y, factor, width, height, cornersize, bottleBodyTurtle):
	
	# --- Initaliaze the color of the bottle and the orientation of the turtle --- #
	bottleColor = (29, 148, 53)
	bottleBodyTurtle.setheading(0)

	# --- Draw the bottle body --- #
	draw_round_rectangle(x, y, width, height, cornersize, bottleColor, bottleBodyTurtle)

	update()

def draw_bottle_neck(x, y, factor, width, height, cornersize, bottleNeckTurtle):

	# --- Draw the neck --- #
	xBottomLeftOfNeck = cornersize*0.78 + x
	yBottomOfNeck = height + y - 1*factor - 30*factor
	neckLength = 144 *1.2 *factor
	angleStartDrawingNeck = 84

	va(xBottomLeftOfNeck, yBottomOfNeck, bottleNeckTurtle)

	bottleNeckTurtle.begin_fill()

	bottleNeckTurtle.setheading(angleStartDrawingNeck) #Valeur de l'angle choisi arbitrairement
	bottleNeckTurtle.fd(neckLength)
	bottleNeckTurtle.setheading(0)
	bottleNeckTurtle.fd(20 *1.2 *factor)
	bottleNeckTurtle.setheading((180-angleStartDrawingNeck) + 180) #Calcul avec theoreme de Thales -> faire schema dans le compte rendu
	bottleNeckTurtle.fd(neckLength)
	bottleNeckTurtle.setheading(180)
	bottleNeckTurtle.fd(width - cornersize*2 *1.2)

	bottleNeckTurtle.end_fill()

	# --- Draw the mouth --- #
	bottleHeight = neckLength * sin(radians(angleStartDrawingNeck)) + yBottomOfNeck 	#Find the height of the bottle (glass part) using trigonometry
	xForTopLeftCorner = neckLength * cos(radians(angleStartDrawingNeck)) + xBottomLeftOfNeck 	#Find the x value for the top left corner of the neck
	va(xForTopLeftCorner, bottleHeight, bottleNeckTurtle)

	bottleNeckTurtle.begin_fill()

	bottleNeckTurtle.setheading(0)
	bottleNeckTurtle.circle(2.5 * factor, -105)
	endOfCurveHeading = bottleNeckTurtle.heading()
	bottleNeckTurtle.setheading(endOfCurveHeading + 180)
	bottleNeckTurtle.fd(9 * factor)
	bottleNeckTurtle.setheading(0) 
	bottleNeckTurtle.fd(20 *1.2 *factor)
	bottleNeckTurtle.setheading(180 - endOfCurveHeading)
	bottleNeckTurtle.fd(9.25 * factor)
	bottleNeckTurtle.setheading(100)
	bottleNeckTurtle.circle(2.5 * factor, -100)
	va(xForTopLeftCorner, bottleHeight, bottleNeckTurtle)

	bottleNeckTurtle.end_fill()

	# --- Draw the red star with a white star as background on the top of the bottle ---  #
	va(x + width / 2, y + height*1.35, bottleNeckTurtle)
	draw_star(bottleNeckTurtle.position()[0] - starArmLength * cos(radians(44)), bottleNeckTurtle.position()[1], starArmLength + 0.75*factor, (220, 220, 220), bottleNeckTurtle)
	
	va(x + width / 2, y + height*1.35, bottleNeckTurtle)
	draw_star(bottleNeckTurtle.position()[0] - starArmLength * cos(radians(44)) + 1.75*factor, bottleNeckTurtle.position()[1] + 1.75*factor, starArmLength - 1*factor, (200, 15, 30), bottleTurtle)


def draw_bottle_label(x, y, factor, width, height, bottlelabelTurtle):

	# --- Draw an oval around the middle kind of white box --- #
	bottlelabelTurtle.pensize(5 * factor)
	draw_oval(x + width/2, y + height/2, height/3.5, width / 2.5, (220, 220, 220), bottlelabelTurtle)
	bottlelabelTurtle.pensize(1)

	# --- Draw the white oval-like form in the middle of the bottle --- #
	bottlelabelTurtle.setheading(0)
	draw_round_rectangle( (x + width * 0.25), (y + height * 0.30), (width - 2 * width * 0.25), (height - 2 * height * 0.30), 10*factor, (220, 220, 220), bottlelabelTurtle)

	# --- Draw the holder used normaly for the beer name --- #
	va(x, y + height / 2 - 15*factor, bottlelabelTurtle)
	bottlelabelTurtle.setheading(0)
	draw_rectangle(width, 30*factor, (48, 41, 64), bottlelabelTurtle)

	# --- Draw two lines at the top and bottom of the holder --- #
	va(x, y + height / 2 - 12*factor, bottlelabelTurtle)
	bottlelabelTurtle.setheading(0)
	draw_rectangle(width, 1.5*factor, (250, 250, 250), bottlelabelTurtle)

	va(x, y + height / 2 + 12*factor - 1.5*factor, bottlelabelTurtle)
	bottlelabelTurtle.setheading(0)
	draw_rectangle(width, 1.5*factor, (250, 250, 250), bottlelabelTurtle)

	# --- Draw the red star on the middle of the bottle --- #
	va(x + width / 2, y + height / 2 - 15*factor + 30*factor, bottlelabelTurtle)
	starArmLength = 8 * factor
	draw_star(bottlelabelTurtle.position()[0] - starArmLength * cos(radians(44)), bottlelabelTurtle.position()[1] + 2*factor, starArmLength, (200, 15, 30), bottlelabelTurtle)

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

def draw_broken_bottle(x, y, factor, bottleTurtle):

	# --- Initialize variables --- #
	width = 90 * factor
	height = 200 * factor
	cornersize = 20 * factor

	draw_bottle_body(x, y, factor, width, height, cornersize, bottleTurtle, True)
	draw_bottle_label(x, y, factor, width, height, bottleTurtle, True)

	# --- Erase the neck of the bottle --- #





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

def test_sizes_broken_bottle(bottleTurtle):
	# --- Function used to test if the bottle design is working in multiple sizes --- # 
	draw_broken_bottle(-600, -400, 2, bottleTurtle)
	leftCorner = -600 + 25+ 90*2
	draw_broken_bottle(leftCorner,-400, 1.8, bottleTurtle)
	leftCorner += 25 + 90*1.8
	draw_broken_bottle(leftCorner, -400, 1.6, bottleTurtle)
	leftCorner += 25 + 90*1.6
	draw_broken_bottle(leftCorner, -400, 1.4, bottleTurtle)
	leftCorner += 25 + 90*1.4
	draw_broken_bottle(leftCorner, -400, 1.2, bottleTurtle)
	leftCorner += 25 + 90*1.2
	draw_broken_bottle(leftCorner, -400, 1, bottleTurtle)
	leftCorner += 25 + 90*1.0
	draw_broken_bottle(leftCorner, -400, 0.8, bottleTurtle)
	leftCorner += 25 + 90*0.8
	draw_broken_bottle(leftCorner, -400, 0.6, bottleTurtle)
	leftCorner += 25 + 90*0.6
	draw_broken_bottle(leftCorner, -400, 0.4, bottleTurtle)