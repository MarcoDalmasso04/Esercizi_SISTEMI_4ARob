f = open("./persona.txt", "w")

dizionario = {}
dizionario["nome"] = input("Inserisci un nome: ")
dizionario["cognome"] = input("Inserisci un cognome: ")
dizionario["giorno"] = int(input("Inserisci giorno di nascita: "))
dizionario["mese"] = int(input("Inserisci mese di nascita: "))
dizionario["anno"] = int(input("Inserisci anno di nascita: "))

for chiave in dizionario:
    f.write(str(dizionario[chiave]) + " ")
f.close()
