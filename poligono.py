import turtle

n = int(input("Inserisci numero di lati del poligono: "))

pol = turtle.Turtle()
schermo = turtle.Screen()

def disegno(turtle, N, L):    
    for l in range(N):          
        turtle.forward(L)
        turtle.left(360/N)  

disegno(pol, n, 50)

schermo.exitonclick()





