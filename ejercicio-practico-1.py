#ejemplo

import random
print(random.randint(2,19))

# crear una lista con 100 numero aleatorios entre 100 y 200

lista = []
for i in range(100):
    lista.append(random.randint(100,200))
    print(lista)
    mayor = max(lista)
    print(f"el número más grande de la lista es {mayor}")

# implementar la función max usando un bucle

indice = 0
may = lista[0]
while indice < 99:
    if may < lista[indice+1]:
     may = lista[indice+1]
indice += 1

print(f"el mayor calculo a mano es: {may}")





