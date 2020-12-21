'''
Fichier test du jeu, celui pour test le bon affichage des dessins
'''

from drawingFunctions import *
from drawBottle import draw_bottle, test_sizes_bottle
from drawSaloon import draw_saloon, draw_many_saloons

from turtle import *
from turtle import TurtleScreenBase, _Screen

# --- Find the size of the screen and create the ratio factor --- #

hideturtle()
tracer(False)
colormode(255)

screen = Screen()
screen.setup(1.0, 1.0)

testScreen = _Screen()
print(testScreen._root.win_width())

print(window_width())
print(window_height())

#from turtle import TurtleScreenBase
#print(TurtleScreenBase._window_size(screen))

screenFactor = 1 #Ceci sera le facteur choisit pour que le jeu soit responsive. Il est calcule dans la fonction Sizefactor

#draw_many_saloons()
#test_sizes_bottle()


x = -575
y = -200
for loop in range(10):
	draw_bottle(x, y, screenFactor)
	x += 125

#half_grid()

update()

#turtle.undo()

exitonclick()