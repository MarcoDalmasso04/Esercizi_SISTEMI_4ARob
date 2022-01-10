f = open("covid-19_gen1.txt","r")
righe = f.readlines()
dizionario = {}
contaA = 0
contaT = 0
contaC = 0
contaG = 0
for r in righe:
    for caraterre in r:
        if caraterre == "A":
            contaA = contaA + 1
        elif caraterre == "T":
            contaT = contaT + 1
        elif caraterre == "C":
            contaC = contaC + 1
        elif caraterre == "G":
            contaG = contaG + 1
dizionario['A'] = contaA
dizionario['T'] = contaT
dizionario['C'] = contaC
dizionario['G'] = contaG

print(dizionario)
f.close()