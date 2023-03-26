import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Función para crear el tablero
def crear_tablero():
    return np.zeros((3,3,3))

# Función para imprimir el tablero en la terminal
def imprimir_tablero(tablero):
    for i in range(3):
        print('Altura', i+1)
        print(tablero[i][:][:])
        print('-')

def movimientos_posibles(tablero):
    return [(i, j, k) for i in range(3) for j in range(3) for k in range(3) if tablero[i][j][k] == 0]

def formas_ganar():
    formas = []
    # Combinaciones que atraviesan las diferentes capas del tablero
    for i in range(3):
        for j in range(3):
            # Combinaciones horizontales
            formas.append([(0, i, j), (1, i, j), (2, i, j)])
            # Combinaciones verticales
            formas.append([(i, 0, j), (i, 1, j), (i, 2, j)])
            # Combinaciones diagonales
            formas.append([(0, 0, j), (1, 1, j), (2, 2, j)])
            formas.append([(0, 2, j), (1, 1, j), (2, 0, j)])
            formas.append([(i, 0, 0), (i, 1, 1), (i, 2, 2)])
            formas.append([(i, 0, 2), (i, 1, 1), (i, 2, 0)])
    # Combinaciones que atraviesan las diferentes alturas del tablero
    for i in range(3):
        # Combinaciones horizontales
        formas.append([(i, 0, 0), (i, 0, 1), (i, 0, 2)])
        formas.append([(i, 1, 0), (i, 1, 1), (i, 1, 2)])
        formas.append([(i, 2, 0), (i, 2, 1), (i, 2, 2)])
        # Combinaciones verticales
        formas.append([(0, i, 0), (1, i, 0), (2, i, 0)])
        formas.append([(0, i, 1), (1, i, 1), (2, i, 1)])
        formas.append([(0, i, 2), (1, i, 2), (2, i, 2)])
    # Combinaciones diagonales que atraviesan las diferentes alturas del tablero
    formas.append([(0, 0, 0), (1, 1, 1), (2, 2, 2)])
    formas.append([(0, 2, 0), (1, 1, 1), (2, 0, 2)])
    formas.append([(2, 0, 0), (1, 1, 1), (0, 2, 2)])
    formas.append([(2, 2, 0), (1, 1, 1), (0, 0, 2)])
    formas.append([(0, 0, 2), (1, 1, 1), (2, 2, 0)])
    formas.append([(0, 2, 2), (1, 1, 1), (2, 0, 0)])
    formas.append([(2, 0, 2), (1, 1, 1), (0, 2, 0)])
    formas.append([(2, 2, 2), (1, 1, 1), (0, 0, 0)])
    return formas

winf=formas_ganar()

def hay_ganador3d(tablero,jugador):
    for w in winf:
        if tablero[w[0]]==tablero[w[1]]==tablero[w[2]]==jugador:
            return True
    return False

def jugador_humano(tablero):
    altur_a = int(input('Ingrese la altura: '))-1
    fil_a = int(input('Ingrese la fila: '))-1
    column_a = int(input('Ingrese la columna: '))-1
    return (altur_a, fil_a, column_a)

def jugador_ia1(tablero):
    movimientos = movimientos_posibles(tablero)
    if len(movimientos) == 0:
        return None
    return random.choice(movimientos)

def jugador_ia2(tablero):
    movimientos = movimientos_posibles(tablero)
    # Verificar si se puede ganar en la siguiente jugada
    for mov in movimientos:
        tablero[mov[0]][mov[1]][mov[2]]=-1
        if hay_ganador3d(tablero,-1) is False:
            tablero[mov[0]][mov[1]][mov[2]]=0
        else:
            
            tablero[mov[0]][mov[1]][mov[2]]=0
            return mov
    
        # Verificar si el jugador puede ganar en la siguiente jugada
    for mov in movimientos:
        tablero[mov[0]][mov[1]][mov[2]]=1
        if hay_ganador3d(tablero,1):
            tablero[mov[0]][mov[1]][mov[2]]=0
            return mov
        else:
            tablero[mov[0]][mov[1]][mov[2]]=0
    # Intentar ocupar el centro
    for i in range(3):
        if tablero[1][1][1] == 0:
            return (1, 1,1)
                
    if len(movimientos) == 0:
        return None
    return random.choice(movimientos)


def mostrar_grafico(tablero):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Configurar las etiquetas de los ejes
    ax.set_xlabel('Fila')
    ax.set_ylabel('Columna')
    ax.set_zlabel('Altura')

    # Graficar los puntos
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if tablero[k][i][j] == 1:
                    ax.scatter(i, j, k, marker='o', color='r', s=100)
                elif tablero[k][i][j] == -1:
                    ax.scatter(i, j, k, marker='x', color='b', s=100)
    ax.plot([0,2],[0,0],[0,0],'r')
    ax.plot([0,0],[0,2],[0,0],'r')
    ax.plot([0,0],[0,0],[0,2],'r')
    ax.plot([2,2],[0,0],[0,2],'r')
    ax.plot([2,2],[0,2],[0,0],'r')
    ax.plot([2,2],[2,2],[0,2],'r')
    ax.plot([2,2],[0,2],[2,2],'r')
    ax.plot([2,0],[2,2],[2,2],'r')
    ax.plot([0,0],[2,0],[2,2],'r')
    ax.plot([0,2],[0,0],[2,2],'r')
    ax.plot([0,0],[2,2],[0,2],'r')
    ax.plot([0,2],[2,2],[0,0],'r')
    # Mostrar el gráfico
    plt.savefig('img/tablero3D.png')
    plt.close()

def jugar(players):
    tablero = crear_tablero()
    jugadores = players
    turno = 0
    simbolo=-1
    while hay_ganador3d(tablero,simbolo) is False and len(movimientos_posibles(tablero)) > 0:
        imprimir_tablero(tablero)
        mostrar_grafico(tablero)
        simbolo=simbolo*-1
        print(f"Turno del jugador {turno + 1}")
        jugador = jugadores[turno]
        column_a,altur_a, fil_a = jugador(tablero)
        while tablero[column_a][altur_a][fil_a] != 0:
            print("Esa posición ya está ocupada. Por favor, ingrese otra.")
            altur_a, fil_a,column_a = jugador(tablero)
        tablero[column_a][altur_a][fil_a] = simbolo
        turno = (turno + 1) % 2
        
            
    imprimir_tablero(tablero)
    mostrar_grafico(tablero)
    ganador=hay_ganador3d(tablero,simbolo)
    if ganador is None:
        print("Empate.")
    else:
        print(f"Ganador: {simbolo}")
    return turno-1


#Inicializamos el juego
t=crear_tablero()
a=hay_ganador=hay_ganador3d(t,10)
print(a)
partidas=int(input('Numero de partidas:'))
while True:
    p1=int(input('jugador 1: 1=ia1, 2= ia2, 3= Humano: '))-1
    p2=int(input('jugador 2: 1=ia1, 2= ia2, 3= Humano: '))-1
    players=[jugador_ia1,jugador_ia2,jugador_humano]
    players=[players[p1],players[p2]]
    vitorias=0
    for a in range(partidas):
        a=jugar(players)
        vitorias=vitorias+a
    print(vitorias)
    
    jugarmas=input('Salir? (q):')
    if jugarmas=='q':
        break
vacio=crear_tablero()
mostrar_grafico(vacio)
