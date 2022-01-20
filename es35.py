def fattoriale(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fattoriale(n - 1)

def main():
    n = int(input("Inserisci un numero: "))
    fat = fattoriale(n)
    print(f"Il fattoriale di {n} è: {fat}")

if __name__ == "__main__":
    main()