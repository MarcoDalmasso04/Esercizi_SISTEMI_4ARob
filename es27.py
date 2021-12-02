lista = ["otto", "ciao", "comeemoc", "Casa", "letto", "Telefono"]
palindrome = []
letMaiusc = []

for parola in lista:
    if parola[0].isupper() == True:
        letMaiusc.append(parola)
    else:
        if parola == parola[::-1]:
            palindrome.append(parola)

print(palindrome)
print(letMaiusc) 

#palindroma = [parola for parola in lista if parola == parla[::-1]]
#letMaiusc = [parola for parola in lista if (parola[0] >= 'A' & parola[0] <= 'Z')]


            
