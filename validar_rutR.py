def repetido(list):
    conjunto = set(list)
    return len(conjunto) < len(list)
def buscarElemento(rut,list):
    for i in list:
        if rut == i:
            return True
    return False