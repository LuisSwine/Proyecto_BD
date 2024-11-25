import networkx as nx
import matplotlib.pyplot as plt

def crear_grafo_metrobus():
    
    # Crear grafo dirigido
    G = nx.DiGraph()
    
    # Definir estaciones y conexiones de todas las líneas del Metrobús
    estaciones_metrobús = {
        # Línea 1 (Rojo)
        "Indios Verdes": [("Deportivo 18 de Marzo", 5)],
        "Deportivo 18 de Marzo": [("Euzkaro", 4), ("Indios Verdes", 5)],
        "Euzkaro": [("Potrero", 3), ("Deportivo 18 de Marzo", 4)],
        "Potrero": [("La Raza", 4), ("Euzkaro", 3)],
        "La Raza": [("Circuito", 3), ("Potrero", 4)],
        "Circuito": [("San Simón", 4), ("La Raza", 3)],
        "San Simón": [("Manuel González", 4), ("Circuito", 4)],
        "Manuel González": [("Buenavista", 3), ("San Simón", 4)],
        "Buenavista": [("El Chopo", 2), ("Manuel González", 3)],
        "El Chopo": [("Revolución", 3), ("Buenavista", 2)],
        "Revolución": [("Plaza de la República", 3), ("El Chopo", 3)],
        "Plaza de la República": [("Reforma", 3), ("Revolución", 3)],
        "Reforma": [("Hamburgo", 2), ("Plaza de la República", 3)],
        "Hamburgo": [("Glorieta de los Insurgentes", 3), ("Reforma", 2)],
        "Glorieta de los Insurgentes": [("Durango", 2), ("Hamburgo", 3)],
        "Durango": [("Álvaro Obregón", 2), ("Glorieta de los Insurgentes", 2)],
        "Álvaro Obregón": [("Sonora", 2), ("Durango", 2)],
        "Sonora": [("Campeche", 3), ("Álvaro Obregón", 2)],
        "Campeche": [("Chilpancingo", 2), ("Sonora", 3)],
        "Chilpancingo": [("Nuevo León", 3), ("Campeche", 2)],
        "Nuevo León": [("La Piedad", 3), ("Chilpancingo", 3)],
        "La Piedad": [("Poliforum", 3), ("Nuevo León", 3)],
        "Poliforum": [("Nápoles", 4), ("La Piedad", 3)],
        "Nápoles": [("Colonia del Valle", 3), ("Poliforum", 4)],
        "Colonia del Valle": [("Ciudad de los Deportes", 3), ("Nápoles", 3)],
        "Ciudad de los Deportes": [("Parque Hundido", 3), ("Colonia del Valle", 3)],
        "Parque Hundido": [("Félix Cuevas", 3), ("Ciudad de los Deportes", 3)],
        "Félix Cuevas": [("Río Churubusco", 3), ("Parque Hundido", 3)],
        "Río Churubusco": [("Teatro Insurgentes", 3), ("Félix Cuevas", 3)],
        "Teatro Insurgentes": [("José María Velasco", 3), ("Río Churubusco", 3)],
        "José María Velasco": [("Francia", 3), ("Teatro Insurgentes", 3)],
        "Francia": [("Olivo", 3), ("José María Velasco", 3)],
        "Olivo": [("Altavista", 3), ("Francia", 3)],
        "Altavista": [("La Bombilla", 3), ("Olivo", 3)],
        "La Bombilla": [("Dr. Gálvez", 3), ("Altavista", 3)],
        "Dr. Gálvez": [("Ciudad Universitaria", 4), ("La Bombilla", 3)],
        "Ciudad Universitaria": [("Centro Cultural Universitario", 4), ("Dr. Gálvez", 4)],
        "Centro Cultural Universitario": [("Perisur", 3), ("Ciudad Universitaria", 4)],
        "Perisur": [("Villa Olímpica", 3), ("Centro Cultural Universitario", 3)],
        "Villa Olímpica": [("Corregidora", 3), ("Perisur", 3)],
        "Corregidora": [("Ayuntamiento", 3), ("Villa Olímpica", 3)],
        "Ayuntamiento": [("Fuentes Brotantes", 3), ("Corregidora", 3)],
        "Fuentes Brotantes": [("Santa Úrsula", 4), ("Ayuntamiento", 3)],
        "Santa Úrsula": [("La Joya", 4), ("Fuentes Brotantes", 4)],
        "La Joya": [("El Caminero", 4), ("Santa Úrsula", 4)],
        "El Caminero": [("La Joya", 4)],

        # Línea 2 (Morado)
        "Tepalcates": [("Nicolás Bravo", 4)],
        "Nicolás Bravo": [("Canal de San Juan", 3), ("Tepalcates", 4)],
        "Canal de San Juan": [("General Antonio de León", 3), ("Nicolás Bravo", 3)],
        "General Antonio de León": [("Tláhuac", 3), ("Canal de San Juan", 3)],
        "Tláhuac": [("Rojo Gómez", 3), ("General Antonio de León", 3)],
        "Rojo Gómez": [("Río Frío", 3), ("Tláhuac", 3)],
        "Río Frío": [("Del Moral", 3), ("Rojo Gómez", 3)],
        "Del Moral": [("Leyes de Reforma", 3), ("Río Frío", 3)],
        "Leyes de Reforma": [("CCH Oriente", 3), ("Del Moral", 3)],
        "CCH Oriente": [("Constitución de Apatzingán", 4), ("Leyes de Reforma", 3)],
        "Constitución de Apatzingán": [("UAM-I", 3), ("CCH Oriente", 4)],
        "UAM-I": [("Iztacalco", 4), ("Constitución de Apatzingán", 3)],
        "Iztacalco": [("Goma", 3), ("UAM-I", 4)],
        "Goma": [("Tlacotal", 3), ("Iztacalco", 3)],
        "Tlacotal": [("Canela", 3), ("Goma", 3)],
        "Canela": [("Metro Coyuya", 3), ("Tlacotal", 3)],
        "Metro Coyuya": [("Coyuya", 3), ("Canela", 3)],
        "Coyuya": [("La Viga", 3), ("Metro Coyuya", 3)],
        "La Viga": [("Andrés Molina Enríquez", 3), ("Coyuya", 3)],
        "Andrés Molina Enríquez": [("Las Américas", 3), ("La Viga", 3)],
        "Las Américas": [("Xola", 3), ("Andrés Molina Enríquez", 3)],
        "Xola": [("Álamos", 3), ("Las Américas", 3)],
        "Álamos": [("Centro SCOP", 3), ("Xola", 3)],
        "Centro SCOP": [("Doctor Vértiz", 3), ("Álamos", 3)],
        "Doctor Vértiz": [("Etiopía / Plaza de la Transparencia", 3), ("Centro SCOP", 3)],
        "Etiopía / Plaza de la Transparencia": [("Amores", 3), ("Doctor Vértiz", 3)],
        "Amores": [("Viaducto", 3), ("Etiopía / Plaza de la Transparencia", 3)],
        "Viaducto": [("Nuevo León", 4), ("Amores", 3)],
        "Nuevo León": [("Escandón", 3), ("Viaducto", 4)],
        "Escandón": [("Patriotismo", 3), ("Nuevo León", 3)],
        "Patriotismo": [("De La Salle", 3), ("Escandón", 3)],
        "De La Salle": [("Parque Lira", 3), ("Patriotismo", 3)],
        "Parque Lira": [("Antonio Maceo", 3), ("De La Salle", 3)],
        "Antonio Maceo": [("Tacubaya", 3), ("Parque Lira", 3)],
        "Tacubaya": [("Antonio Maceo", 3)],

        # Línea 3 (Verde Oscuro)
        "Tenayuca": [("San José de la Escalera", 4)],
        "San José de la Escalera": [("Progreso Nacional", 3), ("Tenayuca", 4)],
        "Progreso Nacional": [("Tres Anegas", 3), ("San José de la Escalera", 3)],
        "Tres Anegas": [("Júpiter", 3), ("Progreso Nacional", 3)],
        "Júpiter": [("La Patera", 3), ("Tres Anegas", 3)],
        "La Patera": [("Poniente 146", 3), ("Júpiter", 3)],
        "Poniente 146": [("Montevideo", 4), ("La Patera", 3)],
        "Montevideo": [("Poniente 134", 4), ("Poniente 146", 4)],
        "Poniente 134": [("Poniente 128", 3), ("Montevideo", 4)],
        "Poniente 128": [("Magdalena de las Salinas", 3), ("Poniente 134", 3)],
        "Magdalena de las Salinas": [("Coltongo", 3), ("Poniente 128", 3)],
        "Coltongo": [("Cuitláhuac", 4), ("Magdalena de las Salinas", 3)],
        "Cuitláhuac": [("Héroe de Nacozari", 3), ("Coltongo", 4)],
        "Héroe de Nacozari": [("Hospital La Raza", 3), ("Cuitláhuac", 3)],
        "Hospital La Raza": [("La Raza", 2), ("Héroe de Nacozari", 3)],
        "La Raza": [("Circuito", 3), ("Hospital La Raza", 2)],
        "Circuito": [("San Simón", 4), ("La Raza", 3)],
        "San Simón": [("Tlatelolco", 3), ("Circuito", 4)],
        "Tlatelolco": [("Ricardo Flores Magón", 3), ("San Simón", 3)],
        "Ricardo Flores Magón": [("Guerrero", 3), ("Tlatelolco", 3)],
        "Guerrero": [("Buenavista", 2), ("Ricardo Flores Magón", 3)],
        "Buenavista": [("Mina", 2), ("Guerrero", 2)],
        "Mina": [("Hidalgo", 2), ("Buenavista", 2)],
        "Hidalgo": [("Juárez", 2), ("Mina", 2)],
        "Juárez": [("Balderas", 3), ("Hidalgo", 2)],
        "Balderas": [("Cuauhtémoc", 3), ("Juárez", 3)],
        "Cuauhtémoc": [("Jardín Pushkin", 2), ("Balderas", 3)],
        "Jardín Pushkin": [("Hospital General", 2), ("Cuauhtémoc", 2)],
        "Hospital General": [("Dr. Márquez", 2), ("Jardín Pushkin", 2)],
        "Dr. Márquez": [("Centro Médico", 3), ("Hospital General", 2)],
        "Centro Médico": [("Obrero Mundial", 3), ("Dr. Márquez", 3)],
        "Obrero Mundial": [("Etiopía / Plaza de la Transparencia", 2), ("Centro Médico", 3)],
        "Etiopía / Plaza de la Transparencia": [("Luz Saviñón", 2), ("Obrero Mundial", 2)],
        "Luz Saviñón": [("Eugenia", 3), ("Etiopía / Plaza de la Transparencia", 2)],
        "Eugenia": [("División del Norte", 3), ("Luz Saviñón", 3)],
        "División del Norte": [("Miguel Laurent", 3), ("Eugenia", 3)],
        "Miguel Laurent": [("Pueblo Santa Cruz Atoyac", 3), ("División del Norte", 3)],
        "Pueblo Santa Cruz Atoyac": [("Miguel Laurent", 3)],

        # Línea 4 (Naranja)
        "Buenavista": [("Delegación Cuauhtémoc", 2)],
        "Delegación Cuauhtémoc": [("México Tenochtitlán", 3), ("Buenavista", 2)],
        "México Tenochtitlán": [("Museo San Carlos", 2), ("Delegación Cuauhtémoc", 3)],
        "Museo San Carlos": [("Plaza de la República", 2), ("México Tenochtitlán", 2)],
        "Plaza de la República": [("Glorieta de Colón", 2), ("Museo San Carlos", 2)],
        "Glorieta de Colón": [("Expo Reforma", 3), ("Plaza de la República", 2)],
        "Expo Reforma": [("Vocacional 5", 3), ("Glorieta de Colón", 3)],
        "Vocacional 5": [("Juárez", 2), ("Expo Reforma", 3)],
        "Juárez": [("Eje Central", 2), ("Vocacional 5", 2)],
        "Eje Central": [("Hidalgo", 2), ("Juárez", 2)],
        "Hidalgo": [("Bellas Artes", 2), ("Eje Central", 2)],
        "Bellas Artes": [("Teatro Blanquita", 2), ("Hidalgo", 2)],
        "Teatro Blanquita": [("República de Chile", 2), ("Bellas Artes", 2)],
        "República de Chile": [("República de Argentina", 2), ("Teatro Blanquita", 2)],
        "República de Argentina": [("Mercado Abelardo L. Rodríguez", 3), ("República de Chile", 2)],
        "Mercado Abelardo L. Rodríguez": [("Mixcalco", 3), ("República de Argentina", 3)],
        "Mixcalco": [("Ferrocarril de Cintura", 2), ("Mercado Abelardo L. Rodríguez", 3)],
        "Ferrocarril de Cintura": [("Morelos", 3), ("Mixcalco", 2)],
        "Morelos": [("Archivo General de la Nación", 3), ("Ferrocarril de Cintura", 3)],
        "Archivo General de la Nación": [("San Lázaro", 2), ("Morelos", 3), ("Pantitlán", 8)],
        "San Lázaro": [("Terminal 1 (Aeropuerto)", 8), ("Archivo General de la Nación", 2)],
        "Terminal 1 (Aeropuerto)": [("Terminal 2 (Aeropuerto)", 3), ("San Lázaro", 8)],
        "Terminal 2 (Aeropuerto)": [("Terminal 1 (Aeropuerto)", 3)],
        "Pantitlán": [("Archivo General de la Nación", 8)],
        

        # Línea 5 (Amarillo)
        "Río de los Remedios": [("314. Memorial New's Divine", 3)],
        "314. Memorial New's Divine": [("5 de Mayo", 2), ("Río de los Remedios", 3)],
        "5 de Mayo": [("Vasco de Quiroga", 3), ("314. Memorial New's Divine", 2)],
        "Vasco de Quiroga": [("El Coyol", 2), ("5 de Mayo", 3)],
        "El Coyol": [("Preparatoria 3", 2), ("Vasco de Quiroga", 2)],
        "Preparatoria 3": [("San Juan de Aragón", 3), ("El Coyol", 2)],
        "San Juan de Aragón": [("Río Guadalupe", 2), ("Preparatoria 3", 3)],
        "Río Guadalupe": [("Talismán", 3), ("San Juan de Aragón", 2)],
        "Talismán": [("Victoria", 3), ("Río Guadalupe", 3)],
        "Victoria": [("Oriente 101", 2), ("Talismán", 3)],
        "Oriente 101": [("Río Santa Coleta", 3), ("Victoria", 2)],
        "Río Santa Coleta": [("Río Consulado", 3), ("Oriente 101", 3)],
        "Río Consulado": [("Canal del Norte", 3), ("Río Santa Coleta", 3)],
        "Canal del Norte": [("Deportivo Eduardo Molina", 2), ("Río Consulado", 3)],
        "Deportivo Eduardo Molina": [("Mercado Morelos", 2), ("Canal del Norte", 2)],
        "Mercado Morelos": [("Archivo General de la Nación", 3), ("Deportivo Eduardo Molina", 2)],
        "Archivo General de la Nación": [("San Lázaro", 2), ("Mercado Morelos", 3)],
        "San Lázaro": [("Venustiano Carranza", 2), ("Archivo General de la Nación", 2)],
        "Venustiano Carranza": [("Avenida del Taller", 2), ("San Lázaro", 2)],
        "Avenida del Taller": [("Mixiuhca", 3), ("Venustiano Carranza", 2)],
        "Mixiuhca": [("Hospital General Troncoso", 3), ("Avenida del Taller", 3)],
        "Hospital General Troncoso": [("Metro Coyuya", 2), ("Mixiuhca", 3)],
        "Metro Coyuya": [("Canela", 3), ("Hospital General Troncoso", 2)],
        "Canela": [("Tlacotal", 2), ("Metro Coyuya", 3)],
        "Tlacotal": [("Goma", 2), ("Canela", 2)],
        "Goma": [("Iztacalco", 3), ("Tlacotal", 2)],
        "Iztacalco": [("UPIICSA", 3), ("Goma", 3)],
        "UPIICSA": [("CCH Oriente", 2), ("Iztacalco", 3)],
        "CCH Oriente": [("Leyes de Reforma", 2), ("UPIICSA", 2)],
        "Leyes de Reforma": [("Del Moral", 3), ("CCH Oriente", 2)],
        "Del Moral": [("Río Frío", 2), ("Leyes de Reforma", 3)],
        "Río Frío": [("Rojo Gómez", 2), ("Del Moral", 2)],
        "Rojo Gómez": [("Tláhuac", 3), ("Río Frío", 2)],
        "Tláhuac": [("General Antonio de León", 3), ("Rojo Gómez", 3)],
        "General Antonio de León": [("Canal de San Juan", 3), ("Tláhuac", 3)],
        "Canal de San Juan": [("Nicolás Bravo", 3), ("General Antonio de León", 3)],
        "Nicolás Bravo": [("Tepalcates", 4), ("Canal de San Juan", 3)],
        "Tepalcates": [("Nicolás Bravo", 4)],

        # Línea 6 (Verde Claro)
        "El Rosario": [("Tezozómoc", 3)],
        "Tezozómoc": [("UAM Azcapotzalco", 2), ("El Rosario", 3)],
        "UAM Azcapotzalco": [("Ferrería / Arena Ciudad de México", 2), ("Tezozómoc", 2)],
        "Ferrería / Arena Ciudad de México": [("Norte 45", 3), ("UAM Azcapotzalco", 2)],
        "Norte 45": [("Montevideo", 3), ("Ferrería / Arena Ciudad de México", 3)],
        "Montevideo": [("Lindavista-Vallejo", 3), ("Norte 45", 3)],
        "Lindavista-Vallejo": [("Instituto del Petróleo", 3), ("Montevideo", 3)],
        "Instituto del Petróleo": [("Poniente 128", 3), ("Lindavista-Vallejo", 3)],
        "Poniente 128": [("Poniente 134", 3), ("Instituto del Petróleo", 3)],
        "Poniente 134": [("Poniente 146", 3), ("Poniente 128", 3)],
        "Poniente 146": [("Vallejo", 3), ("Poniente 134", 3)],
        "Vallejo": [("Coltongo", 3), ("Poniente 146", 3)],
        "Coltongo": [("Cuitláhuac", 3), ("Vallejo", 3)],
        "Cuitláhuac": [("La Raza", 3), ("Coltongo", 3)],
        "La Raza": [("Circuito", 2), ("Cuitláhuac", 3)],
        "Circuito": [("San Simón", 3), ("La Raza", 2)],
        "San Simón": [("Deportivo 18 de Marzo", 3), ("Circuito", 3)],
        "Deportivo 18 de Marzo": [("Euzkaro", 2), ("San Simón", 3)],
        "Euzkaro": [("Misterios", 3), ("Deportivo 18 de Marzo", 2)],
        "Misterios": [("De los Misterios", 2), ("Euzkaro", 3)],
        "De los Misterios": [("Hospital La Villa", 3), ("Misterios", 2)],
        "Hospital La Villa": [("Martín Carrera", 3), ("De los Misterios", 3)],
        "Martín Carrera": [("San Juan de Aragón", 4), ("Hospital La Villa", 3)],
        "San Juan de Aragón": [("Gran Canal", 3), ("Martín Carrera", 4)],
        "Gran Canal": [("Casas Alemán", 3), ("San Juan de Aragón", 3)],
        "Casas Alemán": [("Pueblo San Juan de Aragón", 2), ("Gran Canal", 3)],
        "Pueblo San Juan de Aragón": [("Loreto Fabela", 2), ("Casas Alemán", 2)],
        "Loreto Fabela": [("482", 3), ("Pueblo San Juan de Aragón", 2)],
        "482": [("416 Oriente", 3), ("Loreto Fabela", 3)],
        "416 Oriente": [("416 Poniente", 2), ("482", 3)],
        "416 Poniente": [("Deportivo Los Galeana", 2), ("416 Oriente", 2)],
        "Deportivo Los Galeana": [("Ampliación Providencia", 2), ("416 Poniente", 2)],
        "Ampliación Providencia": [("Volcán de Fuego", 2), ("Deportivo Los Galeana", 2)],
        "Volcán de Fuego": [("La Pradera", 2), ("Ampliación Providencia", 2)],
        "La Pradera": [("Francisco Morazán", 2), ("Volcán de Fuego", 2)],
        "Francisco Morazán": [("Villa de Aragón", 2), ("La Pradera", 2)],
        "Villa de Aragón": [("Francisco Morazán", 2)],

        # Línea 7 (Azul Marino)
        "Indios Verdes": [("Hospital Infantil La Villa", 4)],
        "Hospital Infantil La Villa": [("De los Misterios", 3), ("Indios Verdes", 4)],
        "De los Misterios": [("Garrido", 2), ("Hospital Infantil La Villa", 3)],
        "Garrido": [("Martín Carrera", 3), ("De los Misterios", 2)],
        "Martín Carrera": [("Clínica 18", 3), ("Garrido", 3)],
        "Clínica 18": [("Necaxa", 2), ("Martín Carrera", 3)],
        "Necaxa": [("La Villa", 2), ("Clínica 18", 2)],
        "La Villa": [("Misterios", 3), ("Necaxa", 2)],
        "Misterios": [("Cantera", 3), ("La Villa", 3)],
        "Cantera": [("Talisman", 3), ("Misterios", 3)],
        "Talisman": [("Euzkaro", 2), ("Cantera", 3)],
        "Euzkaro": [("Deportivo 18 de Marzo", 3), ("Talisman", 2)],
        "Deportivo 18 de Marzo": [("Potrero", 3), ("Euzkaro", 3)],
        "Potrero": [("La Raza", 3), ("Deportivo 18 de Marzo", 3)],
        "La Raza": [("Circuito", 2), ("Potrero", 3)],
        "Circuito": [("San Simón", 3), ("La Raza", 2)],
        "San Simón": [("Manuel González", 2), ("Circuito", 3)],
        "Manuel González": [("Buenavista", 2), ("San Simón", 2)],
        "Buenavista": [("El Chopo", 2), ("Manuel González", 2)],
        "El Chopo": [("Revolución", 2), ("Buenavista", 2)],
        "Revolución": [("Plaza de la República", 2), ("El Chopo", 2)],
        "Plaza de la República": [("Reforma", 2), ("Revolución", 2)],
        "Reforma": [("Hamburgo", 2), ("Plaza de la República", 2)],
        "Hamburgo": [("Glorieta de Colón", 2), ("Reforma", 2)],
        "Glorieta de Colón": [("Expo Reforma", 2), ("Hamburgo", 2)],
        "Expo Reforma": [("Vocacional 5", 2), ("Glorieta de Colón", 2)],
        "Vocacional 5": [("Juárez", 2), ("Expo Reforma", 2)],
        "Juárez": [("El Caballito", 2), ("Vocacional 5", 2)],
        "El Caballito": [("La Palma", 2), ("Juárez", 2)],
        "La Palma": [("El Ángel", 2), ("El Caballito", 2)],
        "El Ángel": [("La Diana", 2), ("La Palma", 2)],
        "La Diana": [("Mariana Nacional", 2), ("El Ángel", 2)],
        "Mariana Nacional": [("Auditorio", 3), ("La Diana", 2)],
        "Auditorio": [("Campo Marte", 2), ("Mariana Nacional", 3)],
        "Campo Marte": [("Auditorio", 2)]
    }

    # Conexiones entre líneas
    conexiones = [
        "Buenavista", "San Lázaro", "Indios Verdes", "Deportivo 18 de Marzo",
        "La Raza", "Tacubaya", "Centro Médico", "Etiopía / Plaza de la Transparencia",
        "Reforma", "Hidalgo", "Plaza de la República", "Teatro Blanquita",
        "Coyuya", "Mixcalco", "Morelos", "Archivo General de la Nación"
    ]

    lineas = {
        "Línea 1" : [
            "Indios Verdes", "Deportivo 18 de Marzo", "Euzkaro", "Potrero", "La Raza",
            "Circuito", "San Simón", "Manuel González", "Buenavista", "El Chopo",
            "Revolución", "Plaza de la República", "Reforma", "Hamburgo",
            "Glorieta de los Insurgentes", "Durango", "Álvaro Obregón", "Sonora",
            "Campeche", "Chilpancingo", "Nuevo León", "La Piedad", "Poliforum",
            "Nápoles", "Colonia del Valle", "Ciudad de los Deportes", "Parque Hundido",
            "Félix Cuevas", "Río Churubusco", "Teatro Insurgentes", "José María Velasco",
            "Francia", "Olivo", "Altavista", "La Bombilla", "Dr. Gálvez",
            "Ciudad Universitaria", "Centro Cultural Universitario", "Perisur",
            "Villa Olímpica", "Corregidora", "Ayuntamiento", "Fuentes Brotantes",
            "Santa Úrsula", "La Joya", "El Caminero"
        ],

    # Línea 2 (Morado)
        "Línea 2" : [
            "Tepalcates", "Nicolás Bravo", "Canal de San Juan", "General Antonio de León",
            "Tláhuac", "Rojo Gómez", "Río Frío", "Del Moral", "Leyes de Reforma",
            "CCH Oriente", "Constitución de Apatzingán", "UAM-I", "Iztacalco", "Goma",
            "Tlacotal", "Canela", "Metro Coyuya", "Coyuya", "La Viga", "Andrés Molina Enríquez",
            "Las Américas", "Xola", "Álamos", "Centro SCOP", "Doctor Vértiz",
            "Etiopía / Plaza de la Transparencia", "Amores", "Viaducto", "Nuevo León",
            "Escandón", "Patriotismo", "De La Salle", "Parque Lira", "Antonio Maceo", "Tacubaya"
        ],

        # Línea 3 (Verde)
        "Línea 3" : [
            "Tenayuca", "San José de la Escalera", "Progreso Nacional", "Tres Anegas",
            "Júpiter", "La Patera", "Poniente 146", "Montevideo", "Poniente 134",
            "Poniente 128", "Magdalena de las Salinas", "Coltongo", "Cuitláhuac",
            "Héroe de Nacozari", "Hospital La Raza", "La Raza", "Circuito", "San Simón",
            "Tlatelolco", "Ricardo Flores Magón", "Guerrero", "Buenavista", "Mina",
            "Hidalgo", "Juárez", "Balderas", "Cuauhtémoc", "Jardín Pushkin",
            "Hospital General", "Dr. Márquez", "Centro Médico", "Obrero Mundial",
            "Etiopía / Plaza de la Transparencia", "Luz Saviñón", "Eugenia",
            "División del Norte", "Miguel Laurent", "Pueblo Santa Cruz Atoyac"
        ],

        # Línea 4 (Naranja)
        "Línea 4" : [
            "Buenavista", "Delegación Cuauhtémoc", "México Tenochtitlán", "Museo San Carlos",
            "Plaza de la República", "Glorieta de Colón", "Expo Reforma", "Vocacional 5",
            "Juárez", "Eje Central", "Hidalgo", "Bellas Artes", "Teatro Blanquita",
            "República de Chile", "República de Argentina", "Mercado Abelardo L. Rodríguez",
            "Mixcalco", "Ferrocarril de Cintura", "Morelos", "Archivo General de la Nación",
            "San Lázaro", "Terminal 1 (Aeropuerto)", "Terminal 2 (Aeropuerto)"
        ],

        # Línea 5 (Amarilla)
        "Línea 5" : [
            "Río de los Remedios", "314. Memorial New's Divine", "5 de Mayo",
            "Vasco de Quiroga", "El Coyol", "Preparatoria 3", "San Juan de Aragón",
            "Río Guadalupe", "Talismán", "Victoria", "Oriente 101", "Río Santa Coleta",
            "Río Consulado", "Canal del Norte", "Deportivo Eduardo Molina",
            "Mercado Morelos", "Archivo General de la Nación", "San Lázaro", "Venustiano Carranza",
            "Avenida del Taller", "Mixiuhca", "Hospital General Troncoso", "Metro Coyuya"
        ],

        # Línea 6 (Rosa)
        "Línea 6" : [
            "El Rosario", "Tezozómoc", "UAM Azcapotzalco", "Ferrería / Arena Ciudad de México",
            "Norte 45", "Vallejo", "Lindavista-Vallejo", "Instituto del Petróleo",
            "Poniente 128", "Poniente 134", "Poniente 146", "La Raza", "Circuito",
            "San Simón", "Deportivo 18 de Marzo", "Euzkaro", "Misterios", "De los Misterios",
            "Hospital La Villa", "Martín Carrera", "San Juan de Aragón", "Gran Canal",
            "Casas Alemán", "Pueblo San Juan de Aragón", "Loreto Fabela", "482", "416 Oriente",
            "416 Poniente", "Deportivo Los Galeana", "Ampliación Providencia",
            "Volcán de Fuego", "La Pradera", "Francisco Morazán", "Villa de Aragón"
        ],

        # Línea 7 (Verde Oscuro)
        "Línea 7" : [
            "Indios Verdes", "Hospital Infantil La Villa", "De los Misterios", "Garrido",
            "Martín Carrera", "Clínica 18", "Necaxa", "La Villa", "Misterios", "Cantera",
            "Talisman", "Euzkaro", "Deportivo 18 de Marzo", "Potrero", "La Raza",
            "Circuito", "San Simón", "Manuel González", "Buenavista", "El Chopo",
            "Revolución", "Plaza de la República", "Reforma", "Hamburgo", "Glorieta de Colón",
            "Expo Reforma", "Vocacional 5", "Juárez", "El Caballito", "La Palma", "El Ángel",
            "La Diana", "Mariana Nacional", "Auditorio", "Campo Marte"
        ]
    }
    # Línea 1 (Rojo)
    

    # Convertir nombres de estaciones y conexiones para agregar "_MB"
    estaciones_metrobús_actualizadas = {}
    for estacion, conexiones in estaciones_metrobús.items():
        estacion_mb = f"{estacion}_MB"
        conexiones_mb = [(f"{destino}_MB", tiempo) for destino, tiempo in conexiones]
        estaciones_metrobús_actualizadas[estacion_mb] = conexiones_mb

    # Agregar estaciones y conexiones al grafo
    for estacion, conexiones in estaciones_metrobús_actualizadas.items():
        for destino, tiempo in conexiones:
            G.add_edge(estacion, destino, weight=tiempo)
    
    # Agregar líneas como atributo de cada nodo
    for linea, estaciones in lineas.items():
        for estacion in estaciones:
            estacion_mb = f"{estacion}_MB"
            if estacion_mb in G.nodes:
                nx.set_node_attributes(G, {estacion_mb: linea}, "linea")
    
    
    return G

G_metrobús = crear_grafo_metrobus()

# Verificar atributos de una estación específica
print(G_metrobús.nodes["Indios Verdes_MB"]["linea"])