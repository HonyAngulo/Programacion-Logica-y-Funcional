def preparar_hotcake():
    return "🥞"

def ordenar_hotcakes(numero_piezas):
    numero_hot = [preparar_hotcake() for _ in range(numero_piezas)]
    return numero_hot

hotcakes_grupo_a = ordenar_hotcakes(int(input ('ingresa tu orden')))

print(hotcakes_grupo_a)