jugadores = [
    {"nombre": "brandon", "edad":22},
    {"nombre": "alana", "edad":23},
    {"nombre": "oso", "edad":24},
    {"nombre": "kafai", "edad":25}
    
]

nombres_jugadores = list(map(lambda jugador: jugador["nombre"], jugadores))
print(nombres_jugadores)