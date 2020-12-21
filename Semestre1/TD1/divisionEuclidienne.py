''' Exercice 2 '''

v1 = int(input("Donnez l'entier à diviser : "))
v2 = int(input("Donnez le diviseur : "))
print("Division euclidienne de {0} par {1} : ".format(v1,v2))
print(v1, "=", v1 // v2, "*", v2, "+", v1 % v2)