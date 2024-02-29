import firebase_admin
from firebase_admin import credentials, db

class Conexion:
    def __init__(self):
        self.__URL = None
        self.__PATH = None
        self.__database = None

    def set_datos(self, urlFR, pathFR):
        try:
            if urlFR is None or pathFR is None:
                raise ValueError("No se puede conectar. Faltan datos de conexión.")
            else:
                self.__URL = urlFR
                self.__PATH = pathFR
        except ValueError as e:
            print(f"Error: {e}")

    def conexion(self):
        try:
            if self.__URL is None or self.__PATH is None:
                raise ValueError("No se puede establecer la conexión. Datos de conexión faltantes.")
            else:
                cred = credentials.Certificate(self.__PATH)
                firebase_admin.initialize_app(cred, {"databaseURL": self.__URL})
                self.__database = db.reference("/")
        except ValueError as e:
            print(f"Error: {e}")

    def guardar_datos(self, data):
        try:
            if self.__database is None:
                raise ValueError("No se puede guardar datos. Conexión no establecida.")
            else:
                self.__database.child(f"usuarios/{data['nombre']}").set(data)
        except ValueError as e:
            print(f"Error: {e}")
