import random

class generador_correo():
    def __init__(self):
        self.__dominio = None

    def Setempresa(self, empresa):
        try:
            if empresa is None:
                raise ValueError('No existe dominio')
            else:
                self.__dominio = empresa
        except ValueError as e:
            print(f"Error: {e}")

    def generador_correo(self, nombre, apellido):
        try:
            if nombre is None or apellido is None:
                raise ValueError('Falta un dato del empleado')
            else:
                numero = random.randint(100, 999)
                correo = f"{nombre[0].lower()}.{apellido.lower()}{numero}@{self.__dominio}"
                return correo
        except ValueError as e:
            print(f"Error: {e}")
