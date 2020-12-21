''' Exercice 2 '''

tableAReviser = int(input("Quelle table voulez-vous réviser ? : "))
valeurMax = int(input("Jusqu'à quelle valeur ? : "))

print(f"Révision de la table de {tableAReviser} jusqu'à {valeurMax}")

i = 1

while i <= valeurMax:
    print(f"{i} fois {tableAReviser} = {i * tableAReviser}")
    i += 1
    
print("Fin de la révision.")

''' Exercice 3 '''

n = int(input("Vous voulez faire la factorielle de ... ? : "))

factorielle = 1

x = 1

while n != 1:
    factorielle *= n
    n -= 1
    
print(factorielle)

''' Exercice 4 '''

mini = int(input("Nombre minimum : "))
maxi = int(input("Nombre maximum : "))

while mini != maxi:
    if mini % 2 == 0:
        print(mini)
    mini += 1

''' Exercice 5 '''

from random import randint

print("Salut ! Vous avez 6 coups pour deviner le chiffre determine au hasard et compris entre 1 et 100.")

nombreADeviner = randint(1,100)
n = 1
nombrePropose = int(input("Ecris un nombre :"))

while nombrePropose != nombreADeviner:
 	if nombrePropose > nombreADeviner:
 			print("Le nombre est plus petit")
 	elif nombrePropose < nombreADeviner:
         print("Le nombre est plus grand")
 	n += 1
 	if n > 6:
	    print("Vous avez perdu, le nombre était : {0}".format(nombreADeviner))
	    break
 	nombrePropose = int(input("Ecris un autre nombre :"))
else:
 	print("Vous avez gagne ! Le nombre etait {0} et vous l'avez devine en {1} coup(s)".format(nombreADeviner,n))
    
''' Exercice 6 '''
    
from turtle import *

length = int(input("Longueur du côté du carré : "))

for steps in range(4):
    forward(length)
    left(90)
    
''' Exercice 7 '''

from turtle import *

length = int(input("Longueur du côté du triangle équilatéral : "))

for steps in range(3):
    forward(length)
    left(120)

''' Exercice 8 '''

from turtle import *

length = int(input("Longueur du côté de l'hexagone : "))

for steps in range(6):
    forward(length)
    left(60)

''' Exercice 9 '''

from turtle import *

length = int(input("Longueur du côté du carré : "))
nombreCarre = int(input("Nombre de carrés à dessiner : "))

x = -350
y = -300

up()
goto(x,y)
down()

# --- Version 1 ---
for loop in range(nombreCarre):
    for steps in range(4):
        fd(length)
        left(90)
    x += length
    y += length
    
    up()
    goto(x,y)
    down()

# --- Version 2 ---
for loop in range(nombreCarre):
    for steps in range(6):
        fd(length)
        left(90)
    right(180)

''' Problème 1  '''

from turtle import *
import turtle
up()

window = turtle.Screen()

hauteur = window_height()
largeur = window_width()

hauteur = 720
largeur = 675

print(largeur, hauteur)

longMarche = int(input("Longueur des marches : "))
largMarche = int(input("Largeur des marches : "))
nbMarche = int(input("Nombre de marches : "))

turtle.goto(int(-(largeur-20) / 2), int((hauteur-20) / 2))
turtle.write("Départ")

print("hey")

turtle.done()
turtle.bye()

window.exitonclick()

''' Problème 2 '''

n = int(input("Quel nombre voulez-vous transformer ? : "))
b = int(input("En quelle base ? : "))

answer = str(n%b)

while n // b != 0:
    n = n // b
    answer = str(n % b) + answer
    
print(answer)
    
''' Problème 3 '''

from turtle import *

nbCotePoly = int(input("Nombre de côtés : "))
coteExterieur = int(input("Longueur des côtés : "))
nbPolygone = int(input("Nombre de polygones : "))
f = float(input("Facteur de rétrécissement des côtés : "))

for polygone in range(nbPolygone):
    for cote in range(nbCotePoly):
        forward(coteExterieur)
        left(360/coteExterieur)
        
    
    
    
    
    
    