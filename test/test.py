import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.model import ConjuntoModel


# ══════════════════════════════════════════
# TESTS DE CONJUNTOS
# ══════════════════════════════════════════

def test_union():
    m = ConjuntoModel()
    m.agregar_a_A("1")
    m.agregar_a_A("2")
    m.agregar_a_B("2")
    m.agregar_a_B("3")
    resultado = m.union()
    ok = all(e in resultado for e in ["1", "2", "3"])
    print(f"test_union:                    {'✅ PASO' if ok else '❌ FALLO'} → {resultado}")

def test_interseccion():
    m = ConjuntoModel()
    m.agregar_a_A("1")
    m.agregar_a_A("2")
    m.agregar_a_B("2")
    m.agregar_a_B("3")
    resultado = m.interseccion()
    ok = "2" in resultado and len(resultado) == 1
    print(f"test_interseccion:             {'✅ PASO' if ok else '❌ FALLO'} → {resultado}")

def test_diferencia():
    m = ConjuntoModel()
    m.agregar_a_A("1")
    m.agregar_a_A("2")
    m.agregar_a_B("2")
    m.agregar_a_B("3")
    resultado = m.diferencia()
    ok = "1" in resultado and "2" not in resultado
    print(f"test_diferencia:               {'✅ PASO' if ok else '❌ FALLO'} → {resultado}")

def test_diferencia_simetrica():
    m = ConjuntoModel()
    m.agregar_a_A("1")
    m.agregar_a_A("2")
    m.agregar_a_B("2")
    m.agregar_a_B("3")
    resultado = m.diferencia_simetrica()
    ok = all(e in resultado for e in ["1", "3"]) and "2" not in resultado
    print(f"test_diferencia_simetrica:     {'✅ PASO' if ok else '❌ FALLO'} → {resultado}")

def test_subconjunto_a_en_b():
    m = ConjuntoModel()
    m.agregar_a_A("1")
    m.agregar_a_A("2")
    m.agregar_a_B("1")
    m.agregar_a_B("2")
    m.agregar_a_B("3")
    resultado = m.subconjunto()
    # A={1,2} ⊆ B={1,2,3} → True
    print(f"test_subconjunto A⊆B:          {'✅ PASO' if resultado else '❌ FALLO'} → {resultado}")

def test_subconjunto_b_en_a():
    m = ConjuntoModel()
    m.agregar_a_A("1")
    m.agregar_a_A("2")
    m.agregar_a_A("3")
    m.agregar_a_B("1")
    m.agregar_a_B("2")
    resultado = m.subconjunto2()
    # B={1,2} ⊆ A={1,2,3} → True
    print(f"test_subconjunto B⊆A:          {'✅ PASO' if resultado else '❌ FALLO'} → {resultado}")

def test_superconjunto_a_b():
    m = ConjuntoModel()
    m.agregar_a_A("1")
    m.agregar_a_A("2")
    m.agregar_a_A("3")
    m.agregar_a_B("1")
    m.agregar_a_B("2")
    resultado = m.superconjunto()
    # A={1,2,3} ⊇ B={1,2} → True
    print(f"test_superconjunto A⊇B:        {'✅ PASO' if resultado else '❌ FALLO'} → {resultado}")

def test_superconjunto_b_a():
    m = ConjuntoModel()
    m.agregar_a_A("1")
    m.agregar_a_A("2")
    m.agregar_a_B("1")
    m.agregar_a_B("2")
    m.agregar_a_B("3")
    resultado = m.superconjunto2()
    # B={1,2,3} ⊇ A={1,2} → True
    print(f"test_superconjunto B⊇A:        {'✅ PASO' if resultado else '❌ FALLO'} → {resultado}")

# ══════════════════════════════════════════
# TESTS DE RELACIONES (pares automáticos)
# ══════════════════════════════════════════

def test_reflexiva_auto():
    m = ConjuntoModel()
    m.agregar_a_A("1")
    m.agregar_a_A("2")
    resultado = m.es_reflexiva("A")
    # A={1,2} genera (1,1),(1,2),(2,1),(2,2) → reflexiva ✅
    print(f"test_reflexiva auto:           {'✅ PASO' if resultado else '❌ FALLO'} → {resultado}")

def test_simetrica_auto():
    m = ConjuntoModel()
    m.agregar_a_A("1")
    m.agregar_a_A("2")
    resultado = m.es_simetrica("A")
    # pares completos incluyen todos los inversos → simétrica ✅
    print(f"test_simetrica auto:           {'✅ PASO' if resultado else '❌ FALLO'} → {resultado}")

def test_antisimetrica_auto():
    m = ConjuntoModel()
    m.agregar_a_A("1")
    m.agregar_a_A("2")
    resultado = m.es_antisimetrica("A")
    # tiene (1,2) y (2,1) con 1≠2 → antisimétrica ❌
    print(f"test_antisimetrica auto:       {'✅ PASO' if not resultado else '❌ FALLO'} → {resultado}")

def test_transitiva_auto():
    m = ConjuntoModel()
    m.agregar_a_A("1")
    m.agregar_a_A("2")
    resultado = m.es_transitiva("A")
    # pares completos → transitiva ✅
    print(f"test_transitiva auto:          {'✅ PASO' if resultado else '❌ FALLO'} → {resultado}")

# ══════════════════════════════════════════
# TESTS DE RELACIONES (pares por usuario)
# ══════════════════════════════════════════

def test_reflexiva_u():
    m = ConjuntoModel()
    m.agregar_par_usuario("1", "1")
    m.agregar_par_usuario("2", "2")
    m.agregar_par_usuario("1", "2")
    resultado = m.es_reflexiva_u()
    # tiene (1,1) y (2,2) → reflexiva ✅
    print(f"test_reflexiva usuario:        {'✅ PASO' if resultado else '❌ FALLO'} → {resultado}")

def test_simetrica_u():
    m = ConjuntoModel()
    m.agregar_par_usuario("1", "2")
    m.agregar_par_usuario("2", "1")
    resultado = m.es_simetrica_u()
    # (1,2) tiene espejo (2,1) → simétrica ✅
    print(f"test_simetrica usuario:        {'✅ PASO' if resultado else '❌ FALLO'} → {resultado}")

def test_antisimetrica_u():
    m = ConjuntoModel()
    m.agregar_par_usuario("1", "2")
    m.agregar_par_usuario("2", "1")
    resultado = m.es_antisimetrica_u()
    # (1,2) y (2,1) con 1≠2 → antisimétrica ❌
    print(f"test_antisimetrica usuario:    {'✅ PASO' if not resultado else '❌ FALLO'} → {resultado}")

def test_transitiva_u():
    m = ConjuntoModel()
    m.agregar_par_usuario("1", "2")
    m.agregar_par_usuario("2", "3")
    m.agregar_par_usuario("1", "3")
    resultado = m.es_transitiva_u()
    # (1,2)+(2,3)→(1,3) existe → transitiva ✅
    print(f"test_transitiva usuario:       {'✅ PASO' if resultado else '❌ FALLO'} → {resultado}")

# ══════════════════════════════════════════
# EJECUTAR TODOS
# ══════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 50)
    print("TESTS DE CONJUNTOS")
    print("=" * 50)
    test_union()
    test_interseccion()
    test_diferencia()
    test_diferencia_simetrica()
    test_subconjunto_a_en_b()
    test_subconjunto_b_en_a()
    test_superconjunto_a_b()
    test_superconjunto_b_a()

    print()
    print("=" * 50)
    print("TESTS RELACIONES (pares automáticos)")
    print("=" * 50)
    test_reflexiva_auto()
    test_simetrica_auto()
    test_antisimetrica_auto()
    test_transitiva_auto()

    print()
    print("=" * 50)
    print("TESTS RELACIONES (pares por usuario)")
    print("=" * 50)
    test_reflexiva_u()
    test_simetrica_u()
    test_antisimetrica_u()
    test_transitiva_u()