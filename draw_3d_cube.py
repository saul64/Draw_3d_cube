#Saul Eliseo Aparicio Vivar - 21760641

#Dibuja un cubo 3D usando la libreria de turtle
from turtle import *
import time

speed(2)
color('black')

#Funcion para dibujar caras (cubo)
def draw_square(size):
    for _ in range(4):
        forward(size)
        left(90)

#Dibujar cada frontal
draw_square(200)


pu()
goto(100, 100)
pd()

#Dibujar cara trasera
draw_square(200)


pu()
goto(200, 0)
pd()
goto(300, 100)

pu()
goto(200, 200)
pd()
goto(300, 300)

pu()
goto(0, 200)
pd()
goto(100, 300)

pu()
goto(0, 0)
pd()
goto(100, 100)

time.sleep(5)