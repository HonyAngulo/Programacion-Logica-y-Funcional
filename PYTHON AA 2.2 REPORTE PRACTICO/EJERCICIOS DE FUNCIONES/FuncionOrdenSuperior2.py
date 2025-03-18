# Definición de la función binario_a_decimal que convierte un número binario a decimal
def binario_a_decimal(binario):
    # La función int() toma el número binario como una cadena y lo convierte a entero en base 2 (binario)
    return int(binario, 2)

# Llamada a la función binario_a_decimal pasando el número binario "1101" como argumento
# El número binario "1101" se convertirá a su equivalente en decimal (13)
print(binario_a_decimal("1101"))
