import math

x = int(input("Inserisci coordinata x del primo punto: "))
y = int(input("inserisci coordinata y del primo punto: "))
x1 = int(input("Inserisci coordinata x del secondo punto: "))
y1 = int(input("inserisci coordinata y del secondo punto: "))

punto1 = (x, y)
punto2 = (x1, y1)

distanza = math.sqrt((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2)

print(f"Distanza euclidea tra di due punti inseriti = {distanza}")

