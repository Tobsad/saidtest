# MULTIPLICACION DE MATRICES BIDIMENSIONALES 

# Pedimos al usuario que ingrese los valores de la primera matriz
matriz1 = []
print("===========")
print("Matriz Nº1:")
print("===========")
#Como nos piden un arreglo bidimensional hacemos un recorrido para 2 valores en i y en j:
for i in range(2):
    fila = []
    for j in range(2):
        valor = int(input(f"Ingrese el valor para la posición ({i}, {j}) de la matriz Nº1: "))
        fila.append(valor)
    matriz1.append(fila)
print(matriz1)

# Pedimos al usuario que ingrese los valores de la segunda matriz
matriz2 = []
print("===========")
print("Matriz Nº2:")
print("===========")
#Como nos piden un arreglo bidimensional hacemos un recorrido para 2 valores en i y en j:
for i in range(2):
    fila = []
    for j in range(2):
        valor = int(input(f"Ingrese el valor para la posición ({i}, {j}) de la matriz Nº2: "))
        fila.append(valor)
    matriz2.append(fila)

print(matriz2)

#inicializamos una matriz donde ira la suma de matrices:

multiplicacion=[[0,0],[0,0]]

#agregamos las matrices 1 y 2:

for i in range (2):
    for j in range (2):
        multiplicacion[i][j]= matriz1[i][j]*matriz2[i][j]

#Imprimimos la multiplicacion de matrices:

print(f"La multiplicacion de matrices es: {multiplicacion}")