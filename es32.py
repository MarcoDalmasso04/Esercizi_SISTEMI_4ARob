griglia = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}

def disegnoGriglia(griglia):
    print(f"{griglia[0]} | {griglia[1]} | {griglia[2]} ")
    print(f"{griglia[3]} | {griglia[4]} | {griglia[5]} ")
    print(f"{griglia[6]} | {griglia[7]} | {griglia[8]} ")

def isPieno(griglia):
    ok = True
    for chaive in griglia:
        if griglia[chaive] != " ":
            ok = False
    return ok

def controlloVincitore(griglia):
    ok = True
    if (str(griglia[0]) != " ") & (str(griglia[0]) == str(griglia[1]) == str(griglia[2])):
        ok = False
    elif (str(griglia[3]) != " ") & (str(griglia[3]) == str(griglia[4]) == str(griglia[5])):
        ok = False
    elif (str(griglia[6]) != " ") & (str(griglia[6]) == str(griglia[7]) == str(griglia[8])):
        ok = False
    elif (str(griglia[0]) != " ") & (str(griglia[0]) == str(griglia[3]) == str(griglia[6])):
        ok = False
    elif (str(griglia[1]) != " ") & (str(griglia[1]) == str(griglia[4]) == str(griglia[7])):
        ok = False
    elif (str(griglia[2]) != " ") & (str(griglia[2]) == str(griglia[5]) == str(griglia[8])):
        ok = False
    elif (str(griglia[0]) != " ") & (str(griglia[0]) == str(griglia[4]) == str(griglia[8])):
        ok = False
    elif (str(griglia[2]) != " ") & (str(griglia[2]) == str(griglia[4]) == str(griglia[6])):
        ok = False
    elif isPieno(griglia):
        ok = False
    return ok

while (True):
    condizione = True
    while condizione == True:
        n = int(input("Giocatore 1 --> Inserisci posizione da [0 a 8]: "))
        if (n < 0) or (n > 8):
            condizione = True
        elif griglia[n] != " ":
            print("POSIZIONE OCCUPATA.")
            condizione = True
        else:
            griglia[n] = input("Inserisci carattere [X]: ")
            condizione = False
    
    disegnoGriglia(griglia)

    if controlloVincitore(griglia) == False:
        print("Ha vinto giocatore 1.")
        break

    condizione = True    
    while condizione == True:
        n = int(input("Giocatore 2 --> Inserisci posizione da [0 a 8]: "))
        if (n < 0) or (n > 8):
            condizione = True
        elif griglia[n] != " ":
            print("POSIZIONE OCCUPATA.")
            condizione = True
        else:
            griglia[n] = input("Inserisci carattere [O]: ")
            condizione = False

    disegnoGriglia(griglia)

    if controlloVincitore(griglia) == False:
        print("Ha vinto giocatore 2.")
        break
        
