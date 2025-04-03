def agregar_asignatura(lista):
    asig_nueva = input("escribe la asignatura nueva o 'no' para salir:")
    if asig_nueva == "no":
        return lista
    return agregar_asignatura(lista + [asig_nueva])
asignaturas = ["graficacion", "automatas", "investigacion"]
nueva_lista = agregar_asignatura(asignaturas)