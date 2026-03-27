import json

# APERTURA FICHERO

def load_json():
    
    path = "data/premier_league-24-25.json"
    
    try:
        with open(path, "r", encoding="utf-8") as partidos:
            return json.load(partidos)
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{path}'")
        
    except PermissionError:
        print(f"Error: Sin permisos para leer '{path}'")
        
    except json.JSONDecodeError as e:
        print(f"Error: El archivo no es un JSON válido - {e}")
        
    except OSError as e:
        print(f"Error de sistema al abrir el archivo: {e}")

# MENÚ

def menu():
    
    menu = '''
    1. Listado de equipos (Premier League 24-25)
    2. Cantidad de partidos jugados por jornada
    3. Listado de partidos de un equipo
    4. Listado de los partidos ganados de un equipo
    5. Equipo con más goles hasta la fecha
    6. Salir
    '''
    
    opcion = 0
    
    while opcion != 6:
        print(menu)
        opcion = int(input(">> Introduce una opción (1-6): "))

# LISTAR INFORMACIÓN



# CONTAR INFORMACIÓN



# FILTRAR INFORMACIÓN



# BUSCAR INFORMACIÓN RELACIONADA



# EQUIPO CON MÁS GOLES