import json
import sys

# APERTURA FICHERO

def load_json():
    
    path = "../data/premier_league-24-25.json"
    
    try:
        with open(path, "r", encoding="utf-8") as partidos:
            data = json.load(partidos)
            return data
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{path}'")
        
    except PermissionError:
        print(f"Error: Sin permisos para leer '{path}'")
        
    except json.JSONDecodeError as e:
        print(f"Error: El archivo no es un JSON válido - {e}")
        
    except OSError as e:
        print(f"Error de sistema al abrir el archivo: {e}")
        
    return None

# MENÚ

def menu(data):
    
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
        
        if opcion == 1:
            get_teams(data)

            for team in get_teams(data):
                print(team)
        
        if opcion == 6:
            print("Saliendo del programa, ¡Hasta luego!")
            
# LISTAR INFORMACIÓN

def get_teams(data):

    teams = set()
    for match in data["matches"]:
        teams.add(match["team1"])
        teams.add(match["team2"])
        
    return sorted(teams)

# CONTAR INFORMACIÓN



# FILTRAR INFORMACIÓN



# BUSCAR INFORMACIÓN RELACIONADA



# EQUIPO CON MÁS GOLES