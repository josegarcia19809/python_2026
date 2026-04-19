tamano_matriz = 3
matriz_a = [[3, 1, -4],
            [2, -3, 1],
            [5, -2, 0]]
matriz_b = [[1, -2, -1],
            [0, 5, 4],
            [-1, -2, 3]]

resultado = [[0] * tamano_matriz for r in range(tamano_matriz)]

# Multiplicar las matrices
for fila in range(tamano_matriz):
    for columna in range(tamano_matriz):
        for i in range(tamano_matriz):
            resultado[fila][columna] += matriz_a[fila][i] * matriz_b[i][columna]

# Imprimir el resultado
for fila in range(tamano_matriz):
    print(matriz_a[fila], matriz_b[fila], resultado[fila])
print()
