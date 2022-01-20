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

p1 = Coda()
p1.enqueque(10)
p1.enqueque("ciao")
p1.print() 