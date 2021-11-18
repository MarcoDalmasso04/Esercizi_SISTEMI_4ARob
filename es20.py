n = int(input("Inserisci un numero: "))

ok = True

for i in range(2,n): ##n escluso
    if n % i == 0:
        ok = False;

if ok == True:
    print(f"Il numero {n} è primo. ")
else:
    print(f"Il numero {n} non è primo. ")       
