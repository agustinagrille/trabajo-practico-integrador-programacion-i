import time

def medir_tiempo(funcion, n): ##Defino metodo de medicion de tiempos de ejecución
    inicio = time.time()
    resultado = funcion(n)
    fin = time.time()
    return fin - inicio, resultado #Retorno medicion analizada para inicio y final + resultado