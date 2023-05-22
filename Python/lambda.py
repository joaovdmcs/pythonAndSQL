def dobro(x):
	return(x+x)
	
valor = list(range(1,6))

valorDobrado = list(map(lambda x: x+x, valor))

print(valorDobrado)

#dobro pode ser substituida pela funcao lambda
