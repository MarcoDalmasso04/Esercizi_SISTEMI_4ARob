lista = ["ciao", 45, "casa", 8, 9, 10, "scuola"]
dizionario = {}
k = 0
#dizionario = {x: elemento for x, elemento in enumerate(lista)} #dictionary comprension
for elemento in lista:# for k, elemento in enumerate(lista)
    dizionario[k] = elemento;
    k = k + 1
    #dizionario[k] = elemento
print(dizionario)