from firebase import Conexion
from correo import generador_correo
from dotenv import load_dotenv
import os

load_dotenv()

try:
    url = os.getenv("URL")
    path = os.getenv("credencialJ")
    
    if url is None or path is None:
        raise ValueError("Alguna de las variables de entorno no está definida.")
    
    conexion_instancia = Conexion()
    conexion_instancia.set_datos(url, path)
    conexion_instancia.conexion()
    
    generador = generador_correo()
    generador.Setempresa('empresa.com')
    
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")

    correo_generado = generador.generador_correo(nombre, apellido)

    datos = {
        'nombre': nombre,
        'apellido': apellido,
        'correo': correo_generado,
        'rut': 202382770
    }
    
    conexion_instancia.guardar_datos(datos)
    
except ValueError as e:
    print(f"Error: {e}")
