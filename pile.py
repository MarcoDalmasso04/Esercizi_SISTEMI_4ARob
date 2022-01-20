
def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    return pila.pop()

n = int(input("Quanti numeri vuoi inserire? "))
pila = []
for _ in range (0, n):
    push(pila, int(input("Inserisci un numero: ")))
print(pila)    
for _ in range (0, n):
    print(pila.pop())