def sommeCarre(n):
    if n < 0:
        somme = -1
    else:
        somme = 0
        for number in range(0,n+1):
            somme += number**2        
    return somme
            
def polynome(x, a, b, c):
    return a*(x**2) + b*x + c

def colle(a,b):
    return a+":"+b

print(colle("bon",colle("a","b")))