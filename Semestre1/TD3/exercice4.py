''' Exercice 4 '''

mini = int(input("Nombre minimum : "))
maxi = int(input("Nombre maximum : "))

while mini != maxi:
    if mini % 2 == 0:
        print(mini)
    mini += 1