lista = ["ciao", "casetta", "macchina", "motorino"]
lung = 0;
par = ""
for elemento in lista:
    
    if lung > len(elemento):
        par = elemento;

print(par)