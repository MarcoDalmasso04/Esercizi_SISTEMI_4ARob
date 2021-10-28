#slicing di stringhe ovvero come si tagliano le stringhe
stringa = "Classe quarta A robotica"

#stringa[15] = "B"
#stringa[15] = "B" --> non posso farlo, le stringhe sono immbutabili {TypeError: 'str' object does not support item assignment}

stringa_nuova = stringa[0:14] + "B" + stringa[15:]
print(f"La stringa modificata è : {stringa_nuova}")

print(f"Il primo carattere è {stringa[0]}")
print(f"L'ultimo carattere è {stringa[-1]}")

#stampa i caratteri dallo 0 al 6 escluso
print(stringa[0:6])
print(stringa[6:])
print(stringa[:-2])
print(stringa[2:14:2])#stampa i caratteri dal 2 al 13 a balzi di 2
print(stringa[::-1])#stampa i caratteri al contrario

