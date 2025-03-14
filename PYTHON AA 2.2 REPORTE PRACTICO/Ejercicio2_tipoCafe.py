def preparar_cafe_americano():
    return "cafe americano"

def preparar_cafe_olla():
    return "cafe de olla"

def ordenar_cafe(preparar_cafe_americano, numero_tazas):
    tazas_cafe = [preparar_cafe_americano() for _ in range(numero_tazas)]
    return tazas_cafe

def ordenar_cafe(preparar_cafe_olla, numero_tazas):
    tazas_cafe = [preparar_cafe_olla() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_grupo_a = ordenar_cafe(int(input ('ingresa tu orden')))
cafe_grupo_b = ordenar_cafe(int(input ('ingresa tu orden')))

print(cafe_grupo_a)
print(cafe_grupo_b)