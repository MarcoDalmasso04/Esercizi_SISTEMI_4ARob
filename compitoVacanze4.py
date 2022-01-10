def disegnaGriglia(griglia):
    print(" 0   1   2   3   4   5   6")
    print(f" {griglia[0]} | {griglia[1]} | {griglia[2]} | {griglia[3]} | {griglia[4]} | {griglia[5]} | {griglia[6]}")
    print(f"---+---+---+---+---+---+---")
    print(f" {griglia[7]} | {griglia[8]} | {griglia[9]} | {griglia[10]} | {griglia[11]} | {griglia[12]} | {griglia[13]}")
    print(f"---+---+---+---+---+---+---")
    print(f" {griglia[14]} | {griglia[15]} | {griglia[16]} | {griglia[17]} | {griglia[18]} | {griglia[19]} | {griglia[20]}")
    print(f"---+---+---+---+---+---+---")
    print(f" {griglia[21]} | {griglia[22]} | {griglia[23]} | {griglia[24]} | {griglia[25]} | {griglia[26]} | {griglia[27]}")
    print(f"---+---+---+---+---+---+---")
    print(f" {griglia[28]} | {griglia[29]} | {griglia[30]} | {griglia[31]} | {griglia[32]} | {griglia[33]} | {griglia[34]}")
    print(f"---+---+---+---+---+---+---")
    print(f" {griglia[35]} | {griglia[36]} | {griglia[37]} | {griglia[38]} | {griglia[39]} | {griglia[40]} | {griglia[41]}")
    print("\n\n\n\n")

griglia = []

for _ in range(0, 42):
    griglia.append(' ')

def controllo(griglia, posizione, c):
    ok = False
    n = 7
    while ok == False & n < 42:
        if griglia[posizione] != ' ':
            print("posizione non valida.")
        elif ((griglia[posizione + n] == ' ') & (griglia[posizione + n * 2] != ' ')):
            ok = True
        else: 
            ok = False
            n = n + n
    if ok == True:
        griglia[n] = c
    return ok

while(True):
    ok1 = False
    ok2 = False
    while ok1 == False:
        c1 = 'X'
        n1 = int(input("Giocatore1 : Inserisci posizione pedina = "))
        ok = controllo(griglia, n1, c1)
        if ok == False:
            ok1 = False
        else:
            ok1 = True
    disegnaGriglia(griglia)
    
    while ok2 == False:
        c2 = 'O'
        n2 = int(input("Giocatore2: Inserisci posizione pedina = "))
        ok = controllo(griglia, n2, c2)
        if ok == False:
            ok2 = False
        else:
            ok2 = True
    disegnaGriglia(griglia)

    
