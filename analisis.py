def comparar_algoritmos(tiempo_iterativa, tiempo_formula, tiempo_recursiva):#Se incia la funcion de comparacion de los algoritmos.
    tiempos = {
        "Algoritmo Iterativo": tiempo_iterativa,
        "Algoritmo de Fórmula": tiempo_formula,
        "Algoritmo con Recursiva": tiempo_recursiva
    }
    mejor = min(tiempos, key=tiempos.get)
    print(f"El algoritmo más eficiente fue: {mejor}") #Se imprime el algoritmo de mayor eficiencia.
    for nombre, tiempo in tiempos.items(): #Inicio del ciclo for
        print(f"- {nombre}: {tiempo:.6f} segundos")# Se imprime el tiempo de ejeccucion de los algoritmos.
