class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.conjunto_actual = None
        self._bind_eventos()

    def _bind_eventos(self):
        # Botones de agregar
        self.view.btn_agregar_a.config(command=self.agregar_a_A)
        self.view.btn_agregar_b.config(command=self.agregar_a_B)

        # Botones de limpiar
        self.view.btn_limpiar_a.config(command=self.limpiar_A)
        self.view.btn_limpiar_b.config(command=self.limpiar_B)
        self.view.btn_limpiar.config(command = self.limpiar_p)

        # Operaciones Conjuntos
        self.view.btn_union.config(command=self.calcular_union)
        self.view.btn_interseccion.config(command=self.calcular_interseccion)
        self.view.btn_diferencia.config(command=self.calcular_diferencia)
        self.view.btn_diferencia_simetrica.config(command=self.calcular_diferencia_simetrica)
        self.view.btn_subconjunto.config(command=self.calcular_subconjunto)
        self.view.btn_subconjunto2.config(command=self.calcular_subconjunto2)
        self.view.btn_superconjunto.config(command=self.calcular_superconjunto)
        self.view.btn_superconjunto2.config(command=self.calcular_superconjunto2)

        # Boton de Par A o Par B 
        self.view.btn_p_a.config(command=self.mostrar_pares_a)
        self.view.btn_p_b.config(command=self.mostrar_pares_b)

        # Operaciones Relaciones
        self.view.btn_reflexiva.config(command = self.calcular_reflexiva)
        self.view.btn_simetrica.config(command = self.calcular_simetrica)
        self.view.btn_antisimetrica.config(command = self.calcular_antisimetrica)
        self.view.btn_transitiva.config(command = self.calcular_transitiva)

        # Operaciones para par por el usuario
        self.view.btn_agregar_par.config(command=self.agregar_par_usuario)
        self.view.btn_limpiar_par.config(command=self.limpiar_par_usuario)
        self.view.btn_reflexiva1.config(command = self.calcular_reflexiva1)
        self.view.btn_simetrica1.config(command = self.calcular_simetrica1)
        self.view.btn_antisimetrica1.config(command = self.calcular_antisimetrica1)
        self.view.btn_transitiva1.config(command = self.calcular_transitiva1)
        

    # ── Agregar ───────────────────────────────────────────
    def agregar_a_A(self):
        elemento = self.view.get_entrada_a()
        if elemento:
            self.model.agregar_a_A(elemento)
            self.view.actualizar_label_a(self.model.get_A())

    def agregar_a_B(self):
        elemento = self.view.get_entrada_b()
        if elemento:
            self.model.agregar_a_B(elemento)
            self.view.actualizar_label_b(self.model.get_B())

    # ── Limpiar ───────────────────────────────────────────
    def limpiar_A(self):
        self.model.limpiar_A()
        self.view.actualizar_label_a([])
        self.view.mostrar_resultado("—", [])

    def limpiar_B(self):
        self.model.limpiar_B()
        self.view.actualizar_label_b([])
        self.view.mostrar_resultado("—", [])

    # ── Operaciones Conjuntos───────────────────────────────────────
    def calcular_union(self):
        resultado = self.model.union()
        self.view.mostrar_resultado("A ∪ B", resultado)

    def calcular_interseccion(self):
        resultado = self.model.interseccion()
        self.view.mostrar_resultado("A ∩ B", resultado)

    def calcular_diferencia(self):
        resultado = self.model.diferencia()
        self.view.mostrar_resultado("A - B", resultado)

    def calcular_diferencia_simetrica(self):
        resultado = self.model.diferencia_simetrica()
        self.view.mostrar_resultado("A ⊕ B", resultado)

    def calcular_subconjunto(self):
        resultado = self.model.subconjunto()
        if resultado:
            self.view.mostrar_resultado("A ⊆ B", ["A si es subconjutno de B"])
        else :
            self.view.mostrar_resultado("A ⊆ B", ["A no es subconjunto de B"])

    def calcular_subconjunto2(self):
        resultado = self.model.subconjunto2()
        if resultado:
            self.view.mostrar_resultado("B ⊆ A", ["B si es subconjunto de A"])
        else:
            self.view.mostrar_resultado("B ⊆ A", ["B no es subconjunto de A"])

    def calcular_superconjunto(self):
        resultado = self.model.superconjunto()
        if resultado:
            self.view.mostrar_resultado("A ⊇ B", ["A si es superconjunto de B"])
        else:
            self.view.mostrar_resultado("A ⊇ B", ["A no es superconjunto de B"])

    def calcular_superconjunto2(self):
        resultado = self.model.superconjunto2()
        if resultado:
            self.view.mostrar_resultado("B ⊇ A", ["B si es superconjunto de A"])
        else:
            self.view.mostrar_resultado("B ⊇ A", ["B no es superconjunto de A"])

# ── Operaciones Relaciones───────────────────────────────────────
    def mostrar_pares_a(self):
        self.conjunto_actual = "A"
        resultado = self.model.get_p_a()
        self.view.actualizar_label_p(resultado)

    def mostrar_pares_b(self):
        self.conjunto_actual = "B"
        resultado = self.model.get_p_b()
        self.view.actualizar_label_p(resultado)


    def limpiar_p(self):
        self.model.limpiar_p()
        self.view.actualizar_label_p([])

    def calcular_reflexiva(self):
        if self.conjunto_actual is None:
            self.view.mostrar_resultado_r("Error", ["Seleccione un conjunto para mostrar su par definido."])
            return
        resultado = self.model.es_reflexiva(self.conjunto_actual)
        if resultado:
            self.view.mostrar_resultado_r(f"{self.conjunto_actual}", ["es reflexiva"])
        else:
            self.view.mostrar_resultado_r(f"{self.conjunto_actual}", ["no es reflexiva"])

    def calcular_simetrica(self):
        if self.conjunto_actual is None:
            self.view.mostrar_resultado_r("Error", ["Seleccione un conjunto para mostrar su par definido."])
            return
        resultado = self.model.es_simetrica(self.conjunto_actual)
        if resultado:
            self.view.mostrar_resultado_r(f"{self.conjunto_actual}", ["es simetrica"])
        else:
            self.view.mostrar_resultado_r(f"{self.conjunto_actual}", ["no es simetrica"])

    def calcular_antisimetrica(self):
        if self.conjunto_actual is None:
            self.view.mostrar_resultado_r("Error", ["Seleccione un conjunto para mostrar su par definido."])
            return
        resultado = self.model.es_antisimetrica(self.conjunto_actual)
        if resultado:
            self.view.mostrar_resultado_r(f"{self.conjunto_actual}", ["es antisimetrica"])
        else:
            self.view.mostrar_resultado_r(f"{self.conjunto_actual}", ["no es antisimetrica"])

    def calcular_transitiva(self):
        if self.conjunto_actual is None:
            self.view.mostrar_resultado_r("Error", ["Seleccione un conjunto para mostrar su par definido."])
            return
        resultado = self.model.es_transitiva(self.conjunto_actual)
        if resultado:
            self.view.mostrar_resultado_r(f"{self.conjunto_actual}", ["es transitiva"])
        else:
            self.view.mostrar_resultado_r(f"{self.conjunto_actual}", ["no es transitiva"])

    # ── Operaciones para par por el usuario ───────────────────────────────────────
    def agregar_par_usuario(self):
        val = self.view.get_par_c()
        if ","not in val:
            self.view.mostrar_resultado_ru("Error", ["Ingrese un par con el formato correcto (a,b)."])
            return
        partes = val.split(",")
        if len(partes) != 2:
            self.view.mostrar_resultado_ru("Error", ["Ingrese un par con el formato correcto (a,b)."])
            return
        a = partes[0].strip()
        b = partes[1].strip()
        self.model.agregar_par_usuario(a, b)
        self.view.actualizar_label_c(self.model.get_pares_usuario())

    def limpiar_par_usuario(self):
        self.model.limpiar_pares_usuario()
        self.view.actualizar_label_c([])

    def calcular_reflexiva1(self):
        resultado = self.model.es_reflexiva_u()
        if resultado:
            self.view.mostrar_resultado_ru("C", ["es reflexiva"])
        else:
            self.view.mostrar_resultado_ru("C", ["no es refelxiva"])

    def calcular_simetrica1(self):
        resultado = self.model.es_simetrica_u()
        if resultado:
            self.view.mostrar_resultado_ru("C", ["es simetrica"])
        else:        
            self.view.mostrar_resultado_ru("C", ["no es simetrica"])
    
    def calcular_antisimetrica1(self):
        resultado = self.model.es_antisimetrica_u()
        if resultado:
            self.view.mostrar_resultado_ru("C", ["es antisimetrica"])
        else:
            self.view.mostrar_resultado_ru("C", ["no es antisimetrica"])
    
    def calcular_transitiva1(self):
        resultado = self.model.es_transitiva_u()
        if resultado:
            self.view.mostrar_resultado_ru("C", ["es transitiva"])
        else:
            self.view.mostrar_resultado_ru("C", ["no es transitiva"])



    