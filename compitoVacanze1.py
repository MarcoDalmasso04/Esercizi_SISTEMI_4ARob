lista = [1, 5, 5, 2, 76, 2, 1, 76, 3, 0, 1]
lista_nuova = []
def eliminaDoppi(l):
    for k in range(len(l) - 1):
        j = k + 1
        while j < len(l):
            if l[k] == l[j]:
                l = l[:j] + l[j + 1:]
                j = j - 1
            j = j + 1
    return l
lista_nuova = eliminaDoppi(lista)
print(lista_nuova)