# Tipos de datos
# Colecciones
# Listas
lista = [1, 2, 3, 4, 5]
print(lista)
print(lista[0]) #imprime el primer elemento de la lista
print(lista[1])

# Tuplas
tupla = (1, 2, 3, 4, 5)
print(tupla)
print(tupla[0])#Imprime el primer elemento de la tupla
print(tupla[1])

#Diccionarios
diccionario = {'nombre': 'juan', 'edad': 22}
print(diccionario)
print(diccionario['nombre'])#imprime el valor de la clave nombre
print(diccionario['edad'])

#Conjuntos
conjunto = {1, 2, 3, 4, 5}
print(conjunto)

#Convertir cadena en entero
numero = int("10")
print(conjunto)

#Convertir cadena a flotante
numero = float("10.5")
print(numero)

# Convertir entero a cadena
numero = str(10)
print(numero)

# Convertir flotante a cadena
numero = str(10.5)
print(numero)

# Convertir entero a flotante
numero = float(10)
print(numero)

# Convertir flotante a entero
numero = int(10.5)
print(numero)

# Operaciones aritméticas
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)

# Operaciones relacionales
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print("¿El primer número es mayor que el segundo?:", num1 > num2)
print("¿El primer número es menor que el segundo?:", num1 < num2)
print("¿El primer número es mayor o igual que el segundo?:", num1 >= num2)
print("¿El primer número es menor o igual que el segundo?:", num1 <= num2)
print("¿El primer número es igual que el segundo?:", num1 == num2)
print("¿El primer número es diferente que el segundo?:", num1 != num2)

# Operaciones lógicas
print("Operaciones lógicas")
print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False:", False and False)
print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)
print("Not True:", not True)
print("Not False:", not False)

# Operaciones de asignación
num1 = 10
num1 += 5
print(num1)
num1 -= 5
print(num1)
num1 *= 5
print(num1)
num1 /= 5
print(num1)
num1 **= 5  # Exponente
print(num1)
num1 //= 5  # División entera
print(num1)

# Operadores de pertenencia
lista = [1, 2, 3, 4, 5]
print(1 in lista)
print(6 in lista)  # Imprime False
print(6 not in lista)  # Imprime True

aprobado = float(input("Ingresa tu calificación: ")) >= 70
print("¿Aprobaste?:", aprobado)


