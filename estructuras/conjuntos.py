class Nodo:
    def __init__(self, dato):
        self.sig = None
        self.dato = dato

class Conjunto:
    def __init__ (self):
        self.cabeza = None

    def contiene (self, elemento):
        actual = self.cabeza
        while actual:
            if actual.dato == elemento:
                return True
            actual = actual.sig
        return False
    
    def agregar (self, elemento):
       if not self.contiene(elemento):
           nuevo = Nodo(elemento)
           nuevo.sig = self.cabeza
           self.cabeza = nuevo
    
    def mostrar (self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.sig
        return elementos
    
    def union (self, otro):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.sig
        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.sig

        return resultado
    
    def interseccion (self, otro):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            if otro.contiene(actual.dato):
                resultado.agregar(actual.dato)
            
            actual = actual.sig

        return resultado
    
    def diferencia(self, otro):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            if not otro.contiene(actual.dato):
                resultado.agregar(actual.dato)
            
            actual = actual.sig

        return resultado
    
    def diferencia_simetrica(self, otro):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            if not otro.contiene(actual.dato):
                resultado.agregar(actual.dato)
            
            actual = actual.sig
        
        actual = otro.cabeza
        while actual:
            if not self.contiene(actual.dato):
                resultado.agregar(actual.dato)
            
            actual = actual.sig
                
        return resultado
    
    def subconjunto(self, otro):
        actual = self.cabeza
        while actual:
            if not otro.contiene(actual.dato):
                return False
            actual = actual.sig
        return True
    
    def subconjunto2(self, otro):
        actual = otro.cabeza
        while actual:
            if not self.contiene(actual.dato):
                return False
            actual = actual.sig
        return True
    
    def superconjunto(self, otro):
        return otro.subconjunto(self)
    
    def superconjunto2(self, otro):
        return otro.subconjunto2(self)
   
    

