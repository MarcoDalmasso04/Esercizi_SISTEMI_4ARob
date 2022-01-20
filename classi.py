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

p1 = Pila() #istanza della classe
p1.push("ciao")
p1.push(10)
p1.print()