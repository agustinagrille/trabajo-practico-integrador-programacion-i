def comparar_algoritmos(tiempo_iterativa, tiempo_formula, tiempo_recursiva):
    tiempos = {
        "Algoritmo Iterativo": tiempo_iterativa,
        "Algoritmo de Fórmula": tiempo_formula,
        "Algoritmo con Recursiva": tiempo_recursiva
    }
    mejor = min(tiempos, key=tiempos.get)
    print(f"El algoritmo más eficiente fue: {mejor}")
    for nombre, tiempo in tiempos.items():
        print(f"- {nombre}: {tiempo:.6f} segundos")
        