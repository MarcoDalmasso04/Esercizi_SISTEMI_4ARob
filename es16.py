nOp = int(input("Quele operazione vuoi fare: 0 = somma, 1 = sotrazione, 2 = moltiplicazione, 3 = divisione: "))

if nOp == 0:
    n1 = int(input("Inserisci primo numero: "))
    n2 = int(input("Inserisci secondo numero: "))
    somma = n1 + n2
    print(somma)
elif (nOp == 1):
    n1 = int(input("Inserisci primo numero: "))
    n2 = int(input("Inserisci secondo numero: "))
    sot = n1 - n2
    print(sot)
elif (nOp == 2):
    n1 = int(input("Inserisci primo numero: "))
    n2 = int(input("Inserisci secondo numero: "))
    mol = n1 * n2
    print(mol)
elif (nOp == 3):
    n1 = int(input("Inserisci primo numero: "))
    n2 = int(input("Inserisci secondo numero: "))
    div = n1 / n2
    print(div)

