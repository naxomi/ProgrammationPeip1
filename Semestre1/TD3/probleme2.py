''' Problème 2 '''

n = int(input("Quel nombre voulez-vous transformer ? : "))
b = int(input("En quelle base ? : "))

answer = str(n%b)

while n // b != 0:
    n = n // b
    answer = str(n % b) + answer
    
print(answer)