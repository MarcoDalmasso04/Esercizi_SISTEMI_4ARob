import turtle

f = open("comandi.txt", "w")

fiocco = turtle.Turtle()
sfondo = turtle.Screen()
fiocco.speed(10)

righe = f.readlines()
for riga in righe:
    lista = riga.split(":")
    
def Giro(fiocco, grado, x, y):
    fiocco.goto(x,y)
    fiocco.right(grado)

def diagonali(fiocco, grado):
    fiocco.right(grado)
    fiocco.forward(30)
    fiocco.backward(30)
    fiocco.left(grado * 2)
    fiocco.forward(30)
    fiocco.backward(30)
    fiocco.right(grado)

for _ in range(8):
    fiocco.forward(120)
    f.write("forward:120\n")
    fiocco.backward(30)
    f.write("backward:30\n")
    diagonali(fiocco,45)
    f.write("diagonali(fiocco,45)\n")
    fiocco.backward(30)
    f.write("backward:30\n")
    diagonali(fiocco,45)
    f.write("diagonali(fiocco,45)\n")
    fiocco.backward(30)
    f.write("backward:30\n")
    diagonali(fiocco,45)
    f.write("diagonali(fiocco,45)\n")
    Giro(fiocco,45,0,0)
    f.write("Giro(fiocco:45,0,0)\n")
sfondo.exitonclick()
f.close()