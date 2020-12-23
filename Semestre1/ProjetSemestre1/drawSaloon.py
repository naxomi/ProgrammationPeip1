'''
Fichier permettant de dessiner le saloon
'''

from drawingFunctions import *
from turtle import *
from math import sqrt, sin, radians

def draw_saloon_sign(x, y, lengthMainStructure, heightMainStructure, xShiftFromBaseToStructure, factor, saloonTurtle):

	cornersize = 20 * factor
	signLength = (lengthMainStructure / 1.75)
	signWidth = (heightMainStructure / 3.75)

	xForSign = x + lengthMainStructure/2 - signLength/2 + cornersize
	yForSign = y + heightMainStructure - signWidth/2

	#Draw the shadow for the sign
	saloonTurtle.setheading(0)
	va(xForSign, yForSign - 10*factor, saloonTurtle)
	draw_rectangle_reversed_angle((115, 86, 58), signLength, signWidth, cornersize, saloonTurtle)

	#Draw the sign

	saloonTurtle.setheading(0)
	va(xForSign, yForSign, saloonTurtle)
	draw_rectangle_reversed_angle((251, 200, 46), signLength, signWidth, cornersize, saloonTurtle)

	fontSize = 52 * factor
	saloonTurtle.color(91, 69, 47)
	va(x + lengthMainStructure / 2 + xShiftFromBaseToStructure, yForSign + signWidth / 2 - fontSize / 2, saloonTurtle)
	saloonTurtle.write("SALOON", False, align="center", font=("Western", int(fontSize), "normal"))

def draw_house_window(x, y, heightMainStructure, factor, saloonTurtle):
	# --- Draw the window --- #
	draw_round_rectangle(x, y, 130*factor, heightMainStructure / 4, 10*factor, (114, 86, 58), saloonTurtle)

	va(x + 10*factor, y + 10*factor, saloonTurtle)
	draw_rectangle(110*factor, heightMainStructure / 4 - 20*factor, (132, 215, 221), saloonTurtle)

	# --- Draw the shadow on the window --- #
	saloonTurtle.color(101, 175, 182)
	va(saloonTurtle.position()[0] + 110*factor*0.4, saloonTurtle.position()[1], saloonTurtle)
	saloonTurtle.setheading(0)

	saloonTurtle.begin_fill()

	saloonTurtle.fd(110*factor*0.6)
	saloonTurtle.setheading(90)
	saloonTurtle.fd(heightMainStructure / 4 - 20*factor)
	saloonTurtle.setheading(180)
	saloonTurtle.fd(70*factor*0.6)

	saloonTurtle.end_fill()

def draw_door(xBottomLeft, yBottomLeft, widthDoor, heightDoor, factor, saloonTurtle):
	va(xBottomLeft, yBottomLeft, saloonTurtle)
	saloonTurtle.setheading(0)
	draw_rectangle(widthDoor, heightDoor, (150, 116, 81), saloonTurtle)

	heightDoorHole = heightDoor / 11.0
	widthDoorHole = widthDoor - 2*heightDoorHole

	loop = 1
	while loop <= 9:
		va(xBottomLeft + heightDoorHole, yBottomLeft + heightDoorHole*loop, saloonTurtle)
		draw_rectangle(widthDoorHole, heightDoorHole, (115, 86, 57), saloonTurtle)
		loop += 2

def draw_saloon(x, y, factor, saloonTurtle):
	# --- Draw the base --- #
	va(x, y, saloonTurtle)
	lengthBase = 400 * factor
	heightBase = 20 * factor
	draw_rectangle(lengthBase, heightBase, (70, 52, 33), saloonTurtle)
	
	# --- Draw the main structure --- #
	lengthMainStructure = 360 * factor
	heightMainStructure = 320 * factor
	xShiftFromBaseToStructure = (lengthBase - lengthMainStructure) / 2

	va(x + xShiftFromBaseToStructure, y + heightBase, saloonTurtle)
	draw_rectangle(lengthMainStructure, heightMainStructure - heightBase, (150, 116, 81), saloonTurtle)

	# --- Draw a structural beam in the middle (appearing on each side of the building) --- #
	# --- Bit on the left side --- #
	va(x, y + heightBase + heightMainStructure / 2, saloonTurtle)
	saloonTurtle.setheading(0)
	draw_rectangle(xShiftFromBaseToStructure, xShiftFromBaseToStructure, (114, 86, 58), saloonTurtle)
	# --- Bit on the right side --- #
	va(x + xShiftFromBaseToStructure + lengthMainStructure, y + heightBase + heightMainStructure / 2, saloonTurtle)
	saloonTurtle.setheading(0)
	draw_rectangle(xShiftFromBaseToStructure, xShiftFromBaseToStructure, (114, 86, 58), saloonTurtle)

	# --- Draw the roof --- #
	saloonTurtle.color(91, 69, 47)

	saloonTurtle.begin_fill()

	va(x, y + heightMainStructure, saloonTurtle)
	saloonTurtle.setheading(0)
	saloonTurtle.fd(lengthBase)
	saloonTurtle.left(100)
	saloonTurtle.fd(100*factor)
	saloonTurtle.setheading(180)
	saloonTurtle.fd(lengthBase - 2 * cos(radians(80)) * 100 *factor)
	saloonTurtle.left(80)
	saloonTurtle.fd(100*factor)

	saloonTurtle.end_fill()

	# --- Draw the roof shadow on the building --- #
	va(x + xShiftFromBaseToStructure, y + heightMainStructure - heightBase, saloonTurtle)
	saloonTurtle.setheading(0)
	draw_rectangle(lengthMainStructure, heightBase, (115, 86, 58), saloonTurtle)

	# --- Draw the window on the right --- #
	draw_house_window(x + 50*factor, y + heightBase + heightMainStructure / 2, heightMainStructure, factor, saloonTurtle)

	# --- Draw the window on the left --- #
	saloonTurtle.setheading(0)
	draw_house_window(x + 50*factor + 130*factor + 40*factor, y + heightBase + heightMainStructure / 2, heightMainStructure, factor, saloonTurtle)

	# --- Draw the sign on top of the saloon --- #
	saloonTurtle.setheading(0)
	draw_saloon_sign(x, y, lengthMainStructure, heightMainStructure, xShiftFromBaseToStructure, factor, saloonTurtle)

	# --- Draw the door --- @
	saloonTurtle.setheading(0)

	xBottomLeftCornerDoor = x + lengthMainStructure/3 + xShiftFromBaseToStructure

	va(xBottomLeftCornerDoor, y + heightBase, saloonTurtle)
	widthDoor = lengthMainStructure - 2*lengthMainStructure/3
	heightDoor = heightMainStructure / 2.5
	draw_rectangle(widthDoor, heightDoor, (70, 52, 33), saloonTurtle)

	# --- Draw the border around the door --- #
	saloonTurtle.color(115, 86, 58)
	sizeForThePen = 10*factor

	saloonTurtle.pensize(sizeForThePen)
	va(xBottomLeftCornerDoor - sizeForThePen/2, y + heightBase + sizeForThePen/2, saloonTurtle)
	saloonTurtle.setheading(90)
	saloonTurtle.fd(heightDoor)
	saloonTurtle.setheading(0)
	saloonTurtle.fd(widthDoor + sizeForThePen)
	saloonTurtle.setheading(270)
	saloonTurtle.fd(heightDoor)

	saloonTurtle.pensize(1)

	# --- Draw the darker wood on both side of the door --- #

	saloonTurtle.setheading(0)
	adjustementValue = 1*factor

	va(x + xShiftFromBaseToStructure, y + heightBase, saloonTurtle)
	draw_rectangle(lengthMainStructure/3 - adjustementValue, heightMainStructure/6, (115, 86, 58), saloonTurtle)

	saloonTurtle.setheading(0)
	va(xBottomLeftCornerDoor + widthDoor + adjustementValue, y + xShiftFromBaseToStructure, saloonTurtle)
	draw_rectangle(lengthMainStructure/3 - adjustementValue, heightMainStructure/6, (115, 86, 58), saloonTurtle)
	
	# --- Draw the doors on the middle of the saloon --- #
	widthMoveableDoor = widthDoor*0.46

	# Left door #
	saloonTurtle.setheading(0)
	draw_door(xBottomLeftCornerDoor, y + heightDoor*0.38, widthMoveableDoor, heightDoor/2, factor, saloonTurtle)

	# Right door #
	saloonTurtle.setheading(0)
	draw_door(xBottomLeftCornerDoor + widthDoor - widthMoveableDoor, y + heightDoor*0.38, widthMoveableDoor, heightDoor/2, factor, saloonTurtle)

def draw_many_saloons(saloonTurtle):
	x = -650
	y = -400
	coords = (x, y)
	draw_saloon(coords[0], coords[1], 1.2, saloonTurtle)
	saloonTurtle.setheading(0)
	x += 400 * 1.2 + 50
	coords = (x, y)
	draw_saloon(coords[0], coords[1], 1, saloonTurtle)
	saloonTurtle.setheading(0)
	x += 400 * 1 + 50
	coords = (x, y)
	draw_saloon(coords[0], coords[1], 0.8, saloonTurtle)
	saloonTurtle.setheading(0)
	coords = (0, 50)
	draw_saloon(coords[0], coords[1], 0.6, saloonTurtle)
	saloonTurtle.setheading(0)
	x = 400 * 0.6 + 20
	coords = (x, 50)
	draw_saloon(coords[0], coords[1], 0.4, saloonTurtle)

	update()

######################################## DEBUT TEST 

# height = 1080
# width = 1920

# screen = Screen()
# screen.setup(width, height)

# tracer(False)
# hideturtle()
# colormode(255)

#draw_many_saloons()

#draw_saloon(-200, -200, 1, saloonTurtle)
#draw_saloon(-500, -425, 2, saloonTurtle)

#update()

#exitonclick()

######################################## FIN TEST





