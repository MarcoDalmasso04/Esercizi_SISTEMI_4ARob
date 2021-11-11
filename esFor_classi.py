classi = ["4arob", "3arob", "5arob", "4achi", "3ainf"]
indirizzi = {"rob" : "Smart-rob", "chi" : "Chimica", "inf" : "Informatica"}

#indice = 0

for indice, classe in enumerate(classi):#ciclo sulla posizione e sul contenuto
    indice = indice + 1
    #indirizzo = indirizzi[classe[-3:]]
    print(f"Posizione {indice} nella lista: ")
    print(f"La classe {classe} è dell'indirizzo {indirizzo}", end = "\n\n")