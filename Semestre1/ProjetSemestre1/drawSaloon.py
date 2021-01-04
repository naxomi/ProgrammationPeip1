'''
Fichier permettant de dessiner le saloon
'''

from drawingFunctions import *
from turtle import *
from math import sqrt, sin, radians, cos

def draw_saloon_sign(x, y, lengthMainStructure, heightMainStructure, xShiftFromBaseToStructure, factor):

	cornersize = 20 * factor
	signLength = (lengthMainStructure / 1.75)
	signWidth = (heightMainStructure / 3.75)

	xForSign = x + lengthMainStructure/2 - signLength/2 + cornersize
	yForSign = y + heightMainStructure - signWidth/2

	# --- Draw the shadow for the sign --- #
	setheading(0)
	va(xForSign, yForSign - 10*factor)
	draw_rectangle_reversed_angle((115, 86, 58), signLength, signWidth, cornersize)

	# --- Draw the sign --- #

	setheading(0)
	va(xForSign, yForSign)
	draw_rectangle_reversed_angle((251, 200, 46), signLength, signWidth, cornersize)

	fontSize = 52 * factor
	color(91, 69, 47)
	va(x + lengthMainStructure / 2 + xShiftFromBaseToStructure, yForSign + signWidth/2 - fontSize/2)
	write("SALOON", False, align="center", font=("Western", int(fontSize), "normal"))

def draw_house_window(x, y, heightMainStructure, factor):
	# --- Draw the window --- #
	draw_round_rectangle(x, y, 130*factor, heightMainStructure / 4, 10*factor, (114, 86, 58))

	va(x + 10*factor, y + 10*factor)
	draw_rectangle(110*factor, heightMainStructure / 4 - 20*factor, (132, 215, 221))

	# --- Draw the shadow on the window --- #
	color(101, 175, 182)
	va(position()[0] + 110*factor*0.4, position()[1])
	setheading(0)

	begin_fill()

	fd(110*factor*0.6)
	setheading(90)
	fd(heightMainStructure / 4 - 20*factor)
	setheading(180)
	fd(70*factor*0.6)

	end_fill()

def draw_door(xBottomLeft, yBottomLeft, widthDoor, heightDoor, factor):
	va(xBottomLeft, yBottomLeft)
	setheading(0)
	draw_rectangle(widthDoor, heightDoor, (150, 116, 81))

	heightDoorHole = heightDoor / 11.0
	widthDoorHole = widthDoor - 2*heightDoorHole

	loop = 1
	while loop <= 9:
		va(xBottomLeft + heightDoorHole, yBottomLeft + heightDoorHole*loop)
		draw_rectangle(widthDoorHole, heightDoorHole, (115, 86, 57))
		loop += 2

def draw_saloon(x, y, factor):
	colormode(255)
    
	# --- Draw the base --- #
	va(x, y)
	lengthBase = 400 * factor
	heightBase = 20 * factor
	draw_rectangle(lengthBase, heightBase, (70, 52, 33))
	
	# --- Draw the main structure --- #
	lengthMainStructure = 360 * factor
	heightMainStructure = 320 * factor
	xShiftFromBaseToStructure = (lengthBase - lengthMainStructure) / 2

	va(x + xShiftFromBaseToStructure, y + heightBase)
	draw_rectangle(lengthMainStructure, heightMainStructure - heightBase, (150, 116, 81))

	# --- Draw a structural beam in the middle (appearing on each side of the building) --- #
	# --- Bit on the left side --- #
	va(x, y + heightBase + heightMainStructure / 2)
	setheading(0)
	draw_rectangle(xShiftFromBaseToStructure, xShiftFromBaseToStructure, (114, 86, 58))
	# --- Bit on the right side --- #
	va(x + xShiftFromBaseToStructure + lengthMainStructure, y + heightBase + heightMainStructure / 2)
	setheading(0)
	draw_rectangle(xShiftFromBaseToStructure, xShiftFromBaseToStructure, (114, 86, 58))

	# --- Draw the roof --- #
	color(91, 69, 47)

	begin_fill()

	va(x, y + heightMainStructure)
	setheading(0)
	fd(lengthBase)
	left(100)
	fd(100*factor)
	setheading(180)
	fd(lengthBase - (2 * cos(radians(80)) * 100 *factor))
	left(80)
	fd(100*factor)
	end_fill()

	# --- Draw the roof shadow on the building --- #
	va(x + xShiftFromBaseToStructure, y + heightMainStructure - heightBase)
	setheading(0)
	draw_rectangle(lengthMainStructure, heightBase, (115, 86, 58))

	# --- Draw the window on the right --- #
	draw_house_window(x + 50*factor, y + heightBase + heightMainStructure / 2, heightMainStructure, factor)

	# --- Draw the window on the left --- #
	setheading(0)
	draw_house_window(x + 50*factor + 130*factor + 40*factor, y + heightBase + heightMainStructure / 2, heightMainStructure, factor)

	# --- Draw the sign on top of the saloon --- #
	setheading(0)
	draw_saloon_sign(x, y, lengthMainStructure, heightMainStructure, xShiftFromBaseToStructure, factor)

	# --- Draw the door --- #
	setheading(0)

	xBottomLeftCornerDoor = x + lengthMainStructure/3 + xShiftFromBaseToStructure

	va(xBottomLeftCornerDoor, y + heightBase)
	widthDoor = lengthMainStructure - 2*lengthMainStructure/3
	heightDoor = heightMainStructure / 2.5
	draw_rectangle(widthDoor, heightDoor, (70, 52, 33))

	# --- Draw the border around the door --- #
	color(115, 86, 58)
	sizeForThePen = 10*factor

	pensize(sizeForThePen)
	va(xBottomLeftCornerDoor - sizeForThePen/2, y + heightBase + sizeForThePen/2)
	setheading(90)
	fd(heightDoor)
	setheading(0)
	fd(widthDoor + sizeForThePen)
	setheading(270)
	fd(heightDoor)

	pensize(1)

	# --- Draw the darker wood on both side of the door --- #

	setheading(0)
	adjustementValue = 1*factor

	va(x + xShiftFromBaseToStructure, y + heightBase)
	draw_rectangle(lengthMainStructure/3 - adjustementValue, heightMainStructure/6, (115, 86, 58))

	setheading(0)
	va(xBottomLeftCornerDoor + widthDoor + adjustementValue, y + xShiftFromBaseToStructure)
	draw_rectangle(lengthMainStructure/3 - adjustementValue, heightMainStructure/6, (115, 86, 58))
	
	# --- Draw the doors on the middle of the saloon --- #
	widthMoveableDoor = widthDoor*0.46

	# Left door #
	setheading(0)
	draw_door(xBottomLeftCornerDoor, y + heightDoor*0.38, widthMoveableDoor, heightDoor/2, factor)

	# Right door #
	setheading(0)
	draw_door(xBottomLeftCornerDoor + widthDoor - widthMoveableDoor, y + heightDoor*0.38, widthMoveableDoor, heightDoor/2, factor)
'''
def draw_many_saloons():
	x = -650
	y = -400
	coords = (x, y)
	draw_saloon(coords[0], coords[1], 1.2)
	setheading(0)
	x += 400 * 1.2 + 50
	coords = (x, y)
	draw_saloon(coords[0], coords[1], 1)
	setheading(0)
	x += 400 * 1 + 50
	coords = (x, y)
	draw_saloon(coords[0], coords[1], 0.8)
	setheading(0)
	coords = (0, 50)
	draw_saloon(coords[0], coords[1], 0.6)
	setheading(0)
	x = 400 * 0.6 + 20
	coords = (x, 50)
	draw_saloon(coords[0], coords[1], 0.4)

	update()
'''
######################################## DEBUT TEST 

#height = 768
#width = 1366

#screen = Screen()
#screen.setup(width, height)

#tracer(False)
#hideturtle()
#colormode(255)

#draw_many_saloons()

#draw_saloon(-200, -200, 1)
#draw_saloon(-500, -425, 2)

#update()

######################################## FIN TEST

#exitonclick()