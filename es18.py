lista = []
risp = "s"
while(risp == "s"):
    n = int(input("Inserisci un numero: "))
    lista.append(n)
    risp = input("Ne vuoi ancora? Rispindi [s/n]: ")

print(lista)