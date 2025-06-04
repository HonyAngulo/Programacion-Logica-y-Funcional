# sistema_riego.py
from typing import Literal

# Tipos posibles
Humedad = Literal["baja", "muy_baja", "media", "alta"]

def hora_adecuada(hora: int) -> bool:
    """Devuelve True si la hora es adecuada para regar (antes de las 10 o después de las 18)."""
    return 0 <= hora <= 23 and (hora < 10 or hora > 18)

def alerta_calor(temperatura: int) -> bool:
    """Retorna True si hay temperaturas peligrosas."""
    return temperatura >= 32

def alerta_sequia(humedad: Humedad, temperatura: int) -> bool:
    """Retorna True si hay sequía extrema."""
    return humedad == "muy_baja" and temperatura > 30

def activar_riego(humedad: Humedad, pronostico_lluvia: bool, hora: int, temperatura: int) -> bool:
    """Determina si se debe activar el riego."""
    return (
        humedad == "baja" and 
        not pronostico_lluvia and 
        hora_adecuada(hora) and 
        not alerta_calor(temperatura)
    )

def recomendacion(humedad: Humedad, temperatura: int, hora: int, pronostico_lluvia: bool) -> str:
    """Genera una recomendación basada en los sensores."""
    if activar_riego(humedad, pronostico_lluvia, hora, temperatura) and alerta_calor(temperatura):
        return "ALERTA: Temperatura peligrosa. RECOMENDACION: Postergue riego o use sistema por goteo nocturno"
    elif alerta_sequia(humedad, temperatura):
        return "ALERTA CRITICA: Sequia extrema detectada. RECOMENDACION: Riego de emergencia inmediato"
    elif activar_riego(humedad, pronostico_lluvia, hora, temperatura):
        return "RIEGO AUTORIZADO: Condiciones óptimas detectadas"
    else:
        return "SISTEMA EN ESPERA: No se requieren acciones"

def estado_sensores(humedad: Humedad, temperatura: int, hora: int, pronostico_lluvia: bool):
    """Imprime el estado actual de los sensores."""
    print("\n=== ESTADO ACTUAL DE SENSORES ===")
    print(f"Humedad del suelo: {humedad}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Hora actual: {hora}:00")
    print("Pronóstico: " + ("Lluvia esperada" if pronostico_lluvia else "No hay lluvia"))
    print("==================================\n")

# Ejemplo de ejecución
if __name__ == "__main__":
    h = "baja"
    t = 35
    hr = 20
    lluvia = False
    estado_sensores(h, t, hr, lluvia)
    print(recomendacion(h, t, hr, lluvia))
