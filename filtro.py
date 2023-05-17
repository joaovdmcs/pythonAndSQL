def pares(i):
	if i%2==0:
		return i


lista = list(range(1,11))

listaPares = list(filter(pares, lista))

print(lista,listaPares)
