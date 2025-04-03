from functools import reduce


jugadores =[
{"nombre":"brandon", "edad":22},
{"nombre":"javier", "edad":30},
{"nombre":"carlos", "edad":18},
{"nombre":"jorge", "edad":25}
]

suma_edad = reduce(lambda acumulador, jugador: acumulador+jugador ["edad"], jugadores,0 )
print(suma_edad)