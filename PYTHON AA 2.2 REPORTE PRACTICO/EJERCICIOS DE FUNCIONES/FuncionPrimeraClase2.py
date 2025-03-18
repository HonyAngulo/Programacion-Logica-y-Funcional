#Este código verifica si una dirección IP es privada según las reglas de direccionamiento IP.
# Ejemplo 1: Validar si una dirección IP es privada

def es_ip_privada(ip): # Se define la función es_ip_privada(ip), que recibe un string (ip).
    return ip.startswith("192.168") or ip.startswith("10.") #Usa startswith() para verificar si la IP comienza con "192.168" o "10."

#Se asigna la función es_ip_privada a la variable verificador.
verificador = es_ip_privada 

# Se llama a verificador("192.168.1.1"), que en realidad es es_ip_privada("192.168.1.1").
#"192.168.1.1" comienza con "192.168", por lo que devuelve True.
#Se imprime "True" en pantalla.
resultado = "✅ True" if verificador("192.168.1.1") else "❌ False"
print(resultado)


'''¿Por qué estos valores?
➡️Las IP privadas más comunes son:

😉192.168.x.x → Usadas en redes domésticas.
😉10.x.x.x → Usadas en redes corporativas y grandes sistemas.
👉 Si la IP empieza con alguno de estos valores, la función devuelve True (privada).
👉Si no, devuelve False (pública).'''

