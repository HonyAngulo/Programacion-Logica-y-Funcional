from riego import *

# Parámetros de prueba
humedad = "baja"
temperatura = 35
hora = 20
lluvia = False

print("hora_adecuada:", hora_adecuada(hora))
print("alerta_calor:", alerta_calor(temperatura))
print("alerta_sequia:", alerta_sequia(humedad, temperatura))
print("activar_riego:", activar_riego(humedad, lluvia, hora, temperatura))
print("recomendacion:", recomendacion(humedad, temperatura, hora, lluvia))
