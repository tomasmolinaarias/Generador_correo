import re

def validar_telefono(telefono):
    # Se define un patrón que verifica si el teléfono tiene 9 dígitos
    patron = re.compile(r'^\d{9}$')

    # Se verifica si el teléfono coincide con el patrón
    return bool(patron.match(telefono))

