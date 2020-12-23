#!/usr/bin/env python
# coding: utf-8

# In[1]:

from drawingFunctions import *
from drawBottle import draw_bottle, test_sizes_bottle
from drawSaloon import draw_saloon, draw_many_saloons
from gameFunctions import *

from random import choice, randrange
from time import sleep
from turtle import *

hideturtle()

bottleTurtle = Turtle()

bottleTurtle.hideturtle()
tracer(False)

colormode(255)

height = 1080
width = 1920

screen = Screen()
screen.setup(width, height)

#Groupe 1 : Jaime Alba Pastor et Raphael Anjou

#        - MOTEUR DU JEU -

nbInitial = randrange(4,10)                 #Tirer un nombre aléatoire de quilles
nbDeQuilles = nbInitial

quilles=[[0,nbInitial-1]]
afficheQuilles(quilles, nbInitial, bottleTurtle)

gagnant = False

while not gagnant:                              #Tant qu'il n'y a pas de gagnant :
    
    #Faire jouer le joueur
    choix = joueurJoue(quilles)
    jouer(choix, quilles)
        
    nbDeQuilles = compterQuilles(quilles)            #Mettre à jour le nombre de quilles
    
    afficheQuilles(quilles, nbInitial, bottleTurtle)      #Afficher les quilles
    
    if nbDeQuilles == 0:                           #S'il n'y a plus de quilles : le joueur a gagné
        print("Tu as gagné!")
        sleep(5)    
        gagnant = True
    
    else:
        sleep(1)                                   #S'il reste des quilles :   
        print("Le robot joue !!!!!")
        jouer(ordiJoue(quilles),quilles)    #Faire jouer l'ordinateur
        
        nbDeQuilles = compterQuilles(quilles)        #Mettre à jour le nombre de quilles
              
        afficheQuilles(quilles, nbInitial, bottleTurtle)  #Afficher les quilles
        
        if nbDeQuilles == 0:                        #S'il n'y a plus d'allumettes, l'ordinateur a gagné                      
            print("Tu as perdu!") 
            sleep(3)
            gagnant = True
        
        

