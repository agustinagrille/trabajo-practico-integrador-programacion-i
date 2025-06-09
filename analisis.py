def comparar_algoritmos(tiempo_iterativa, tiempo_formula, tiempo_recursiva):
    tiempos = {
        "Iterativa": tiempo_iterativa,
        "Fórmula": tiempo_formula,
        "Recursiva": tiempo_recursiva
    }
    mejor = min(tiempos, key=tiempos.get)
    print(f"El algoritmo más eficiente fue: {mejor}")
    for nombre, tiempo in tiempos.items():
        print(f"- {nombre}: {tiempo:.6f} segundos")
        