import json
import os

def linea_decorativa():
    print("═" * 60)

def sublinea():
    print("─" * 60)

def limpiar_pantalla():
    try:
        comando = "cls" if os.name == "nt" else "clear"
        os.system(comando)
    except:
        print("No se pudo limpiar la pantalla")

def pausa():
    input("\nPulsa ENTER para volver al menú...")

# APERTURA FICHERO

def load_json():

    try:
        with open("../data/premier_league-24-25.json", "r", encoding="utf-8") as partidos:
            return json.load(partidos)
            
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo especificado.")

    except PermissionError:
        print("❌ Error: No tienes permisos para leer el archivo.")

    except json.JSONDecodeError as e:
        print(f"❌ Error: El archivo JSON es inválido → {e}")

    except OSError as e:
        print(f"❌ Error del sistema: {e}")

    return None

# MENÚ

def menu(data):

    menu = '''
        [1] Listado de equipos (Premier League 24-25)
        [2] Cantidad de partidos jugados por jornada
        [3] Listado de partidos de un equipo
        [4] Listado de los partidos ganados de un equipo
        [5] Equipo con más goles hasta la fecha
        [6] Salir
    '''

    opcion = 0
    encabezado = "MENÚ GESTIÓN DE PARTIDOS PREMIER LEAGUE 24-25"

    while opcion != 6:

        limpiar_pantalla()
        linea_decorativa()
        print(encabezado.center(60))
        linea_decorativa()
        print(menu)
        linea_decorativa()

        try:
            opcion = int(input(">> Introduce una opción (1-6): "))

            if opcion == 1:
                limpiar_pantalla()
                linea_decorativa()
                print("LISTADO DE EQUIPOS".center(60))
                linea_decorativa()

                equipos = get_teams(data)
                contador = 0
                for team in equipos:
                    contador += 1
                    print(f"{contador}. {team}")

                print(f"\nTotal de equipos: {contador}")
                pausa()

            elif opcion == 2:
                limpiar_pantalla()
                linea_decorativa()
                print("PARTIDOS POR JORNADA".center(60))
                linea_decorativa()

                contar_partidos_por_jornada(data)

                total_partidos = len(data["matches"])
                print(f"\nTotal de partidos registrados: {total_partidos}")
                pausa()

            elif opcion == 3:
                limpiar_pantalla()
                linea_decorativa()
                print("PARTIDOS DE UN EQUIPO".center(60))
                linea_decorativa()

                contador = partidos_por_equipo(data)
                print(f"\nTotal de partidos encontrados: {contador}")
                pausa()

            elif opcion == 4:
                limpiar_pantalla()
                linea_decorativa()
                print("VICTORIAS DE UN EQUIPO".center(60))
                linea_decorativa()

                contador = victorias_equipo(data)
                print(f"\nTotal de victorias: {contador}")
                pausa()

            elif opcion == 5:
                limpiar_pantalla()
                linea_decorativa()
                print("EQUIPO CON MÁS GOLES".center(60))
                linea_decorativa()

                maximo_goleador(data)
                pausa()

            elif opcion == 6:
                print("Saliendo del programa, ¡Hasta luego!")

            else:
                print("❌ Opción fuera de rango. Introduce un número entre 1 y 6.")
                pausa()

        except ValueError:
            print("❌ Error: Debes introducir un número válido.")
            pausa()

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

    equipoabuscar = input(">> Introduce el nombre del equipo: ").strip()
    contador = 0
    
    for match in data["matches"]:
        
        if match["team1"] == equipoabuscar or match["team2"] == equipoabuscar:
            contador += 1
            fecha = match["date"]
            team1 = match["team1"]
            team2 = match["team2"]
            
            if "score" in match:
                resultado = f"{match['score']['ft'][0]} - {match['score']['ft'][1]}"
            else:
                resultado = "Sin resultado"
            
            print(f"{fecha} | {team1} vs {team2} | {resultado}")

    if contador == 0:
        print("❌ No se encontraron partidos para ese equipo.")

    return contador

# BUSCAR INFORMACIÓN RELACIONADA

def victorias_equipo(data):

    equipo = input("Equipo: ").strip().lower()
    victorias = 0
 
    for partido in data["matches"]:
        resultado = partido.get("score", {}).get("ft")
        local = partido["team1"]
        visitante = partido["team2"]
        jornada = partido["round"]
 
        if resultado:
            if local.lower() == equipo and resultado[0] > resultado[1]:
                victorias += 1
                print(f"{jornada} | Rival: {visitante} | {resultado[0]}-{resultado[1]}")
            elif visitante.lower() == equipo and resultado[1] > resultado[0]:
                victorias += 1
                print(f"{jornada} | Rival: {local} | {resultado[1]}-{resultado[0]}")

    if victorias == 0:
        print("❌ No se encontraron victorias para ese equipo.")

    return victorias

# EQUIPO CON MÁS GOLES

def maximo_goleador(data):

    goles_por_equipo = {}
 
    for partido in data["matches"]:
        resultado = partido.get("score", {}).get("ft")
 
        if resultado:
            equipo1 = partido["team1"]
            equipo2 = partido["team2"]
 
            goles_por_equipo[equipo1] = goles_por_equipo.get(equipo1, 0) + resultado[0]
            goles_por_equipo[equipo2] = goles_por_equipo.get(equipo2, 0) + resultado[1]
 
    equipo_maximo = max(goles_por_equipo, key=goles_por_equipo.get)
    print(f"{equipo_maximo}: {goles_por_equipo[equipo_maximo]} goles")