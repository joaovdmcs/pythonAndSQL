from functools import reduce 
def soma(x,y):
	return (x+y)
lista = [1,3,5,10,20,7,7]

somaVal = reduce(soma,lista)

print(somaVal)
