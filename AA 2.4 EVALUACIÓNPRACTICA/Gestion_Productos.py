def gestion_productos(productos):
    productos_ordenados = sorted(productos)
    cadena_ordenada = ", ".join(productos_ordenados)
    
    crear_slug = lambda nombre: nombre.lower().replace(" ", "-")
    slugs = list(map(crear_slug, productos))  
    
    return {
        "slugs": slugs,
        "cadena_ordenada": cadena_ordenada,
        "lista_ordenada": productos_ordenados 
    }

productos = [
    "Frijoles Refritos",
    "Coca Cola",
    "Zumo de Naranja", 
    "Café de Olla", 
    "Gorditas de Chicharrón", 
    "Huevos Motuleños"
]

resultado = gestion_productos(productos)

print("a. Lista de slugs:")
print("   -> " + "\n   -> ".join(resultado["slugs"])) 

print("\nb. Cadena de nombres en orden alfabético:")
print("   " + resultado["cadena_ordenada"])
