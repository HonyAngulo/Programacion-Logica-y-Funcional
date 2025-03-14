def ordena_comida(x):
    if x == 1:
        return '🍔 Hamburguesa'
    elif x == 2:
        return '🍟 Papas fritas'
    elif x == 3:
        return '🥤 Coca cola'
    elif x == 4:
        return '🍨 Helado'
    elif x == 5:
        return '🍪 Galleta'
    else:
        return "Opción inválida"

def bienvenido():
    print('¡Bienvenido al camión de comida!')
    print('Aquí está el menú:')
    print('1. 🍔 Hamburguesa')
    print('2. 🍟 Papas fritas')
    print('3. 🥤 Coca cola')
    print('4. 🍨 Helado')
    print('5. 🍪 Galleta')

bienvenido()

opcion = int(input('¿Qué te gustaría ordenar? '))
print(ordena_comida(opcion))
