<<<<<<< Updated upstream
'''
Fichier test du jeu, celui pour test le bon affichage des dessins etc...
'''

from drawingFunctions import *
from bullet import shoot_bullet
from drawBottle import draw_bottle, test_sizes_bottle
from drawSaloon import draw_saloon, draw_many_saloons

from turtle import *
from turtle import TurtleScreenBase, _Screen

from time import sleep

# --- Find the size of the screen and create the ratio factor --- #

hideturtle()
#tracer(False)
colormode(255)

screen = Screen()
screen.setup(1.0, 1.0)

#print(window_width())
#print(window_height())

screenFactor = 1 #Ceci sera le facteur choisit pour que le jeu soit responsive. Il est calcule dans la fonction Sizefactor

#########################

#Just to open the screen of turtle and have time to watch the animation

# bulletTurtle = Turtle()
# bulletTurtle.hideturtle()
# bulletTurtle.tracer(False)

# va(0, 0, bulletTurtle)
# bulletTurtle.setheading(0)
# draw_rectangle(100, 100, "white", bulletTurtle)
# sleep(3)
# bulletTurtle.setheading(0)

# #########################

# va(0, -(window_height() / 2), bulletTurtle)
# bulletTurtle.color("black")
# bulletTurtle.goto(200, 200)

# #########################

# bulletTurtle = Turtle()
# bulletTurtle.hideturtle()
# bulletTurtle.tracer(False)
# shoot_bullet(0, -(window_height() / 2), 200, 200, 1, bulletTurtle)

#########################

saloonTurtle = Turtle()
saloonTurtle.hideturtle()
saloonTurtle.tracer(False)
draw_saloon(-700, -250, 1.25, saloonTurtle)
#draw_many_saloons(saloonTurtle)

#########################

bancTurtle = Turtle()
bancTurtle.hideturtle()
bancTurtle.tracer(False)
va(-160, -175, bancTurtle)
lengthTable = 850
draw_rectangle(lengthTable, 25, "brown", bancTurtle)

#########################

bottleTurtle = Turtle()
bottleTurtle.hideturtle()
bottleTurtle.tracer(False)
#draw_bottle(0, -150, 0.6, bottleTurtle)

#test_sizes_bottle(bottleTurtle)

#########################

# def organizeBottle(numberOfBottle, lengthTable, widthBottle, factor):
# 	# --- On sait que le nombre minimum de bouteilles est 5 et le nombre maximum de bouteilles 15 --- #

# 	factorSizeBottle = 0.5 + numberOfBottle*0.03

# 	return factorSizeBottle, intervalBetweenBottle

#########################
#########################

#FONCTION TRES IMPORTANTE !!!!!!!
#PERMET DE CREER LES QUILLES DE FACON ORGANISE PEUT IMPORTE LE NOMBRE

x = -160
y = -150

numberOfBottle = 15
factor = 1

widthBottleOriginal = 90 * factor
factorSizeBottle = 0.8 - (numberOfBottle-5)*0.03

widthBottleModified = widthBottleOriginal * factorSizeBottle
intervalBetweenBottle = (lengthTable - widthBottleModified * numberOfBottle) / (numberOfBottle + 1)

x += intervalBetweenBottle

for loop in range(numberOfBottle):
	draw_bottle(x, y, factorSizeBottle, bottleTurtle)
	x += intervalBetweenBottle + widthBottleModified

#########################
#########################

#half_grid()

#bulletTurtle = Turtle()
#bulletTurtle.hd()
#bulletTurtle.tracer(False)
#bullet(0, 0, 1, bulletTurtle)

update()

#turtle.undo()
=======
# --- Imports --- #
from turtle import *
>>>>>>> Stashed changes

from drawBottle import draw_bottle, draw_broken_bottle
from drawSaloon import draw_saloon
from drawNature import draw_mountain, draw_tree_1, draw_tree_2, draw_bench
from drawingFunctions import va, draw_rectangle


def draw_message(lengthScreen,heightScreen, message):
    x = lengthScreen*7/32
    y = heightScreen*5/16
    
    va(x,y)
    setheading(0)
    draw_rectangle(lengthScreen/4, heightScreen/8, (251, 200, 46))
    va(x,y)
    setheading(0)
    draw_rectangle(lengthScreen/4, heightScreen/8,"Navy",False)
    
    va(x+lengthScreen/8, y+heightScreen/32)
    setheading(0)
    write(message, False, align="center", font=("Playbill", 20, "normal"))
    print(message)
    
    update()
    
def draw_background(lengthScreen, heightScreen, xForBench, yForBench, lengthBench, factor=1):
    # --- Initialize turtle modules --- #
    screen = Screen()
    screen.setup(lengthScreen,heightScreen)
    hideturtle()
    tracer(False)
    
    # --- Draw background colors --- #
    va(-lengthScreen/2, -heightScreen/2)
    draw_rectangle(lengthScreen, heightScreen*2/3,"SandyBrown")
    va(-lengthScreen/2, heightScreen/6)
    draw_rectangle(lengthScreen, heightScreen/3, "LightSkyBlue")
    
    # --- Draw mountains --- #
    for loop in range(6):
        x = -lengthScreen/2 + loop*lengthScreen/6
        draw_mountain(x, heightScreen/8, lengthScreen/6, True)
        
    for loop in range (7):
        x = - lengthScreen*27/48 + loop*lengthScreen/6
        draw_mountain(x, heightScreen/9, lengthScreen/8)
        
    # --- Draw trees --- #
    nb = 15
    for loop in range(nb+1):
        x = -lengthScreen/2 + loop*lengthScreen/nb
        draw_tree_1(x, 0, heightScreen/10)
    
    nb = 8
    for loop in range(nb):
        x = -lengthScreen/2 +lengthScreen/20 + loop*lengthScreen/nb
        draw_tree_2(x, 0, heightScreen/11)
    
    # --- Draw saloon --- #
    draw_saloon(-lengthScreen*3/7, -heightScreen*2/5,0.95*factor)
    
    # --- Draw bench --- #
    draw_bench(xForBench, yForBench, lengthBench)