def main():
    n = int(input("Inserisci numero alunni: "))
    f = open("cognomi.csv", "w")
    for _ in range(0, n):
        cognome = input("Inserisci cognome: ")
        num = len(cognome)
        nuovo_cognome = cognome[:1] +  (num - 1) * "*"
        voto = float(input("Inserisci voto alunno: "))
        f.write(f"{nuovo_cognome}, {voto}\n")
    f.close
if __name__ == "__main__":
    main()