def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("Inserisci un numero limite: "))
    x = 0
    fib = 0
    while fib < n:
        fib = fibonacci(x)
        print(fib)
        x += 1

if __name__ == "__main__":
    main()