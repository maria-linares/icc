import os
import numpy as np
import pygame
import sys
import math

VERDE=(0,250,0)
NEGRO=(0,0,0)
ROJO =(255,0,0)
AZUL = (0,0,255)
#Numero de filas y columnas
Fila_contador = 6
Columna_contador = 7

def crear_tabla(): #Crea la tabla de fondo (matriz)
    tabla = np.zeros((Fila_contador,Columna_contador))
    return tabla

def pieza(tabla, fila, col, pieza): #La pieza de cada jugador
    tabla[fila][col] = pieza

def ubicacion(tabla, col): #Ubica del tablero
    return tabla[Fila_contador-1][col]==0

def s_fila(tabla, col): #siguiente fila
    for f in range (Fila_contador):
        if tabla[f][col]==0:
            return f

def nueva_tabla(tabla): #Tabla con principio de coordenas invertido
    print(np.flip(tabla, 0))


def dibujar(tabla):
    #Dibuja la tabla y los circulos negros como si fueran vacios
    for c in range(Columna_contador):
        for f in range (Fila_contador):
            pygame.draw.rect(screen, VERDE, (c*cuadrados, f*cuadrados+cuadrados, cuadrados, cuadrados))
            pygame.draw.circle(screen, NEGRO, (int(c*cuadrados+cuadrados/2), int(f*cuadrados+cuadrados+cuadrados/2)),radio)

    #Dibuja los circulos que son las piezas para jugar para cada jugador
    for c in range(Columna_contador):
        for f in range (Fila_contador):
            if tabla[f][c] == 1:
                pygame.draw.circle(screen, ROJO,
                           (int(c * cuadrados + cuadrados / 2), alto-int(f * cuadrados + cuadrados / 2)),
                           radio)
            elif tabla[f][c] == 2:
                pygame.draw.circle(screen, AZUL,
                           (int(c * cuadrados + cuadrados / 2), alto-int(f * cuadrados + cuadrados / 2)),
                           radio)
    pygame.display.update()



tabla=crear_tabla()
nueva_tabla(tabla)
game_over = False
turno=0

pygame.init()

#Tamaño de un lado del cuadrado
cuadrados = 100

#Tamaño de toda la tabla
ancho = Columna_contador*cuadrados
alto = (Fila_contador+1)*cuadrados
tamaño = (ancho,alto)

radio=int((cuadrados/2) - 5)

screen = pygame.display.set_mode(tamaño)
dibujar(tabla)
pygame.display.update()


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, NEGRO, (0,0,ancho,cuadrados))
            posx = event.pos[0]
            if turno == 0:
                pygame.draw.circle(screen, ROJO, (posx,int(cuadrados/2)),radio)
            else:
                pygame.draw.circle(screen, AZUL, (posx, int(cuadrados / 2)), radio)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)


            #Jugador 1
            if turno == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/cuadrados))

                if ubicacion(tabla,col):
                    fila = s_fila(tabla,col)
                    pieza(tabla, fila, col, 1)
            #Jugador 2
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / cuadrados))

                if ubicacion(tabla, col):
                    fila = s_fila(tabla, col)
                    pieza(tabla, fila, col, 2)

            print(nueva_tabla(tabla))
            dibujar(tabla)

            turno += 1
            turno = turno%2
