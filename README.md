# Proyecto 1 — Operaciones de Conjuntos y Relaciones Binarias
**Autor:** Andres Eduardo Choque Terrazas 

## Descripción
Aplicación de escritorio desarrollada en Python con interfaz gráfica Tkinter.
Permite trabajar con dos conjuntos (A y B) implementados con listas enlazadas,
realizar operaciones entre ellos y analizar propiedades de relaciones binarias.

---

## Estructura del proyecto
proyecto1_Choque_Andres/
├── controllers/
│   └── controller.py       # conecta model y view
├── datos/
│   └── conjuntos.json      # guarda el estado de la app
├── estructuras/
│   ├── conjuntos.py        # Nodo y Conjunto (lista enlazada)
│   └── relaciones.py       # Par y Relacion (lista enlazada)
├── models/
│   └── model.py            # lógica y operaciones
├── test/
│   └── test.py             # pruebas automáticas
├── views/
│   └── view.py             # interfaz gráfica
└── main.py                 # punto de entrada
---

## Requisitos
- Python 3.x
- tkinter (incluido en Python por defecto)

---

## Cómo ejecutar
```bash
cd proyecto1_Choque_Andres
python main.py
```

---

## Funcionalidades

### Sección: Conjuntos
Se definen dos conjuntos A y B. Cada uno se implementa internamente
como una lista enlazada que no permite elementos duplicados.

| Operación | Descripción |
|---|---|
| Unión (A ∪ B) | Todos los elementos de A y B sin repetir |
| Intersección (A ∩ B) | Solo los elementos que están en A y en B |
| Diferencia (A - B) | Elementos de A que no están en B |
| Diferencia simétrica (A ⊕ B) | Elementos que están en A o en B pero no en ambos |
| Subconjunto (A ⊆ B) | Verifica si todos los elementos de A están en B |
| Subconjunto (B ⊆ A) | Verifica si todos los elementos de B están en A |
| Superconjunto (A ⊇ B) | Verifica si A contiene todos los elementos de B |
| Superconjunto (B ⊇ A) | Verifica si B contiene todos los elementos de A |

---

### Sección: Relaciones (pares automáticos)
Al presionar "Mostrar par (A)" o "Mostrar par (B)" se genera automáticamente
el producto cartesiano del conjunto seleccionado. Por ejemplo:
A = {1, 2}  →  pares = {(1,1), (1,2), (2,1), (2,2)}

Luego se pueden verificar las siguientes propiedades sobre esos pares:

| Propiedad | Descripción |
|---|---|
| Reflexiva | Para todo elemento a, el par (a,a) debe existir |
| Simétrica | Si existe (a,b), entonces (b,a) también debe existir |
| Antisimétrica | Si existen (a,b) y (b,a), entonces a debe ser igual a b |
| Transitiva | Si existen (a,b) y (b,c), entonces (a,c) también debe existir |

---

### Sección: Relaciones (pares por usuario)
El usuario puede definir su propia relación C ingresando pares
manualmente con el formato `a,b`. Por ejemplo escribir `1,2` y
presionar "Agregar par" agrega el par (1,2) a C.

Se pueden verificar las mismas 4 propiedades sobre C:

| Propiedad | Descripción |
|---|---|
| Reflexiva | Verifica sobre los elementos que aparecen en los propios pares de C |
| Simétrica | Si existe (a,b), entonces (b,a) también debe existir en C |
| Antisimétrica | Si existen (a,b) y (b,a) en C, entonces a debe ser igual a b |
| Transitiva | Si existen (a,b) y (b,c) en C, entonces (a,c) también debe existir |

---

## Ejemplos de uso

### Operaciones de conjuntos
A = {1, 2, 3}
B = {2, 3, 4}
Unión:               {1, 2, 3, 4}
Intersección:        {2, 3}
Diferencia (A-B):    {1}
Dif. simétrica:      {1, 4}
A ⊆ B:               No
A ⊇ B:               No

### Relaciones automáticas
A = {1, 2}
Pares: {(1,1), (1,2), (2,1), (2,2)}
Reflexiva:      ✅ tiene (1,1) y (2,2)
Simétrica:      ✅ (1,2) tiene espejo (2,1)
Antisimétrica:  ❌ (1,2) y (2,1) existen con 1≠2
Transitiva:     ✅ (1,2)+(2,1)→(1,1) existe

### Relaciones por usuario
C = {(1,2), (2,3), (1,3)}
Reflexiva:      ❌ faltan (1,1),(2,2),(3,3)
Simétrica:      ❌ (1,2) no tiene espejo (2,1)
Antisimétrica:  ✅ ningún par tiene su espejo
Transitiva:     ✅ (1,2)+(2,3)→(1,3) existe

---

## Arquitectura — Patrón MVC
Usuario
↓ interactúa con
View (view.py)
↓ notifica a
Controller (controller.py)
↓ opera sobre
Model (model.py)
↓ usa
Estructuras (conjuntos.py / relaciones.py)

- **Model** — única capa que conoce las estructuras internas
- **View** — solo construye widgets y expone métodos de lectura/escritura
- **Controller** — conecta eventos de la view con operaciones del model

---

## Persistencia
Al cerrar la ventana los datos se guardan automáticamente en
`datos/conjuntos.json`. Al abrir la app nuevamente se restauran
los conjuntos A, B y los pares de C del estado anterior.

---

## Tests
Para ejecutar las pruebas automáticas:
```bash
python test/test.py
```
Los tests verifican todas las operaciones de conjuntos y las
4 propiedades de relaciones tanto automáticas como por usuario.