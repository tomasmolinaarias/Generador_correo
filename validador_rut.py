def validar_rut(rut):
    if not rut:
        return False
    # Eliminar puntos y guiones del Rut
    rut = rut.replace(".", "").replace("-", "")

    # Separar el número y el dígito verificador
    numero = rut[:-1]
    digito_verificador = rut[-1].upper()

    # Calcular el dígito verificador esperado
    suma = 0
    multiplicador = 2

    for digito in reversed(numero):
        suma += int(digito) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    resto = suma % 11
    dv_esperado = 11 - resto if resto != 0 else 0

    # Verificar si el dígito verificador ingresado es válido, considerando 'K' como 10
    if (digito_verificador.isdigit() and int(digito_verificador) == dv_esperado) or (digito_verificador == 'K' and dv_esperado == 10):
        return True
    else:
        return False
    

