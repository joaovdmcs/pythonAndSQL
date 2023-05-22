import random

numero = random.randint(0,10)
print(numero)

random.seed(1)
numero2 = random.randint(0,10)
print(numero2)
random.seed()

lista = [6,45,9]
numero3 = random.choice(lista)
print(numero3)