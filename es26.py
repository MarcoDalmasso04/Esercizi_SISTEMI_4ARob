s = input("Inserisci una parola: ")

x = lambda s: True if s == s[::-1] else False

if x(s):
    print("La parola è palindroma. ")
else:
    print("La parola non è palindroma. ")