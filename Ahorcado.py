#Ahorcado proyecto.
#Importar las herramientas que sirven para cambiar de color los textos impresos.
import colors
#Importar las herramientas que sirven para crear tiempos de espera.
import time
#Importar las herramientas que sirven para principal (Limpiar pantalla).
import os
print('Bienvenido al juego del ahorcado ')
#Empieza el ciclo while que contendra las 10 palabras.
start=input('Quieres empezar el juego?')
#v son las vidas, o intentos que tendra el jugador para completar la palabra.
v=7
if start=='si':
    while start=='si':
        print('La primera preguanta es /n ')
else:
    print('Entiendo que no estes list@ para empezar es un desafio dificil :)')
    start=input('Ya estas list@ para empezar?')
#p sera la variable para guardar una letra que sustituira un epacio de la palabra si son iguales.
p=input('Cual es la letra que eliges?')
