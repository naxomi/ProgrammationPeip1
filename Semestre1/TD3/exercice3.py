''' Exercice 3 '''

n = int(input("Vous voulez faire la factorielle de ... ? : "))

factorielle = 1

x = 1

while n != 1:
    factorielle *= n
    n -= 1
    
print(factorielle)