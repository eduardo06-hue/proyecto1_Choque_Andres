from estructuras.conjuntos import Conjunto
from estructuras.relaciones import Relacion
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RUTA_JSON = os.path.join(BASE_DIR, "datos", "conjuntos.json")


class ConjuntoModel:
    def __init__(self):
        self.conjuntoA = Conjunto()
        self.conjuntoB = Conjunto()
        self.relacion = Relacion()
        self.relacion_u = Relacion()
    
    # Metodos de conjuntos

    def agregar_a_A(self, elemento):
        self.conjuntoA.agregar(elemento)
    
    def agregar_a_B(self, elemento):
        self.conjuntoB.agregar(elemento)

    def get_A(self):
        return self.conjuntoA.mostrar()
    
    def get_B(self):
        return self.conjuntoB.mostrar()
    
    def union(self):
        return self.conjuntoA.union(self.conjuntoB).mostrar()
    
    def interseccion(self):
        return self.conjuntoA.interseccion(self.conjuntoB).mostrar()
    
    def diferencia(self):
        return self.conjuntoA.diferencia(self.conjuntoB).mostrar()
    
    def diferencia_simetrica(self):
        return self.conjuntoA.diferencia_simetrica(self.conjuntoB).mostrar()
    
    def subconjunto(self):
        return self.conjuntoA.subconjunto(self.conjuntoB)
    
    def subconjunto2(self):
        return self.conjuntoA.subconjunto2(self.conjuntoB)
    
    def superconjunto(self):
        return self.conjuntoA.superconjunto(self.conjuntoB)
    
    def superconjunto2(self):
        return self.conjuntoA.superconjunto2(self.conjuntoB)

    def limpiar_A(self):
        self.conjuntoA = Conjunto()

    def limpiar_B(self):
        self.conjuntoB = Conjunto()

    # Métodos de relaciones
    def _cargar_pares(self, conjunto):
        elementos = conjunto.mostrar()
        for a in elementos:
            for b in elementos:
                self.relacion.agregarP(a, b)

    def get_p_a(self):
        self._cargar_pares(self.conjuntoA)
        return self.relacion.mostrarP()
    
    def get_p_b(self):
        self._cargar_pares(self.conjuntoB)
        return self.relacion.mostrarP()
    
    def limpiar_p(self):
        self.relacion = Relacion()
    
    def es_reflexiva(self, cual):
        if cual == "A":
            self._cargar_pares(self.conjuntoA)
            return self.relacion.reflexiva(self.conjuntoA)
        else:
            self._cargar_pares(self.conjuntoB)
            return self.relacion.reflexiva(self.conjuntoB)
        
    def es_simetrica(self, cual):
        if cual == "A":
            self._cargar_pares(self.conjuntoA)
        else:
            self._cargar_pares(self.conjuntoB)
        
        return self.relacion.simetrica()
    
    def es_antisimetrica(self, cual):
        if cual == "A":
            self._cargar_pares(self.conjuntoA)
        else:
            self._cargar_pares(self.conjuntoB)
        
        return self.relacion.antisimetrica()
    
    def es_transitiva(self, cual):
        if cual == "A":
            self._cargar_pares(self.conjuntoA)
        else:
            self._cargar_pares(self.conjuntoB)
        
        return self.relacion.transitiva()
    
    # ── Métodos para par por el usuario ───────────────────────────────────────────────
    def agregar_par_usuario(self, a, b):
     self.relacion_u.agregarP(a, b)

    def get_pares_usuario(self):
      return self.relacion_u.mostrarP()

    def limpiar_pares_usuario(self):
     self.relacion_u = Relacion()

    def es_reflexiva_u(self):
     return self.relacion_u.reflexiva_u()

    def es_simetrica_u(self):
     return self.relacion_u.simetrica()

    def es_antisimetrica_u(self):
     return self.relacion_u.antisimetrica()

    def es_transitiva_u(self):
     return self.relacion_u.transitiva()
    
    # ── JSON ───────────────────────────────────────────────────────────────
    def guardar(self):
     datos = {
        "conjuntoA": self.conjuntoA.mostrar(),
        "conjuntob": self.conjuntoB.mostrar(),
        "relacion_u": self.relacion_u.mostrarP()
     }
     with open(RUTA_JSON, "w") as f:
        json.dump(datos, f, indent=4)

    def cargar(self):
      try:
        with open(RUTA_JSON, "r") as f:
            datos = json.load(f)
        for e in datos["conjuntoA"]:
            self.conjuntoA.agregar(e)
        for e in datos["conjuntoB"]:
            self.conjuntoB.agregar(e)
        for par in datos["relacion_u"]:
            par = par.replace("(", "").replace(")", "")
            partes = par.split(",")
            a = partes[0].strip()
            b = partes[1].strip()
            self.relacion_u.agregarP(a, b)
      except:
        pass
