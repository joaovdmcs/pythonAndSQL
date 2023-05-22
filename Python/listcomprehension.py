x = [1 , 2, 3, 4, 5]
y = []


for i in x:
	y.append(i**2)
	

# y = [valor_a_adicionar laço condição]

z = [i**2 for i in x] #simplificação do procedimento realizado em y

print(x)
print(y)
print(z)
 
w = [i for i in x if i%2==0]	

print(w) #itens pares de x
