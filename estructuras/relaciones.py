class Par:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.sig = None

class Relacion:
    def __init__(self):
        self.cabeza = None

    def contieneP(self, a, b):
        actual = self.cabeza
        while actual:
            if actual.a == a and actual.b == b:
                return True
            actual = actual.sig
        return False

    def agregarP(self,a, b):
        if not self.contieneP(a,b):
          nuevo = Par(a,b)
          nuevo.sig = self.cabeza
          self.cabeza = nuevo

    def mostrarP(self):
        pares = []
        actual = self.cabeza
        while actual:
            pares.append(f"({actual.a}, {actual.b})")
            actual = actual.sig
        return pares
    
    def reflexiva (self, conjunto):
        elementos = conjunto.mostrar()
        for elemento in elementos:
            if not self.contieneP(elemento, elemento):
                return False
        return True
    
    def simetrica (self):
        actual = self.cabeza
        while actual:
            if not self.contieneP(actual.b, actual.a):
                return False
            actual = actual.sig
        return True
    
    def antisimetrica(self):
        actual = self.cabeza
        while actual:
           if actual.a != actual.b :
            if self.contieneP(actual.b, actual.a):
                return False
           actual = actual.sig
        return True
    
    def transitiva(self):
        actual1 = self.cabeza
        while actual1:
            actual2 = self.cabeza
            while actual2:
                if actual1.b == actual2.a:
                    if not self.contieneP(actual1.a, actual2.b):
                        return False
                actual2 = actual2.sig
            actual1 = actual1.sig
        return True
    
    def reflexiva_u(self):
     elementos = []
     actual = self.cabeza
     while actual:
        if actual.a not in elementos:
            elementos.append(actual.a)
        if actual.b not in elementos:
            elementos.append(actual.b)
        actual = actual.sig
     for e in elementos:
        if not self.contieneP(e, e):
            return False
     return True
        

