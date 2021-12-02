f = open("./numeriPrimi.txt", "w")

def isPrimo(n):
    ok = True
    i = 2
    while ok == True & i < n:
        if n % i == 0:
            ok = False
        i = i + 1;
    return ok;
n = 2;
while num < n:
    if isPrimo(n):
        f.write(str(n))
        n = n + 1;
    num = num + 1;
f.close()
        
