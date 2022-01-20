def enqueque(coda, elemento):
    coda.append(elemento)

def dequeque(coda):
    if len(coda) != 0:
        return coda.pop(0)
    else:
        print("Coda vuota.")

##coda = [0, 1, 2, 3, 4]
##        ^           ^
##        |           |
##       head        tail

coda = []

n = int(input("Inserisci quanti numeri vuoi: "))
for _ in range(0, n):
    enqueque(coda, int(input("Inserisci un numero: ")))
print(coda)
for _ in range(0, n):
    print(dequeque(coda))


