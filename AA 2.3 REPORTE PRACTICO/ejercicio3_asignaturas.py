asignatura_viii =["logica y funcional"]
b = asignatura_viii+["web"]
print(asignatura_viii)
print(b)

def agregar_asignatura(lista, asignatura):
    return lista + asignatura
pregunta = input('ingresa nueva asignatura')
print (agregar_asignatura(asignatura_viii, pregunta))