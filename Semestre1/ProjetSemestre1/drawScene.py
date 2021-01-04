# --- Imports --- #
from turtle import *

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