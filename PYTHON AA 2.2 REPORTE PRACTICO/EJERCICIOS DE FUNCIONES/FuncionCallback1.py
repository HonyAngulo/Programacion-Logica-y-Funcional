#Callback para Notificar Eventos
# Función de orden superior que recibe un callback
def ejecutar_accion(mensaje, callback):
    callback(mensaje)  # Llama al callback con el mensaje

# Callback que imprime una notificación
#notificar(evento) → Es el callback, imprime 🔔 con el mensaje.
def notificar(curso): 
    print(f"🔔 Notificación: {curso}")

# Llamar a la función con el callback
# Ejecuta dos eventos: "Usuario ha iniciado sesión" y "Bienvenida".
ejecutar_accion("Usuario ha iniciado sesión al curso de ISC", notificar)
ejecutar_accion("Bienvenido al curso Honorio", notificar)
