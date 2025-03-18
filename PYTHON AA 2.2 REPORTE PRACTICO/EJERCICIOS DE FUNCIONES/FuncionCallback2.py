# Función de orden superior que recibe un callback
def ejecutar_alerta(curso, callback):
    callback(curso)  # Llama al callback con el curso

# Callback que muestra la alerta con el curso y su profesor asignado
def mostrar_alerta(curso):
    cursos_profesores = {
        "programacion": ("👩‍💻", "Paloma Gongora"),
        "interfaces": ("💻", "Eduardo Moo"),
        "inteligencia artificial": ("🤖", "Placido Balam")
    }

    # Obtener el icono y el profesor según el curso ingresado
    icono, profesor = cursos_profesores.get(curso.lower(), ("❓", "Desconocido"))

    print(f"{icono} CURSO: {curso.title()} | Profesor: {profesor}")

# Pedir el curso al usuario
curso_usuario = input("Ingrese el curso (Programacion, Interfaces, Inteligencia Artificial): ").strip()

# Llamar a la función con el curso ingresado
ejecutar_alerta(curso_usuario, mostrar_alerta)

