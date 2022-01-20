import turtle
import random

Stella=turtle.Turtle()
window = turtle.Screen()

def Disegno_stella(x,y):
    Stella.penup()
    Stella.setposition(x,y)#setta la posizione di partenza
    Stella.pendown()
    Stella.speed(30)#velocità
    for _ in range(5): #disegno stella
        Stella.forward(280)
        Stella.right(144)

for _ in range(50):
    Disegno_stella(random.randint(-480,480),random.randint(-480,480))
window.exitonclick()