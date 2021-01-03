# --- Imports --- #
from turtle import *

from drawBottle import draw_bottle, draw_broken_bottle
from drawSaloon import draw_saloon
from drawNature import draw_mountain, draw_tree_1, draw_tree_2, draw_bench
from drawingFunctions import va, draw_rectangle


def draw_message(length,height, message):
    x = length*7/32
    y = height*5/16
    
    va(x,y)
    setheading(0)
    draw_rectangle(length/4,height/8, "Yellow")
    va(x,y)
    setheading(0)
    draw_rectangle(length/4,height/8,"Navy",False)
    
    va(x+length/8,y+height/32)
    setheading(0)
    write(message, False, align="center", font=("Playbill", 20, "normal"))
    print(message)
    
    update()
    
def draw_background(length=1200,height=600,factor=1):
    # --- Initialize turtle modules --- #
    screen = Screen()
    screen.setup(length,height)
    hideturtle()
    tracer(False)
    
    # --- Draw background colors --- #
    va(-length/2,-height/2)
    draw_rectangle(length, height*2/3,"SandyBrown")
    va(-length/2,height/6)
    draw_rectangle(length, height/3, "LightSkyBlue")
    
    # --- Draw mountains --- #
    for loop in range(6):
        x = -length/2 + loop*length/6
        draw_mountain(x,height/8,length/6, True)
        
    for loop in range (7):
        #x = -length/2 - (length/6 - length*5/48) + loop*length/6
        x = - length*27/48 + loop*length/6
        draw_mountain(x,height/9,length/8)
        
    # --- Draw trees --- #
    nb = 15
    for loop in range(nb+1):
        x = -length/2 + loop*length/nb
        draw_tree_1(x, 0, height/10)
    
    nb = 8
    for loop in range(nb):
        x = -length/2 +length/20 + loop*length/nb
        draw_tree_2(x, 0, height/11)
    
    # --- Draw saloon --- #
    draw_saloon(-length*3/7,-height*2/5,0.95*factor)
    
    # --- Draw bench --- #
    draw_bench(length/20,-height/4, 400*factor)