'''
Fichier permettant de dessiner les balles de pistolet
'''

from drawingFunctions import *
from turtle import *
from math import atan, radians, degrees, ceil
from time import sleep

def draw_bullet(lengthBulletBody, widthBulletBody, countStep, factor, turtleDrawing):
	
	# --- Draw the body of the bullet --- #
	draw_rectangle(lengthBulletBody, widthBulletBody, (219, 176, 57), turtleDrawing)

	# --- Go to the top right corner of the bullet body (necessary to start drawing the head) --- #
	turtleDrawing.up()
	turtleDrawing.fd(lengthBulletBody)
	turtleDrawing.down()

	# --- Draw the bullet head --- #
	turtleDrawing.color(163, 70, 40)
	turtleDrawing.begin_fill()
	turtleDrawing.circle(widthBulletBody / 2, 180)
	turtleDrawing.end_fill()

	# --- #
	update()

def shoot_bullet(xStart, yStart, xDestination, yDestination, factor, turtleDrawing):

	# --- Initialize the size of the bullet --- #
	lengthBulletBodyStart = 100
	widthBulletBodyStart = 50

	# --- Go to the start of the trajectory, find the distance from the start to the target, calculate the distance needed to be traveled for each steps --- #
	va(xStart, yStart, turtleDrawing)
	waypoint = turtleDrawing.position()
	distanceToTarget = turtleDrawing.distance(xDestination, yDestination)
	steps = 60
	distancePerStep = distanceToTarget / steps

	# --- Initialize the distance traveled and the number of steps traveled as well as the factor used to determine the size of the bullet --- #
	traveledDistance = 0
	countStep = 0
	sizeChanger = 1
	
	# --- While the bullet has not reached the target : --- #
	while traveledDistance <= distanceToTarget:

		# --- Update the length and width of the bullet --- #
		lengthBulletBody = lengthBulletBodyStart * sizeChanger
		widthBulletBody = widthBulletBodyStart * sizeChanger

		# --- Set the right orientation for the turtle to go straight to the target --- #
		turtleDrawing.setheading(0)
		direction = turtleDrawing.towards(xDestination, yDestination)
		turtleDrawing.setheading(direction)

		# --- Move the turtle to be centered on the line going directly from the start to the target --- #
		turtleDrawing.right(90)
		turtleDrawing.fd(widthBulletBody / 2)
		turtleDrawing.left(90)

		# --- Draw the bullet and go back to the coordinates of the start of the drawing--- #
		draw_bullet(lengthBulletBody, widthBulletBody, countStep, 1, turtleDrawing)
		va(waypoint[0], waypoint[1], turtleDrawing)

		# --- Orientate the turtle on the right direction and make a step closer to the target --- #
		turtleDrawing.setheading(direction)
		turtleDrawing.fd(distancePerStep)
		waypoint = turtleDrawing.position()

		# --- Increment the distance traveled by the turtle and the number of steps taken. Reduce the size a little bit more since the turtle is going further away --- #
		traveledDistance += distancePerStep
		countStep += 1
		sizeChanger -= 0.01

		# --- Update the screen and delete the previous iteration of the bullet --- #
		update()
		delay(50)
		turtleDrawing.clear()
