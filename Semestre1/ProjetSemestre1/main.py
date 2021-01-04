#coding: utf-8
'''
Groupe 1 : Jaime Alba Pastor et Raphael Anjou
'''

# --- Imports --- #
from drawingFunctions import *
from drawScene import draw_background, draw_message
from gameFunctions import *

from random import randrange
from time import sleep

# --- Initialize variables --- #
lengthScreen = 1200
heightScreen = 600
factor = 1

xForBench = -lengthScreen/20
yForBench = -heightScreen/2.7
lengthBench = 600 * factor

# --- Initialize turtle modules --- #
hideturtle()
tracer(False)
title("Jeu de quilles fun et amusant !")
setundobuffer(0)
draw_background(lengthScreen, heightScreen, xForBench, yForBench, lengthBench, factor)

# --- MOTEUR DU JEU --- #

nbInitial = randrange(5,6)                 #Tirer un nombre aléatoire de quilles
nbDeQuilles = nbInitial

quilles=[[0,nbInitial-1]]

bottleAlreadyShot = []

bottleAlreadyShot = afficheQuilles(quilles, nbInitial, xForBench, yForBench, lengthBench, bottleAlreadyShot, factor)

gagnant = False

while not gagnant:                              #Tant qu'il n'y a pas de gagnant :
    
    #Faire jouer le joueur
    draw_message(lengthScreen, heightScreen, "C'est ton tour!")
    choix = joueurJoue(quilles)
    jouer(choix, quilles)
    
    bottleAlreadyShot = afficheQuilles(quilles, nbInitial, xForBench, yForBench, lengthBench, bottleAlreadyShot, factor)      #Afficher les quilles
    
    nbDeQuilles = compterQuilles(quilles)            #Mettre à jour le nombre de quilles
    #print("Il y a",nbDeQuilles,"quilles")
    
    if nbDeQuilles == 0:                           #S'il n'y a plus de quilles : le joueur a gagné
        draw_message(lengthScreen, heightScreen, "Tu as gagné!")
        gagnant = True
    
    else:
        draw_message(lengthScreen, heightScreen, "Le robot joue!")      #S'il reste des quilles : 
        jouer(ordiJoue(quilles),quilles)                    #Faire jouer l'ordinateur

        bottleAlreadyShot = afficheQuilles(quilles, nbInitial, xForBench, yForBench, lengthBench, bottleAlreadyShot, factor)  #Afficher les quilles
        
        nbDeQuilles = compterQuilles(quilles)               #Mettre à jour le nombre de quilles
        print("Il y a",nbDeQuilles,"quilles")
        
        if nbDeQuilles == 0:                                #S'il n'y a plus d'allumettes, l'ordinateur a gagné                      
            draw_message(lengthScreen, heightScreen, "Tu as perdu!") 
            gagnant = True
        
exitonclick()

