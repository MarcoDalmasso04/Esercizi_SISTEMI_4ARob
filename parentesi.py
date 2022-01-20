#1) chiedere stringa utente
#2) ciclo stringa per eliminare i caratteri che non sono parentesi (), [], {}
#3) logica: se trovo parentesi aperta paccio pusch, altrimenti faccio pop cotrollo che siano dello stesso tipo

stringa = input("Inserisci stringa: ")
DEFAULT = "abc(stp[xy{}o]p)"

def eliminoCaratteri(stringa):
    nuova = ""
    for carattere in stringa:
        if carattere == '(' | carattere == ')' | carattere == '[' | carattere == ']' | carattere == '{' | carattere == '}':
            nuova = nuova + carattere
    return nuova

