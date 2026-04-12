from funciones import *

data = load_json()
if data:
    menu(data)
    
else:
    print("No se pudo cargar el fichero")
