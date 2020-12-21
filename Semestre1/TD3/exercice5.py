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