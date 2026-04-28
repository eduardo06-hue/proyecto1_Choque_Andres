import tkinter as tk
from views.view import View
from controllers.controller import Controller
from models.model import ConjuntoModel

def main():
    root = tk.Tk()

    model = ConjuntoModel()
    view = View(root)
    controller = Controller(model, view)   
    model.cargar()
    
    view.actualizar_label_a(model.get_A())
    view.actualizar_label_b(model.get_B())
    view.actualizar_label_c(model.get_pares_usuario())

    root.protocol("WM_DELETE_WINDOW", lambda: [model.guardar(), root.destroy()])

    root.mainloop()

if __name__ == "__main__":
    main()
