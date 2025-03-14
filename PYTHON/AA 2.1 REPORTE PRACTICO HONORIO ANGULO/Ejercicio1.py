# input() es para solicitar información al usuario. 
# Cada variable (nombre_completo, semestre, grupo, carrera) almacenará el texto que el usuario escriba en la consola.
nombre_completo = input("Escribe tu nombre completo: ")
semestre = input("Escribe tu semestre: ")
grupo = input("Escribe tu grupo: ")
carrera = input("Escribe tu carrera: ")

# print() para imprimir un encabezado. 
# El \n al inicio agrega un salto de línea para que la información tenga un espacio antes de mostrarse.
print("\n=== Información del Estudiante ===")

# (f"") imprimen la información del usuario en un formato de lista ordenada.
# f-strings (f"") para insertar variables directamente dentro del texto.
# Se usa - al inicio de cada línea para simular una lista.
print(f"- Nombre completo: {nombre_completo}")
print(f"- Semestre: {semestre}")
print(f"- Grupo: {grupo}")
print(f"- Carrera: {carrera}")
