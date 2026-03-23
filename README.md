# Proyecto-JSON

Fuente fichero JSON: https://github.com/openfootball/football.json/blob/master/2024-25/en.1.json

Se dispone de un fichero JSON que contiene información de la temporada 2024-25 de la Premier League inglesa. La estructura principal del JSON es la siguiente:

name: nombre de la competición.  
rounds: lista de jornadas o rondas, cada una con:  
name: nombre de la jornada.  
matches: lista de partidos, donde cada partido tiene:  
date: fecha del partido.  
team1 y team2: nombres de los equipos.  
score: resultado con ft (full-time) indicando goles de cada equipo.  

# Ejercicio 1 - Listar información

Lista todos los equipos que participan en la Premier League 2024-25.
Imprime una lista única de nombres de equipos sin repeticiones.

# Ejercicio 2 - Contar información

Cuenta cuántos partidos se han jugado en cada jornada.
Para cada jornada, mostrar su nombre y el número de partidos disputados.

# Ejercicio 3 - Buscar o filtrar información

Pide al usuario el nombre de un equipo y muestra todos los partidos en los que participa ese equipo.
Cada partido debe mostrar fecha, rival y resultado si está disponible.

# Ejercicio 4 - Buscar información relacionada

Pide al usuario el nombre de un equipo y muestra todas las jornadas en las que dicho equipo ganó algún partido.
Muestra jornada, rival y resultado de los partidos ganados por el equipo.

# Ejercicio 5 - Ejercicio libre

Determina qué equipo ha marcado más goles en total hasta el momento (sumando todos los goles de cada partido) y muestra el total de goles.
Imprime el nombre del equipo y número total de goles anotados.
