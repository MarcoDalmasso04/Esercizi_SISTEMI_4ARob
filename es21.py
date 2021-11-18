n = 1000
conta = 0

for i in range(2, n):
    ok = True
    for k in range(2, i):
        if i % k == 0:
            ok = False
    if ok == True:
        conta = conta + 1

print(f"Numero di num primi minori di 1000 = {conta}")