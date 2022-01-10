f = open("main.txt", "r")
righe = f.readlines()
numeroRighe = len(righe)
contaPrintf, contaCommenti = 0, 0

for parola in righe:
        caraPrint = 0
        parolaPrintf = ""
        caraComm = 0
        commento = ""
        for lettera in parola:
            if lettera == "p":
                for c in range (0, 6):
                    parolaPrintf = parolaPrintf + lettera[c]
            if lettera == "/":
                for k in range(0, 2):
                    commento = commento + lettera[k]  
        if(parolaPrintf == "printf"):
            contaPrintf = contaPrintf + 1
        if(commento == "//"):
            contaCommenti = contaCommenti + 1
print(f"Numero di righe: " +  {numeroRighe} + "Numero di printf: " + {contaPrintf} + "Numero di commenti: " + {contaCommenti})
f.close()