from algoritmos import suma_iterativa, suma_formula, suma_recursiva #Se importan las funciones de los otros modulos.
from tiempo import medir_tiempo
from analisis import comparar_algoritmos

def main():#Nuestra funcion principal
    n = 900 #incializo variable con valor 10000

    print(f"Calculando la suma de los primeros {n} números...\n")

    tiempo_iterativa, resultado_iterativa = medir_tiempo(suma_iterativa, n)#Ejecutamos la función suma_iterativa con n, medimos el tiempo que tarda en ejecutarse,
                                                                           #y guardamos el resultado de la suma y el tiempo en dos variables
    print(f"Suma iterativa: Resultado = {resultado_iterativa}, Tiempo = {tiempo_iterativa:.6f} segundos")

    tiempo_formula, resultado_formula = medir_tiempo(suma_formula, n)#Medimos cuánto tarda suma_formula(n) y guardamos el tiempo y el resultado
    print(f"Suma con fórmula: Resultado = {resultado_formula}, Tiempo = {tiempo_formula:.6f} segundos")

    tiempo_recursiva, resultado_recursiva = medir_tiempo(suma_recursiva, n)#Medimos cuánto tarda suma_recursiva(n) y guardamos el tiempo y el resultado
    print(f"Suma recursiva: Resultado = {resultado_recursiva}, Tiempo = {tiempo_recursiva:.6f} segundos")

    print("\nAnálisis de eficiencia:")
    comparar_algoritmos(tiempo_iterativa, tiempo_formula, tiempo_recursiva)#Comparamos los resultados de los tiempos de cada algoritmos

if __name__ == "__main__":
    main()