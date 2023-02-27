# Definimos las dos matrices
matriz1 = [[1, 2], [3, 4]]


matriz2 = [[5, 6], [7, 8]]

# Creamos una matriz vacía para almacenar la suma
suma = [[0, 0], [0, 0]]

# Realizamos la suma de las dos matrices
for i in range(2):
    for j in range(2):
        suma[i][j] = matriz1[i][j] + matriz2[i][j]

# Imprimimos la matriz resultante
print(suma)