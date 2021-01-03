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
length = 1200
height = 600
factor = 1


# --- Initialize turtle modules --- #
hideturtle()
tracer(False)
draw_background(length, height, factor)

# --- MOTEUR DU JEU --- #

nbInitial = randrange(5,15)                 #Tirer un nombre aléatoire de quilles
nbDeQuilles = nbInitial

quilles=[[0,nbInitial-1]]
afficheQuilles(quilles, nbInitial, length, height, factor)

gagnant = False

while not gagnant:                              #Tant qu'il n'y a pas de gagnant :
    
    #Faire jouer le joueur
    draw_message(length, height, "C'est ton tour!")
    choix = joueurJoue(quilles)
    jouer(choix, quilles)
    
    afficheQuilles(quilles, nbInitial, length, height, factor)      #Afficher les quilles
    
    nbDeQuilles = compterQuilles(quilles)            #Mettre à jour le nombre de quilles
    print("Il y a",nbDeQuilles,"quilles")
    
    if nbDeQuilles == 0:                           #S'il n'y a plus de quilles : le joueur a gagné
        draw_message(length, height, "Tu as gagné!")
        gagnant = True
    
    else:
        draw_message(length, height, "Le robot joue!")      #S'il reste des quilles : 
        sleep(2)
        jouer(ordiJoue(quilles),quilles)                    #Faire jouer l'ordinateur

        afficheQuilles(quilles, nbInitial, length, height, factor)  #Afficher les quilles
        
        nbDeQuilles = compterQuilles(quilles)               #Mettre à jour le nombre de quilles
        print("Il y a",nbDeQuilles,"quilles")
        
        if nbDeQuilles == 0:                                #S'il n'y a plus d'allumettes, l'ordinateur a gagné                      
            draw_message(length, height, "Tu as perdu!") 
            gagnant = True
        
exitonclick()

