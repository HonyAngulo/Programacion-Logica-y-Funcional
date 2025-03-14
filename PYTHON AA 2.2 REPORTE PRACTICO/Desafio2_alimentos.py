def preparar_pizza():
    return "🍕"

def preparar_hamburguesa():
    return "🍔"

def preparar_hotdog():
    return "🌭"

def calcular_bonus(num_porciones):  
    if num_porciones > 2:  
        return "coca gratis"
    return ""  

def ordenar_alimento(preparar_alimento, num_porciones):  
    porciones_alimento = [preparar_alimento() for _ in range(num_porciones)]
    bonus = calcular_bonus(num_porciones)  
    return porciones_alimento, bonus  


alimento_grupoA = ordenar_alimento(preparar_pizza, 5)
alimento_grupoB = ordenar_alimento(preparar_hamburguesa, 3)
alimento_grupoC = ordenar_alimento(preparar_hotdog, 2)

print(alimento_grupoA, alimento_grupoB, alimento_grupoC)