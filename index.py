from firebase import Conexion
from correo import generador_correo
from datos import Empleado
from dotenv import load_dotenv
from validar_rutR import repetido,buscarElemento
import os

load_dotenv()

try:
    url = os.getenv("URL")
    path = os.getenv("credencialJ")
    if url is None or path is None:
        raise ValueError("Alguna de las variables de entorno no está definida.")
    #Conexion
    conexion_instancia = Conexion()
    conexion_instancia.set_datos(url, path)
    conexion_instancia.conexion()
    #ingreso de datos
    empleado = Empleado()
    empleado.ingreso_datos()
    datos= empleado.obtener_datos()
    #generador_correo
    generador = generador_correo()
    generador.Setempresa('empresa.com')
    #Verificar si ya existec usuario
    datosGuardados = conexion_instancia.obtener_datos(datos)
    
    rut = list()
    
    if datosGuardados != None:
        for i in datosGuardados:
            rut.append(datosGuardados[i]['rut'])
        
    else:
        correo_generado = generador.generador_correo(datos["nombre"], datos["apellido"])
        datos["correo"] = correo_generado
        conexion_instancia.guardar_datos(datos)
       
    print(repetido(rut))
    if  repetido(rut) and rut != []:
        rut = []
    
    elif buscarElemento(datos['rut'],rut) and rut != []:
        print("Usuario ya existe 🫠")
        print(f"Usuario: {datosGuardados[datos['rut']]['nombre']}{datosGuardados[datos['rut']]['apellido'] }\nCorreo: {datosGuardados[datos['rut']]['correo']}")
        res = f"Usuario ya existe🤨\nUsuario: {datosGuardados[datos['rut']]['nombre']}{datosGuardados[datos['rut']]['apellido'] }\nCorreo: {datosGuardados[datos['rut']]['correo']}"
        rut = []
    else: 
        print('aqui lin 49') 
        correo_generado = generador.generador_correo(datos["nombre"], datos["apellido"])
        datos["correo"] = correo_generado
        conexion_instancia.guardar_datos(datos) 
except ValueError as e:
  print(f"Error: {e}")