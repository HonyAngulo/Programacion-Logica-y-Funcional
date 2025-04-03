jugadores = [
    {"nombre": "brandon", "edad":22},
    {"nombre": "alana", "edad":23},
    {"nombre": "oso", "edad":24},
    {"nombre": "kafai", "edad":25}
    
]

jugadores_mayores = list(filter(lambda jugador: jugador["edad"] > 23, jugadores))
print(jugadores_mayores)