#Saul Eliseo Aparicio Vivar - 21760641
#Dibuja líneas con el algoritmo de Bresenham

import turtle as t
import time

def calculate_steps(x1, y1, x2, y2):
    """Calcula los pasos necesarios y las diferencias en X y Y para el algoritmo de Bresenham."""
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    return dx, dy, sx, sy, err

def draw_point_at_position(x, y, size):
    """Dibuja un punto en la posición (x, y) con un tamaño dado."""
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.dot(size)

def draw_dotted_line(x1, y1, x2, y2, dot_size=3):
    """Dibuja una línea de puntos utilizando el algoritmo de Bresenham modificado."""
    dx, dy, sx, sy, err = calculate_steps(x1, y1, x2, y2)
    
    while True:
        draw_point_at_position(x1, y1, dot_size)
        
        if x1 == x2 and y1 == y2:
            break
        
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

def draw_multiple_dotted_lines():
    """Dibuja varias líneas utilizando puntos."""
    t.speed(0)

    # Definir las coordenadas de las líneas
    lines = [
        ((100, 100), (0,100)), #linea horizontal
        ((100, 50), (100,100)) #linea vertical
    ]

    # Dibujar cada línea de puntos
    for start, end in lines:
        draw_dotted_line(start[0], start[1], end[0], end[1], dot_size=5)

draw_multiple_dotted_lines()
time.sleep(5) 
