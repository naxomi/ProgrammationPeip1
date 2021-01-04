'''
Fichier permettant de dessiner les bouteilles
'''

from drawingFunctions import *
from turtle import *
from math import sqrt, sin, cos, radians

def draw_bottle_body(x, y, factor, width, height, cornersize):
	
	# --- Initaliaze the color of the bottle and the orientation of the turtle --- #
	bottleColor = "Green"
	setheading(0)

	# --- Draw the bottle body --- #
	draw_round_rectangle(x, y, width, height, cornersize, bottleColor)

	# --- Draw the neck --- #

	xBottomLeftOfNeck = cornersize*0.78 + x
	yBottomOfNeck = height + y - 1*factor - 30*factor
	neckLength = 144 *1.2 *factor
	angleStartDrawingNeck = 84

	va(xBottomLeftOfNeck, yBottomOfNeck)

	begin_fill()

	setheading(angleStartDrawingNeck) #Valeur de l'angle choisi arbitrairement
	fd(neckLength)
	setheading(0)
	fd(20 *1.2 *factor)
	setheading((180-angleStartDrawingNeck) + 180) #Calcul avec theoreme de Thales -> faire schema dans le compte rendu
	fd(neckLength)
	setheading(180)
	fd(width - cornersize*2 *1.2)

	end_fill()

	# --- Draw the "goulot" --- #
	bottleHeight = neckLength * sin(radians(angleStartDrawingNeck)) + yBottomOfNeck 	#Find the height of the bottle (glass part) using trigonometry
	xForTopLeftCorner = neckLength * cos(radians(angleStartDrawingNeck)) + xBottomLeftOfNeck 	#Find the x value for the top left corner of the neck

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

	# --- #

def draw_bottle_label(x, y, factor, width, height):

	# --- Draw an oval around the middle kind of white box --- #
	pensize(5 * factor)
	draw_oval(x + width/2, y + height/2, height/3.5, width / 2.5, (250,250,250))
	pensize(1)

	# --- Draw the white oval-like form in the middle of the bottle --- #
	setheading(0)
	draw_round_rectangle( (x + width * 0.25), (y + height * 0.30), (width - 2 * width * 0.25), (height - 2 * height * 0.30), 10*factor, (250,250,250))

	# --- Draw the holder used normaly for the beer name --- #
	va(x, y + height / 2 - 15*factor)
	setheading(0)
	draw_rectangle(width, 30*factor, "DarkSlateBlue")

	# --- Draw two lines at the top and bottom of the holder --- #
	va(x, y + height / 2 - 12*factor)
	setheading(0)
	draw_rectangle(width, 1.5*factor, (250,250,250))

	va(x, y + height / 2 + 12*factor - 1.5*factor)
	setheading(0)
	draw_rectangle(width, 1.5*factor, (250,250,250))

	# --- Draw the red star on the middle of the bottle --- #
	va(x + width / 2, y + height / 2 - 15*factor + 30*factor)
	starArmLength = 8 * factor
	draw_star(position()[0] - starArmLength * cos(radians(44)), position()[1] + 2*factor, starArmLength, "FireBrick")

	# --- Draw the red star with a white star as background on the top of the bottle ---  #
	va(x + width / 2, y + height*1.35)
	draw_star(position()[0] - starArmLength * cos(radians(44)), position()[1], starArmLength + 0.75*factor, (250,250,250))
	va(x + width / 2, y + height*1.35)
	draw_star(position()[0] - starArmLength * cos(radians(44)) + 1.75*factor, position()[1] + 1.75*factor, starArmLength - 1*factor, "FireBrick")

	# --- #
	update()

def draw_bottle(x, y, factor):
	# --- Initialize variables --- #
	width = 90 * factor
	height = 200 * factor
	cornersize = 20 * factor

	# --- Draw the bottle by making the body first and then the label on it --- #
	draw_bottle_body(x, y, factor, width, height, cornersize)
	draw_bottle_label(x, y, factor, width, height)

def draw_broken_bottle(x, y, factor, breaking, backgroundColor):
	# --- Initialize variables --- #
	width = 90 * factor
	height = 100 * factor
	cornersize = 20 * factor

	# --- If the bottle is shot, we need to erase the bottle breaking before placing the broken one --- #

	if breaking == True:

		setheading(0)
		draw_round_rectangle(x, y, width, height*3.55, cornersize, backgroundColor)

	# --- Draw the bottle base --- #
	draw_round_rectangle(x, y, width, height, cornersize, "Green")

	# --- Draw the broken part --- #
	va(x,y+height/2)
	draw_rectangle(width,height/2,"Green")
	draw_triangle_isocele(x-width/7, y+height, width/4, height/3, "Green")
	draw_triangle_isocele(x, y+height, width/3, height/2, "Green")
	draw_triangle_isocele(x+width/5, y+height, width/3, height/4, "Green")
	draw_triangle_isocele(x+width/3, y+height, width/3, height/3, "Green")
	draw_triangle_isocele(x+width/2, y+height, width/2, height/2, "Green")
	draw_triangle_isocele(x+width*4/5, y+height, width/4, height/3, "Green")
    
	# --- Clean the edges of the bottle --- #
	va(x-width/6,y)
	draw_rectangle(width/6, height*2, backgroundColor)
	va(x+width,y)
	draw_rectangle(width/10, height*2, backgroundColor)

	# --- #
