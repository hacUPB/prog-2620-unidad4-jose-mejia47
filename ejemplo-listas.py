# Lista vacía
componentes = []

# Lista con elementos
componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]

# Lista con diferentes tipos de datos
datos_vuelo = [202, "Boeing 737", True, 10500.5]

# Listas anidadas
matriz_rotacion = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]



# sub sets, (componentes)

# Indexación (comienza en 0)
print(componentes[0])  # "alas"
print(componentes[-1])  # "tren de aterrizaje" (indexación negativa)

# Slicing (rebanado)
print(componentes[1:3])  # ["fuselaje", "motores"]
print(componentes[:2])   # ["alas", "fuselaje"]
print(componentes[2:])   # ["motores", "tren de aterrizaje"]



#ejemplo 1

lista = []
# llenar la lista con 10 datos iguales

for i in range(10):
    lista.append("hola")
    print(lista)


#ejemplo 2

# llenar la lista con 3 datos ingresados por el teclado

for i in range(3):
    dato1 = int("ingrese el primer dato")
    lista.append(dato1)
print(lista)





