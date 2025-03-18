# Definición de la función medir_tiempo que mide el tiempo de ejecución de una función
def medir_tiempo(funcion, *args):
    import time  # Se importa el módulo 'time' para medir el tiempo de ejecución
    
    # Se guarda el momento de inicio antes de ejecutar la función
    inicio = time.time()
    
    # Ejecuta la función proporcionada con los argumentos dados y guarda el resultado
    resultado = funcion(*args)
    
    # Se guarda el momento de finalización después de ejecutar la función
    fin = time.time()
    
    # Se imprime el tiempo que ha tardado en ejecutarse la función
    print(f"Tiempo de ejecución: {fin - inicio} segundos")
    
    # Retorna el resultado de la función ejecutada
    return resultado

# Definición de la función 'suma' que toma dos parámetros y devuelve su suma
def suma(a, b): 
    return a + b

# Llamada a la función medir_tiempo pasando la función 'suma' y los argumentos 10 y 20
print(medir_tiempo(suma, 10, 20))  # Esto va a ejecutar la suma y medir el tiempo de ejecución
