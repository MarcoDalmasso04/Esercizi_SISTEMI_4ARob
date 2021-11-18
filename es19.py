lista = [5, 8, 92, -11, 52, 21, 7, 3, -8]

max = 0
min = 1000

for n in lista:
    if n > max:
        max = n

for n in lista:
    if n < min:
        min = n

print(f"Valore massimo: {max}")
print(f"Valore minimo: {min}")
