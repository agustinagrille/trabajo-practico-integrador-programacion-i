from algoritmos import suma_iterativa, suma_formula, suma_recursiva
from tiempo import medir_tiempo
from analisis import comparar_algoritmos

def main():
    n = 10000

    print(f"Calculando la suma de los primeros {n} números...\n")

    tiempo_iterativa, resultado_iterativa = medir_tiempo(suma_iterativa, n)
    print(f"Suma iterativa: Resultado = {resultado_iterativa}, Tiempo = {tiempo_iterativa:.6f} segundos")

    tiempo_formula, resultado_formula = medir_tiempo(suma_formula, n)
    print(f"Suma con fórmula: Resultado = {resultado_formula}, Tiempo = {tiempo_formula:.6f} segundos")

    tiempo_recursiva, resultado_recursiva = medir_tiempo(suma_recursiva, n)
    print(f"Suma recursiva: Resultado = {resultado_recursiva}, Tiempo = {tiempo_recursiva:.6f} segundos")

    print("\nAnálisis de eficiencia:")
    comparar_algoritmos(tiempo_iterativa, tiempo_formula, tiempo_recursiva)

if name == "main":
    main()