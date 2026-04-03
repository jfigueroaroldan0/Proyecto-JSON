import json
import os

# APERTURA FICHERO

def load_json():

    try:
        with open("../data/premier_league-24-25.json", "r", encoding="utf-8") as partidos:
            return json.load(partidos)
            
    except FileNotFoundError:
        print("Error: No se encontró el archivo")
        
    except PermissionError:
        print("Error: Sin permisos para leer el archivo")
        
    except json.JSONDecodeError as e:
        print(f"Error: JSON inválido - {e}")
        
    except OSError as e:
        print(f"Error de sistema: {e}")
        
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
        
        elif opcion == 2:
            contar_partidos_por_jornada(data)
        
        elif opcion == 3:
            partidos_por_equipo(data)
        
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

def contar_partidos_por_jornada(data):

    jornadas = {}

    for match in data["matches"]:
        jornada = match["round"]

        if jornada not in jornadas:
            jornadas[jornada] = []

        jornadas[jornada].append(match)
    
    for jornada, partidos in jornadas.items():
        print(f"{jornada}: {len(partidos)} partidos")

# FILTRAR INFORMACIÓN

def partidos_por_equipo(data):
    equipoabuscar = input(">> Introduce el nombre del equipo: ")
    
    for match in data["matches"]:
        
        if match["team1"] == equipoabuscar or match["team2"] == equipoabuscar:
            fecha = match["date"]
            team1 = match["team1"]
            team2 = match["team2"]
            
            if "score" in match:
                resultado = f"{match['score']['ft'][0]} - {match['score']['ft'][1]}"
                
            else:
                resultado = "Sin resultado"
            
            print(f"{fecha} | {team1} vs {team2} | {resultado}")

# BUSCAR INFORMACIÓN RELACIONADA



# EQUIPO CON MÁS GOLES