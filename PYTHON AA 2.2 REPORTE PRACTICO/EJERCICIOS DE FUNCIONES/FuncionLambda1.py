# Lista de cursos
cursos = ['Curso de Python', 'Curso de Java', 'Curso de C++', 'Curso de Redes']

# Lista de horas de los cursos
horas_cursos = [4, 6, 8, 10]

# Lista de alumnos inscritos
alumnos = ['Carlos', 'Andrea', 'Fernando', 'Laura', 'Juan']

# Asegurándonos de que el número de cursos y alumnos coincide
if len(cursos) == len(horas_cursos):
    # Bienvenida al curso
    print("¡Bienvenidos a los cursos de Sistemas Impartido por Honorio!")
    
    # Multiplicar la duración de los cursos por 2 (simulando horas extra de estudio)
    doble_horas = lambda x: x * 2

    # Imprimir las horas duplicadas de cada curso
    for i, curso in enumerate(cursos):
        horas_dobladas = doble_horas(horas_cursos[i])
        print(f'{curso}: {horas_dobladas} horas')

    # Asocia a cada alumno con su curso
    alumnos_con_curso = list(zip(alumnos, cursos))
    print("\nAlumnos inscritos:")
    for alumno, curso in alumnos_con_curso:
        print(f'{alumno} está inscrito en {curso}')
else:
    print('El número de cursos no coincide con el número de alumnos')
