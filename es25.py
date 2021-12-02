s = input("Inserisci una parola: ")

x = lambda s: True if s[0] == s[0].isupper else False

if x(s):
    print("La parola inizia con una lettera maiuscola. ")
else:
    print("La parola non inizia con una lettera maiuscola")