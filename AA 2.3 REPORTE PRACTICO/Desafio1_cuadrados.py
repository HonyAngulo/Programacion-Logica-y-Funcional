def cuadradosLista(arreglo):
    """
    Recibe una lista de números reales y devuelve una lista con los cuadrados 
    de los enteros positivos utilizando filter() y map().
    """
    enteros_positivos = filter(lambda x: isinstance(x, int) and x > 0, arreglo)  # Filtra enteros positivos
    cuadrados = map(lambda x: x**2, enteros_positivos)  # Calcula el cuadrado de cada número filtrado
    return list(cuadrados)  # Convierte el resultado en una lista y lo devuelve

# Uso
if __name__ == "__main__":
    numeros = [-3, 4.8, 5, 3, -3.2]  # Lista de entrada
    cuadrados_enteros = cuadradosLista(numeros)  # Llama a la función
    print("Entrada:", numeros)  # Muestra la lista original
    print("Salida:", cuadrados_enteros)  # Muestra la salida esperada: [25, 9]
