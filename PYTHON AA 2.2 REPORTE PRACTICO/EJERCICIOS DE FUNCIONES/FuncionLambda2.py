# Lista de alumnos en el curso de programación
alumnos = ['Carlos', 'Andrea', 'Fernando', 'Laura', 'Juan']

# Lista de calificaciones obtenidas por los alumnos (sobre 100)
calificaciones = [85, 70, 92, 60, 78]

# Función anónima (lambda) para asignar un estado según la calificación
asignar_estado = lambda calif: "Aprobado" if calif >= 70 else "Reprobado"

# Usamos map() para evaluar a cada alumno
resultados = list(map(asignar_estado, calificaciones))

# Combinar los alumnos con su estado
calificaciones_finales = list(map(lambda alumno, estado: f"{alumno}: {estado}", alumnos, resultados))

# Imprimir los resultados finales sin corchetes
for resultado in calificaciones_finales:
    print(resultado)
