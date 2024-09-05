import turtle
import random

# Configurar la pantalla
screen = turtle.Screen()
screen.bgcolor("black")

# Configurar la tortuga
pen = turtle.Turtle()
pen.speed(0)  # Velocidad máxima para dibujo rápido
pen.width(2)  # Ancho de la línea

# Función para cambiar a un color aleatorio
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# Función para dibujar un espirógrafo más grande
def draw_large_spirograph(radius, size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        pen.color(random_color())  # Cambiar a un color aleatorio
        pen.circle(radius)  # Dibujar un círculo con un radio mayor
        pen.setheading(pen.heading() + size_of_gap)  # Cambiar la orientación de la tortuga

# Llamada a la función para dibujar el espirógrafo grande
draw_large_spirograph(200, 5)

# Cerrar la ventana al hacer clic
screen.exitonclick()
