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

def ganar(tabla,pieza):
    #Ubicacion horizontal para ganar
    for c in range(Columna_contador-3):
        for f in range(Fila_contador):
            if tabla [f][c]==pieza and tabla [f][c+1] == pieza and tabla[f][c+2]== pieza and tabla[f][c+3] == pieza:
                return True

    #ubicacion vertical para ganar
    for c in range(Columna_contador):
        for f in range(Fila_contador-3):
            if tabla [f][c]==pieza and tabla [f+1][c] == pieza and tabla[f+2][c]== pieza and tabla[f+3][c] == pieza:
                return True

    #Pendiente Positiva
    for c in range(Columna_contador-3):
        for f in range(Fila_contador - 3):
            if tabla[f][c] == pieza and tabla[f + 1][c + 1] == pieza and tabla[f + 2][c + 2] == pieza and tabla[f + 3][
                c + 3] == pieza:
                return True

    #Pendiente Negativa
    for c in range(Columna_contador-3):
        for f in range(3, Fila_contador):
            if tabla[f][c] == pieza and tabla[f - 1][c + 1] == pieza and tabla[f - 2][c + 2] == pieza and tabla[f - 3][
                c + 3] == pieza:
                return True


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

letra = pygame.font.SysFont("helvetica",75)

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
            pygame.draw.rect(screen, NEGRO, (0,0,ancho,cuadrados))

            #print(event.pos)


            #Jugador 1
            if turno == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/cuadrados))

                if ubicacion(tabla,col):
                    fila = s_fila(tabla,col)
                    pieza(tabla, fila, col, 1)

                    if ganar(tabla,1):
                        frase = letra.render("¡Gana Jugador 1!",1,ROJO)
                        screen.blit(frase,(40,10))
                        game_over = True

            #Jugador 2
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / cuadrados))

                if ubicacion(tabla, col):
                    fila = s_fila(tabla, col)
                    pieza(tabla, fila, col, 2)

                    if ganar(tabla, 2):
                        frase = letra.render("¡Gana Jugador 2!", 1, AZUL)
                        screen.blit(frase, (40, 10))
                        game_over = True


            nueva_tabla(tabla)
            dibujar(tabla)

            turno += 1
            turno = turno%2

            if game_over:
                pygame.time.wait(100000)
