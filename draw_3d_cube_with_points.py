#Saul Eliseo Aparicio Vivar - 21760641
#Dibuja un cubo utilizando una funcion con puntos usando coordenadas

from turtle import *
import time

speed(3)

# Función para dibujar líneas con puntos entre dos coordenadas
def draw_3d_cube_with_points(x1, y1, x2, y2, step=5):
    pu()
    goto(x1, y1)
    dx = x2 - x1
    dy = y2 - y1
    distance = (dx ** 2 + dy ** 2) ** 0.5
    steps = int(distance / step)

    for i in range(steps + 1):
        dot(4, "black")  # Tamaño y color del punto
        x = x1 + (dx * i / steps)
        y = y1 + (dy * i / steps)
        goto(x, y)

# Coordenadas de los vértices del cubo
vertices = [
    # Cara frontal
    (0, 0),     #0 
    (200, 0),   #1
    (200, 200), #2
    (0, 200),   #3
    
    # Cara trasera
    (100, 100), #4
    (300, 100), #5
    (300, 300), #6
    (100, 300)  #7
]

# Caras frontales y traseras
edges = [
    # Cara frontal
    (0, 1),    #(0,0) - (200,0)
    (1, 2),    #(200,0) - (200,200)
    (2, 3),    #(200, 200) - (0,200)
    (3, 0),    #(0, 200) - (0,0)


    # Cara trasera
    (4, 5),   #(100, 100) - (300, 100)
    (5, 6),   #(300, 100) - (300, 300)
    (6, 7),   #(300, 300) - (100, 300)
    (7, 4),   #(100, 300) - (100, 100)

    # Conexiones entre ambas caras
    (0, 4),   #(0,0) - (100,100)
    (1, 5),   #(200, 0) - (300, 100)
    (2, 6),   #(200,200) - (300,300)
    (3, 7)    #(0,200) - (100,300)
]

# Dibujar el cubo usando la función de puntos
for start, end in edges:
    draw_3d_cube_with_points(vertices[start][0], vertices[start][1], vertices[end][0], vertices[end][1])

time.sleep(5)