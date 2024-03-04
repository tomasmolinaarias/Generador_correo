from validador_rut import validar_rut
from validar_telefono import validar_telefono

class Empleado:
    def __init__(self):
        self._nombre = None
        self._apellido = None
        self._telefono = None
        self._rut = None

    def validar_rut(self, rut):
        try:
            if not rut or not validar_rut(rut):
                raise ValueError("Rut no válido")
            return True
        except ValueError as e:
            print(f"Error de validación del Rut: {e}")
            return False

    def validar_telefono(self, telefono):
        try:
            if not telefono or not validar_telefono(telefono):
                raise ValueError("Teléfono no válido")
            return True
        except ValueError as e:
            print(f"Error de validación del teléfono: {e}")
            return False

    def ingreso_datos(self):
        try:
            nombre = input("Ingrese Nombre:  ")
            apellido = input("Ingrese apellido: ")
            telefono= input("Ingrese telefono: ")
            rut = input("Ingrese rut: ")
            if not nombre or not apellido or not telefono or not rut:
                raise ValueError("Faltan datos")
            
            if not self.validar_rut(rut):
                raise ValueError("Rut no válido")
            if not self.validar_telefono(telefono):
                raise ValueError("Teléfono no válido")
            
            self._nombre = nombre
            self._apellido = apellido
            self._telefono = telefono
            self._rut = rut

        except ValueError as e:
            print(f"Error: {e}")

    def obtener_datos(self):
        datos = {
            "nombre": self._nombre,
            "apellido": self._apellido,
            "telefono": self._telefono,
            "rut": self._rut,
            "correo": None
        }
        return datos
