"""
Fichier permettant de dessiner les elements de la nature
"""

from turtle import *
from drawingFunctions import *

def draw_mountain(x, y, base, sombre=False):
    # --- Initialize variables --- #
	hauteur=base

	# --- Draw the structure --- #
	if sombre:
		couleur = "Grey"
	else:
		couleur = "DarkGrey"
	draw_triangle_isocele(x, y, base, hauteur, couleur)

	# --- Change the position and color of the turtle --- #
	color("snow")
	va(x+base/2, y+hauteur)

	# --- Draw the top snow --- #
	begin_fill()

	Y = y + (5/8)*hauteur
	goto((Y-y+2*x)/2, Y)
	goto(x+base*5/12, y+hauteur*11/16)
	goto(x+base/2, y+hauteur*9/16)
	goto(x+base*7/12, y+hauteur*11/16)
	goto((y+2*x+2*base-Y)/2, Y)
	#goto(x+base/2,y+hauteur)

	end_fill()
	# --- End drawing --- #

def draw_tree_trunk(x, y, hauteur):
	va(x,y)
	draw_rectangle(hauteur/15, hauteur, "SaddleBrown")

def draw_cercle(x, y, rayon, couleur):
	# --- Initialize the position and color of the turtle --- #
	color(couleur)
	va(x, y)

	# --- Start drawing --- #
	begin_fill()
	circle(rayon)
	end_fill()
	# --- End drawing --- #

def draw_tree_1(x, y, hauteur, couleur="ForestGreen"):
    # --- Draw trunk --- #
	draw_tree_trunk(x, y, hauteur)

    # --- Draw leaves --- #
	draw_cercle(x+hauteur/30, y+hauteur/3, hauteur*0.55, couleur)
	draw_cercle(x+hauteur/30, y+hauteur*0.9, hauteur*0.45, couleur)
	draw_cercle(x+hauteur/30, y+hauteur*1.5, hauteur*0.3, couleur)
    # --- End drawing --- #


def draw_tree_2(x, y, hauteur, couleur="YellowGreen"):
    # --- Draw trunk --- #
	draw_tree_trunk(x,y,hauteur)

    # --- Draw leaves --- #
	draw_triangle_isocele(x+hauteur/30-hauteur*1.25/2, y+hauteur/3, hauteur*1.25, hauteur*1.25, couleur)
	draw_triangle_isocele(x+hauteur/30-hauteur/2, y+hauteur*0.8, hauteur, hauteur, couleur)
	draw_triangle_isocele(x+hauteur/30-hauteur*0.8/2, y+hauteur*1.2, hauteur*0.8, hauteur*0.8, couleur)
    # --- End drawing --- #

def draw_bench(x, y, lengthBench):
    draw_round_rectangle(x, y, lengthBench, lengthBench/24, lengthBench/48, "Sienna")
    draw_round_rectangle(x+lengthBench*2/10, y-lengthBench/11, lengthBench/47, lengthBench/10, lengthBench/120, "Sienna")
    draw_round_rectangle(x+lengthBench*8/10, y-lengthBench/11, lengthBench/47, lengthBench/10, lengthBench/120, "Sienna")