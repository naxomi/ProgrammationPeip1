''' Exercice 2 '''

tableAReviser = int(input("Quelle table voulez-vous réviser ? : "))
valeurMax = int(input("Jusqu'à quelle valeur ? : "))

print(f"Révision de la table de {tableAReviser} jusqu'à {valeurMax}")

i = 1

while i <= valeurMax:
    print(f"{i} fois {tableAReviser} = {i * tableAReviser}")
    i += 1
    
print("Fin de la révision.")