#ejemplo 1 Funcion para calcular el area de un cuadrado.
def calcular_area_cuadrado(lado):
    return lado ** 2

# solicita el valor al usuario el valor del lado del cuadrado.
lado = float(input("Ingrese la longitud del lado del cuadrado: ")) 

#Se calcula el area del cuadrado.
area = calcular_area_cuadrado(lado)
# imprime el resultado.
print(f"El area del cuadrado es: {area} 🟦")


