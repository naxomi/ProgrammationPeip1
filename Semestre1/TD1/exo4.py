''' Exercice 4 '''

''' Version "legit" '''

initiales = str(input("Donnez vos initiales : "))
line = int(input("Nombre de lignes : "))
column = int(input("Nombre de columns : "))

#Create the first and last lines at the same time because they are the same
firstAndLastLines = (initiales + " ") * (column - 1) + initiales
#Create one line from in between the ends
inBetweenLine = (initiales + (" " * (column - 1) + (" " * (column - 2)) * len(initiales)) + initiales)

print(firstAndLastLines)
print((inBetweenLine + "\n") * (line - 3) + inBetweenLine) 
print(firstAndLastLines)

''' Version "tricheur" '''

initiales = str(input("Donnez vos initiales : "))
line = int(input("Nombre de lignes : "))
column = int(input("Nombre de colonnes : "))

for loop in range(line):
    if loop % (line - 1) == 0:
        print((initiales + " ") * (column - 1) + initiales)
    else:
        print(initiales + (" " * (column - 1) + (" " * (column - 2)) * len(initiales)) + initiales)
