# Sombrero seleccionador 🧙‍♂️
"""
Este script simula el Sombrero Seleccionador de Harry Potter, que 
asigna a los usuarios a una de las cuatro casas de Hogwarts 
(Gryffindor, Hufflepuff, Ravenclaw, Slytherin) basado en sus 
respuestas a tres preguntas.

Variables:
    gryffindor (int): Contador de puntos para la casa Gryffindor.
    hufflepuff (int): Contador de puntos para la casa Hufflepuff.
    ravenclaw (int): Contador de puntos para la casa Ravenclaw.
    slytherin (int): Contador de puntos para la casa Slytherin.
"""

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

"""
Flujo del programa:
1. Imprime el título del Sombrero Seleccionador.
"""

print('===============')
print('El sombrero seleccionador 🧙‍♂️')
print('===============')

"""
2. Realiza las preguntas y actualiza los puntos de las casas según 
   la respuesta.
3. Determina y anuncia la casa a la que el usuario ha sido asignado, 
   basada en los puntos acumulados.

Preguntas:
1. ¿Te gusta el amanecer o el atardecer?
    - 1) Amanecer: +1 Gryffindor, +1 Ravenclaw
    - 2) Atardecer: +1 Hufflepuff, +1 Slytherin
"""
# Preguntas y sistema de puntos para el Sombrero Seleccionador

"""
2. Cuando muera, quiero que la gente me recuerde como:
    - 1) El bueno o la buena: +2 Hufflepuff
    - 2) El valiente o la valiente: +2 Slytherin
    - 3) El sabio o la sabia: +2 Ravenclaw
    - 4) El astuto o la astuta: +2 Gryffindor

3. ¿Qué tipo de instrumento complace más tu oído?
    - 1) El violín: +4 Slytherin
    - 2) La trompeta: +4 Hufflepuff
    - 3) El piano: +4 Ravenclaw
    - 4) El tambor: +4 Gryffindor
"""

# ~~~~~~~~~~~~~~ Pregunta 1 ~~~~~~~~~~~~~~

print('P1) ¿Te gusta el amanecer o el atardecer?')

print('  1) Amanecer')
print('  2) Atardecer')

respuesta = int(input('Ingresa respuesta (1-2): '))

if respuesta == 1:
    gryffindor += 1
    ravenclaw += 1
elif respuesta == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('Respuesta incorrecta.')

# ~~~~~~~~~~~~~~ Pregunta 2 ~~~~~~~~~~~~~~

print('\nP2) Cuando muera, quiero que la gente me recuerde como:')

print('  1) El bueno o la buena')
print('  2) El valiente o la valiente')
print('  3) El sabio o la sabia')
print('  4) El astuto o la astuta')
respuesta = int(input('Ingresa tu respuesta (1-4): '))

if respuesta == 1:
    hufflepuff += 2
elif respuesta == 2:
    slytherin += 2
elif respuesta == 3:
    ravenclaw += 2
elif respuesta == 4:
    gryffindor += 2
else:
    print('Respuesta incorrecta.')

# ~~~~~~~~~~~~~~ Pregunta 3 ~~~~~~~~~~~~~~

print('\nP3) ¿Qué tipo de instrumento complace más tu oído?')

print('  1) El violín')
print('  2) La trompeta')
print('  3) El piano')
print('  4) El tambor')

respuesta = int(input('Ingresa tu respuesta (1-4): '))

if respuesta == 1:
    slytherin += 4
elif respuesta == 2:
    hufflepuff += 4
elif respuesta == 3:
    ravenclaw += 4
elif respuesta == 4:
    gryffindor += 4
else:
    print('Respuesta incorrecta.')

"""
Resultados:
"""
# Imprime los puntos acumulados para cada casa.
# Anuncia la casa a la que el usuario ha sido asignado, basada en los puntos acumulados.

print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print('🦁 Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
    print('🦅 Ravenclaw!')
elif hufflepuff >= slytherin:
    print('🦡 Hufflepuff!')
else:
    print('🐍 Slytherin!')
