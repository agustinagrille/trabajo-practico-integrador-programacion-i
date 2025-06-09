def suma_iterativa(n): ##Primer algoritmo que analizaremos
    total = 0
    for i in range(1, n + 1): ##Iteramos la suma con un ciclo for
        total += i
    return total ##Retornamos el total una vez que se termina de recorrer el numero

def suma_formula(n): ##Segundo algoritmo a analizar
    return n * (n + 1) // 2 ##Retornamos directamente el producto de la formula de Gauss para la suma de n

def suma_recursiva(n): ##Tercer algoritmo a analizar
    if n == 0: ##Valido si n es 0
        return 0 ##Retorno 0, cierro el llamado recursivo
    return n + suma_recursiva(n - 1)  ##Aplico recursividad