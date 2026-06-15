# EXAMEN T3 - Laberinto del ratón usando Backtracking

matriz = [
    ['F', 1, 1, 1, 0, 1, 1, 1, 1],
    [-2, 0, 0, -1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, -1, 0, 0, 0, -1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [-1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 0],
    ['I', 1, -1, 1, 1, 1, 0, 1, 1]
]

filas = 9
columnas = 9

# Posición inicial (I)
fila_inicio = 8
columna_inicio = 0

# Posición final (F)
fila_final = 0
columna_final = 0

vidas_iniciales = 3

# Matriz para guardar el camino encontrado
solucion = [[0 for j in range(columnas)] for i in range(filas)]

# Matriz de visitados
visitado = [[False for j in range(columnas)] for i in range(filas)]


def es_valido(fila, columna):
    """Verifica si una posición es válida"""

    if fila < 0 or fila >= filas:
        return False

    if columna < 0 or columna >= columnas:
        return False

    if matriz[fila][columna] == 0:
        return False

    if visitado[fila][columna]:
        return False

    return True


def costo_vidas(valor):
    """Calcula cuántas vidas pierde"""

    if valor == -1:
        return 1

    if valor == -2:
        return 2

    return 0


def resolver(fila, columna, vidas):

    print("Posición:", (fila, columna), " Vidas:", vidas)

    visitado[fila][columna] = True
    solucion[fila][columna] = 1

    # Si llegó a F
    if fila == fila_final and columna == columna_final:
        return True

    # Orden solicitado:
    # abajo, derecha, arriba, izquierda
    movimientos = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]

    for df, dc in movimientos:

        nueva_fila = fila + df
        nueva_columna = columna + dc

        if es_valido(nueva_fila, nueva_columna):

            vidas_restantes = vidas

            valor = matriz[nueva_fila][nueva_columna]

            vidas_restantes -= costo_vidas(valor)

            # Mientras tenga al menos 1 vida puede seguir
            if vidas_restantes > 0:

                if resolver(nueva_fila, nueva_columna, vidas_restantes):
                    return True

    # Backtracking
    solucion[fila][columna] = 0
    visitado[fila][columna] = False

    return False


print("LABERINTO ORIGINAL\n")

for fila in matriz:
    print(fila)

print("\nRECORRIDO DEL RATON\n")

encontrado = resolver(
    fila_inicio,
    columna_inicio,
    vidas_iniciales
)

if encontrado:

    print("\nSE ENCONTRO UN CAMINO VALIDO\n")

    print("MATRIZ SOLUCION\n")

    for fila in solucion:
        print(fila)

else:

    print("\nNO EXISTE UN CAMINO VALIDO")