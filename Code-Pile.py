from unicodedata import name


class Coda():
    def __init__(self):
        self.coda = []
    
    def enqueque(self, elemento):
        self.coda.append(elemento)
    
    def dequeque(self):
       if len(self.coda) != 0:
            return self.coda.pop(0)
       else:
            return None

    def print(self):
        print(self.coda)

class Pila(object):
    def __init__(self):
        self.pila = []
    
    def push(self, elemento):
        self.pila.append(elemento)
    
    def pop(self):
        if len(self.pila) != 0:
            return self.pila.pop()
        else:
            return None

    def print(self):
        print(self.pila)

def main():
    p = Pila()
    p.push(10)
    p.push(50)
    x = p.pop
    p.print()

    q = Coda()
    q.enqueque(10)
    q.enqueque(50)
    y = q.dequeque()
    q,print()

if __name__ == "__main__":
    main()
