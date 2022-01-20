n = int(input("Inserisci un numero: "))

def divisioneDue(n):
    ok = False
    if n % 2 == 0:
        ok = True
    return ok

def divisioneTre(n):
    ok = False
    if n % 3 == 0:
        ok = True
    return ok

def divisioneCinque(n):
    ok = False
    if n % 5 == 0:
        ok = True
    return ok

if divisioneDue(n):
    if divisioneTre(n):
        if divisioneCinque(n):
            print("Numero divisibile per 2, 3, 5.")
        else:
            print("Numero divisibile per 2, 3.")
    else:
        print("Numero divisible per 2.")
elif divisioneTre(n):
    if divisioneCinque(n):
        print("Numero divisibile per 3, 5.")
    else:
        print("Numero divisibile per 3.")
elif divisioneCinque(n):
    print("Numero divisibile per 5.")
else:
    print("Numero non divisibile per 2, 3, 5.")
