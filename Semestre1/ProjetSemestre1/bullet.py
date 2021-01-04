'''
Fichier permettant de dessiner les balles de pistolet
'''

from drawingFunctions import *
from turtle import *
from math import atan, radians, degrees, ceil
from time import sleep

def draw_bullet(lengthBulletBody, widthBulletBody, turtleDrawing):
	
	# --- Draw the body of the bullet --- #

	#We can't use our rectangle function because we would need to specify the turtle drawing everywhere else
	turtleDrawing.color(219, 176, 57)
	turtleDrawing.begin_fill()

	for loop in range(2):
		turtleDrawing.fd(lengthBulletBody)
		turtleDrawing.left(90)
		turtleDrawing.fd(widthBulletBody)
		turtleDrawing.left(90)

	turtleDrawing.end_fill()

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
	tracer(0)

def shoot_bullet(xStart, yStart, xDestination, yDestination, factor, factorSizeBottle, turtleDrawing):

	# --- Initialize the size of the bullet --- #
	lengthBulletBodyStart = 100 * factor * factorSizeBottle
	widthBulletBodyStart = 50 * factor * factorSizeBottle

	# --- Go to the start of the trajectory, find the distance from the start to the target, calculate the distance needed to be traveled for each steps --- #
	turtleDrawing.up()
	turtleDrawing.goto(xStart, yStart)
	turtleDrawing.down()

	waypoint = turtleDrawing.position() #Create a waypoint to remember the starting coordinates for each iteration of the bullet 
	distanceToTarget = turtleDrawing.distance(xDestination, yDestination)
	steps = 10
	distancePerStep = distanceToTarget / steps

	# --- Initialize the distance traveled and the number of steps traveled as well as the factor used to determine the size of the bullet --- #
	traveledDistance = 0
	countStep = 0
	sizeChanger = 1
	
	# --- While the bullet has not reached the target : --- #
	while traveledDistance <= (distanceToTarget - lengthBulletBodyStart*steps*0.025):

		# --- Place the turtle on the last waypoint --- #

		turtleDrawing.up()
		turtleDrawing.goto(waypoint[0], waypoint[1])
		turtleDrawing.down()

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

		# --- Draw the bullet and go back to the waypoint --- #

		draw_bullet(lengthBulletBody, widthBulletBody, turtleDrawing)

		turtleDrawing.up()
		turtleDrawing.goto(waypoint[0], waypoint[1])
		turtleDrawing.down()

		# --- Orientate the turtle on the right direction and make a step closer to the target --- #
		turtleDrawing.up()

		turtleDrawing.setheading(direction)
		turtleDrawing.fd(distancePerStep)
	
		turtleDrawing.down()

		# --- Update the waypoint --- #
		waypoint = turtleDrawing.position()

		# --- Increment the distance traveled by the turtle and the number of steps taken. Reduce the size a little bit more because the turtle is going further away --- #
		traveledDistance += distancePerStep
		countStep += 1
		sizeChanger -= 0.025

		# --- Update the screen and delete the previous iteration of the bullet --- #
		update()
		delay(25)
		turtleDrawing.clear()

	# --- #
