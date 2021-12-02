n = 1000
lista = []

def isPrimo(n):
    ok = True
    i = 2
    while ok == True & i < n:
        if n % i == 0:
            ok = False
        i = i + 1;
    return ok;

def contaPrimi(n):
    for i in range(2, n):
        if isPrimo(i) == True:
            lista.append(i)
    return lista;

lista = contaPrimi(n)

print(lista)

##primi = [k for k in range(2, 1003) if isPrimo(k)]