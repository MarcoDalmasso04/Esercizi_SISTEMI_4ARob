#le liste sono mutabili

lista = [3, 3.1415, "ciao"]#lista eterogenea, fatta di tipi diversi
print(lista)
print(lista[-1])#stampo l'ultimo elemento
numeri_primi = [2, 3, 5, 7, 11, 13]#lista omogenea
print(numeri_primi)

lista[1] = 2.645 #posso farlo perchè sono mutabili
print(lista)

numeri_primi.append(17) #aggiungere un elemento alla lista
print(numeri_primi)
print(f"La lunghzza è {len(numeri_primi)}") #len serve per calcolare la lunghezza della lista

altri_numeri_primi = [19, 23, 29]
molti_numeri_primi = numeri_primi + altri_numeri_primi #concatenare stringe
print(molti_numeri_primi)

print(5 * altri_numeri_primi) #ripete la lista 5 volte