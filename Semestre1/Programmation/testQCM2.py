def factorielle(n):
	
	if n >= 0:
		somme = 1

		for number in range(n):
			somme *= (number + 1)
	else:
		somme = -1

	return somme

def proc(x):
	x += 1

print(proc(3))