import tkinter as tk
from tkinter import Frame, Label, Button, Entry, StringVar, ttk

class View:
    def __init__(self, master):
        self.master = master
        master.title("Operaciones de Conjuntos y Relaciones")
        master.resizable(True, True)

        # ── Título Conjuntos ──────────────────────────────────────
        frame_t = Frame(master, pady = 10)
        frame_t.pack()
        Label(frame_t, text = "CONJUNTOS", font = ("Arial", 14, "bold"), width = 12, anchor = "w", fg = "red").pack()

        # ── Entrada Conjunto A ──────────────────────────────
        frame_a = Frame(master, padx=10, pady=5)
        frame_a.pack(fill="x")

        Label(frame_a, text="Conjunto A:", width=12, anchor="w").pack(side="left")
        self.entry_a = Entry(frame_a, width=20)
        self.entry_a.pack(side="left", padx=5)
        self.btn_agregar_a = Button(frame_a, text="Agregar")
        self.btn_agregar_a.pack(side="left")
        self.btn_limpiar_a = Button(frame_a, text="Limpiar A")
        self.btn_limpiar_a.pack(side="left", padx=5)

        self.label_a = Label(master, text="A = {}", fg="blue", font=("Arial", 11))
        self.label_a.pack()

        # ── Entrada Conjunto B ──────────────────────────────
        frame_b = Frame(master, padx=10, pady=5)
        frame_b.pack(fill="x")

        Label(frame_b, text="Conjunto B:", width=12, anchor="w").pack(side="left")
        self.entry_b = Entry(frame_b, width=20)
        self.entry_b.pack(side="left", padx=5)
        self.btn_agregar_b = Button(frame_b, text="Agregar")
        self.btn_agregar_b.pack(side="left")
        self.btn_limpiar_b = Button(frame_b, text="Limpiar B")
        self.btn_limpiar_b.pack(side="left", padx=5)

        self.label_b = Label(master, text="B = {}", fg="darkgreen", font=("Arial", 11))
        self.label_b.pack()

        # ── Botones de operaciones ──────────────────────────
        frame_ops = Frame(master, pady=10)
        frame_ops.pack()

        self.btn_union        = Button(frame_ops, text="Unión (A ∪ B)",         width=20)
        self.btn_interseccion = Button(frame_ops, text="Intersección (A ∩ B)",  width=20)
        self.btn_diferencia   = Button(frame_ops, text="Diferencia (A - B)",    width=20)
        self.btn_diferencia_simetrica = Button(frame_ops, text = "Diferencia Simetrica (A ⊕ B)", width = 20)
        self.btn_subconjunto = Button(frame_ops, text = "Subconjunto (A ⊆ B)", width = 20)
        self.btn_subconjunto2 = Button(frame_ops, text = "Subconjunto (B ⊆ A)", width = 20)
        self.btn_superconjunto = Button(frame_ops, text = "Superconjunto (A ⊇ B)", width = 20)
        self.btn_superconjunto2 = Button(frame_ops, text = "Superconjunto (B ⊇ A)", width = 20)

        self.btn_union.grid(row=0, column=0, padx=5, pady=3)
        self.btn_interseccion.grid(row=0, column=1, padx=5, pady=3)
        self.btn_diferencia.grid(row=0, column=2, padx=5, pady=3)
        self.btn_diferencia_simetrica.grid(row=1, column=0, padx=5, pady=3)
        self.btn_subconjunto.grid(row=1, column=1, padx = 5, pady = 3)
        self.btn_subconjunto2.grid(row=1, column=2, padx = 5, pady = 3)
        self.btn_superconjunto.grid(row=2, column=0, padx = 5, pady = 3)
        self.btn_superconjunto2.grid(row=2, column=1, padx = 5, pady = 3)

        # ── Resultado ──────────────────────────────────────
        Label(master, text="Resultado:", font=("Arial", 11, "bold")).pack(pady=(10, 0))
        self.label_resultado = Label(master, text="—", font=("Arial", 12),fg="purple", pady=5)
        self.label_resultado.pack()
        
        # ── Título Relaciones ──────────────────────────────────────
        frame_r = Frame(master, pady = 10)
        frame_r.pack()
        Label(frame_r, text = "RELACIONES", font = ("Arial", 14, "bold"), width = 12, anchor = "w", fg = "red").pack()

        # ── Entrada Par Definido────────────────────────────────────────────
        frame_p = Frame(master,padx = 10, pady = 5)
        frame_p.pack(fill = "x")
        Label(frame_p, text = "Par del conjunto A o B:", width = 17, anchor = "w").pack(side="left")
        self.label_p = Label(frame_p, text = "{}", fg = "black", font = ("Arial", 11))
        self.label_p.pack(side = "left", padx = 5)
        self.btn_limpiar = Button(frame_p, text = "Limpiar par")
        self.btn_limpiar.pack(side = "left", padx = 5) 
        self.btn_p_a = Button(frame_p, text = "Mostrar par (A)")
        self.btn_p_a.pack(side="left", padx = 5)
        self.btn_p_b = Button(frame_p, text = "Mostrar par (B)")
        self.btn_p_b.pack(side="left", padx = 5)

        # ── Botones de operaciones Relaciones definidas ──────────────────────────
        frame_ops_r = Frame(master,pady = 10)
        frame_ops_r.pack()
        self.btn_reflexiva = Button(frame_ops_r, text = "Reflexiva", width = 20)
        self.btn_simetrica = Button(frame_ops_r, text = "Simetrica", width = 20)
        self.btn_antisimetrica = Button(frame_ops_r, text = "Antisimetrica", width = 20)
        self.btn_transitiva = Button(frame_ops_r, text = "Transitiva", width = 20)
        self.btn_reflexiva.grid(row = 0, column = 0, padx = 5, pady = 3)
        self.btn_simetrica.grid(row = 0, column = 1, padx = 5, pady = 3)
        self.btn_antisimetrica.grid(row = 0, column = 2, padx = 5, pady = 3)
        self.btn_transitiva.grid(row = 1, column = 0, padx = 5, pady = 3)

        # ── Resulatado Relaciones definido ───────────────────────────────
        Label(master, text="Resultado:", font=("Arial", 11, "bold")).pack(pady=(10, 0))
        self.label_resultado_r = Label(master, text = "—", font = ("Arial", 12), fg = "purple", pady = 5)
        self.label_resultado_r.pack()

        # —— Entrada Par por el usuario ——————————————————————————————————
        frame_por_usuario = Frame(master, padx=10, pady=5)
        frame_por_usuario.pack(fill="x")
        Label(frame_por_usuario, text="Agregar par (a,b):", width=13, anchor="w").pack(side="left")
        self.entry_por_usuario = Entry(frame_por_usuario, width=40)
        self.entry_por_usuario.pack(side="left", padx=5)
        self.btn_agregar_par = Button(frame_por_usuario, text="Agregar par")
        self.btn_agregar_par.pack(side="left", padx=5)
        self.btn_limpiar_par = Button(frame_por_usuario, text="Limpiar par")
        self.btn_limpiar_par.pack(side="left", padx=5)

        self.label_c = Label(master, text="C = {}", fg="green", font=("Arial", 12))
        self.label_c.pack()

        # —— Botones de operaciones para par por el usuario ——————————————————————————————
        frame_ops_ru = Frame(master,pady = 10)
        frame_ops_ru.pack()
        self.btn_reflexiva1 = Button(frame_ops_ru, text = "Reflexiva C", width = 20)
        self.btn_simetrica1 = Button(frame_ops_ru, text = "Simetrica C", width = 20)
        self.btn_antisimetrica1 = Button(frame_ops_ru, text = "Antisimetrica C", width = 20)
        self.btn_transitiva1 = Button(frame_ops_ru, text = "Transitiva C", width = 20)
        self.btn_reflexiva1.grid(row = 0, column = 0, padx = 5, pady = 3)
        self.btn_simetrica1.grid(row = 0, column = 1, padx = 5, pady = 3)
        self.btn_antisimetrica1.grid(row = 0, column = 2, padx = 5, pady = 3)
        self.btn_transitiva1.grid(row = 1, column = 0, padx = 5, pady = 3)

        # —— Resultado para par por el usuario —————————————————————————————————————————————— 
        Label(master, text="Resultado:", font=("Arial", 11, "bold")).pack(pady=(10, 0))
        self.label_resultado_ru = Label(master, text="—", font=("Arial", 12),fg="purple", pady=5)
        self.label_resultado_ru.pack()




    # ── Métodos de actualización Conjuntos──────────────────────────
    def get_entrada_a(self):
        val = self.entry_a.get().strip()
        self.entry_a.delete(0, "end")
        return val

    def get_entrada_b(self):
        val = self.entry_b.get().strip()
        self.entry_b.delete(0, "end")
        return val

    def actualizar_label_a(self, elementos):
        self.label_a.config(text=f"A = {{ {', '.join(elementos)} }}")

    def actualizar_label_b(self, elementos):
        self.label_b.config(text=f"B = {{ {', '.join(elementos)} }}")

    def mostrar_resultado(self, operacion, elementos):
        self.label_resultado.config(text=f"{operacion} = {{ {', '.join(elementos)} }}")

     # ── Métodos de actualización Relaciones──────────────────────────
    
    def actualizar_label_p(self, elementos):
         self.label_p.config(text = "{" + ", ".join(elementos) + "}")
        
    def mostrar_resultado_r(self, operacion, elementos):
        self.label_resultado_r.config(text=f"{operacion} = {{ {', '.join(elementos)} }}")

    # ── Métodos de actualización para par por el usuario ──────────────────────────
     
    def get_par_c(self):
        val = self.entry_por_usuario.get().strip()
        self.entry_por_usuario.delete(0, "end")
        return val

    def actualizar_label_c(self, elementos):
        self.label_c.config(text=f"C = {{ {', '.join(elementos)} }}")

    def mostrar_resultado_ru(self, operacion, elementos):
        self.label_resultado_ru.config(text=f"{operacion} = {{ {', '.join(elementos)} }}") 

    