string = "contemporaneamente"

print(f"Prima lettera = {string[0]} | ultima lettera = {string[-1]}")
print(f"Parola senza prima e ultima lettera = " + string[1:-1])
print(f"Parola alternando le lettere 1 a 1 = " + string[::2])
print(f"Parola al contrario = " + string[::-1])

string_nuova = string[0:3] + "?" + string[4:]
print(f"Parola con ? al terzo carattere = " + string_nuova)

