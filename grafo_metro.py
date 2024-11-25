import networkx as nx
import matplotlib.pyplot as plt


def crear_grafo_metro():
    
    # Crear un grafo dirigido
    G = nx.DiGraph()

    # Definición de las estaciones y conexiones
    # Cada estación tiene su nombre y sus conexiones (estaciones conectadas)
    estaciones = {
    "Observatorio": [("Tacubaya", 5)],
    "Tacubaya": [("Observatorio", 5), ("Juanacatlán", 5), ("Constituyentes", 5), ("San Pedro de los Pinos", 5), ("Patriotismo", 5)],
    "Juanacatlán": [("Tacubaya", 5), ("Chapultepec", 5)],
    "Chapultepec": [("Juanacatlán", 5), ("Sevilla", 5)],
    "Sevilla": [("Chapultepec", 5), ("Insurgentes", 5)],
    "Insurgentes": [("Sevilla", 5), ("Cuauhtémoc", 5)],
    "Cuauhtémoc": [("Insurgentes", 5), ("Balderas", 5)],
    "Balderas": [("Cuauhtémoc", 5), ("Salto del Agua", 5), ("Juárez", 5), ("Niños Héroes", 5)],
    "Salto del Agua": [("Balderas", 5), ("Isabel la Católica", 5), ("San Juan de Letrán", 5), ("Doctores", 5)],
    "Isabel la Católica": [("Salto del Agua", 5), ("Pino Suárez", 5)],
    "Pino Suárez": [("Isabel la Católica", 5), ("Merced", 5), ("Zócalo", 5), ("San Antonio Abad", 5)],
    "Merced": [("Pino Suárez", 5), ("Candelaria", 5)],
    "Candelaria": [("Merced", 5), ("San Lázaro", 5), ("Morelos", 5), ("Fray Servando", 5)],
    "San Lázaro": [("Moctezuma", 5), ("Candelaria", 5), ("Morelos", 5), ("Flores Magón", 5)],
    "Moctezuma": [("San Lázaro", 5), ("Balbuena", 5)],
    "Balbuena": [("Moctezuma", 5), ("Blvd. Puerto Aéreo", 5)],
    "Blvd. Puerto Aéreo": [("Balbuena", 5), ("Gómez Farías", 5)],
    "Gómez Farías": [("Blvd. Puerto Aéreo", 5), ("Zaragoza", 5)],
    "Zaragoza": [("Gómez Farías", 5), ("Pantitlán", 5)],
    "Pantitlán": [("Zaragoza", 5), ("Hangares", 5), ("Puebla", 5), ("Agrícola Oriental", 5)],
    
    "Cuatro Caminos": [("Panteones", 5)],
    "Panteones": [("Tacuba", 5), ("Cuatro Caminos", 5)],
    "Tacuba": [("Panteones", 5), ("Cuitláhuac", 5), ("Refinería", 5), ("San Joaquín", 5)],
    "Cuitláhuac": [("Tacuba", 5), ("Popotla", 5)],
    "Popotla": [("Cuitláhuac", 5), ("Colegio Militar", 5)],
    "Colegio Militar": [("Popotla", 5), ("Normal", 5)],
    "Normal": [("Colegio Militar", 5), ("San Cosme", 5)],
    "San Cosme": [("Normal", 5), ("Revolución", 5)],
    "Revolución": [("San Cosme", 5), ("Hidalgo", 5)],
    "Hidalgo": [("Revolución", 5), ("Bellas Artes", 5), ("Guerrero", 5), ("Juárez", 5)],
    "Bellas Artes": [("Hidalgo", 5), ("Allende", 5), ("Garibaldi", 5), ("San Juan de Letrán", 5)],
    "Allende": [("Bellas Artes", 5), ("Zócalo", 5)],
    "Zócalo": [("Allende", 5), ("San Antonio Abad", 5)],
    "San Antonio Abad": [("Zócalo", 5), ("Chabacano", 5)],
    "Chabacano": [("San Antonio Abad", 5), ("Viaducto", 5), ("Obrera", 5), ("La Viga", 5), ("Lázaro Cárdenas", 5), ("Jamaica", 5)],
    "Viaducto": [("Chabacano", 5), ("Xola", 5)],
    "Xola": [("Viaducto", 5), ("Villa de Cortés", 5)],
    "Villa de Cortés": [("Xola", 5), ("Nativitas", 5)],
    "Nativitas": [("Villa de Cortés", 5), ("Portales", 5)],
    "Portales": [("Nativitas", 5), ("Ermita", 5)],
    "Ermita": [("Portales", 5), ("General Anaya", 5), ("Eje Central", 5), ("Mexicaltzingo", 5)],
    "General Anaya": [("Ermita", 5), ("Tasqueña", 5)],
    "Tasqueña": [("General Anaya", 5)],

    "Indios Verdes": [("Deportivo 18 de Marzo", 5)],
    "Deportivo 18 de Marzo": [("Potrero", 5), ("Indios Verdes", 5), ("La Villa", 5), ("Lindavista", 5)],
    "Potrero": [("Deportivo 18 de Marzo", 5), ("La Raza", 5)],
    "La Raza": [("Potrero", 5), ("Tlatelolco", 5), ("Autobuses del Norte", 5), ("Misterios", 5)],
    "Tlatelolco": [("La Raza", 5), ("Guerrero", 5)],
    "Guerrero": [("Tlatelolco", 5), ("Hidalgo", 5), ("Buenavista", 5)],
    "Juárez": [("Hidalgo", 5), ("Balderas", 5)],
    "Niños Héroes": [("Balderas", 5), ("Hospital General", 5)],
    "Hospital General": [("Centro Médico", 5), ("Niños Héroes", 5)],
    "Centro Médico": [("Hospital General", 5), ("Etiopía", 5), ("Chilpancingo", 5), ("Lázaro Cárdenas", 5)],
    "Etiopía": [("Centro Médico", 5), ("Eugenia", 5)],
    "Eugenia": [("Etiopía", 5), ("División del Norte", 5)],
    "División del Norte": [("Eugenia", 5), ("Zapata", 5)],
    "Zapata": [("División del Norte", 5), ("Coyoacán", 5), ("Hospital 20 de Noviembre", 5), ("Parque de los Venados", 5)],
    "Coyoacán": [("Zapata", 5), ("Viveros", 5)],
    "Viveros": [("Coyoacán", 5), ("Miguel Ángel de Quevedo", 5)],
    "Miguel Ángel de Quevedo": [("Viveros", 5), ("Copilco", 5)],
    "Copilco": [("Miguel Ángel de Quevedo", 5), ("Universidad", 5)],
    "Universidad": [("Copilco", 5)],

    "Martín Carrera": [("Talisman", 5), ("La Villa", 5)],
    "Talisman": [("Martín Carrera", 5), ("Bondojito", 5)],
    "Bondojito": [("Talisman", 5), ("Consulado", 5)],
    "Consulado": [("Bondojito", 5), ("Canal del Norte", 5), ("Valle Gómez", 5), ("Eduardo Molina", 5)],
    "Canal del Norte": [("Consulado", 5), ("Morelos", 5)],
    "Morelos": [("Canal del Norte", 5), ("Fray Servando", 5)],
    "Fray Servando": [("Morelos", 5), ("Jamaica", 5)],
    "Jamaica": [("Santa Anita", 5), ("Fray Servando", 5), ("Chabacano", 5), ("Mixiuhca", 5)],
    "Santa Anita": [("Jamaica", 5), ("La Viga", 5), ("Coyuya", 5)],

    "Politécnico": [("Instituto del Petróleo", 5)],
    "Instituto del Petróleo": [("Autobuses del Norte", 5), ("Politécnico", 5), ("Vallejo", 5), ("Lindavista", 5)],
    "Autobuses del Norte": [("Instituto del Petróleo", 5), ("La Raza", 5)],
    "Misterios": [("La Raza", 5), ("Valle Gómez", 5)],
    "Valle Gómez": [("Misterios", 5), ("Consulado", 5)],
    "Eduardo Molina": [("Consulado", 5), ("Aragón", 5)],
    "Aragón": [("Oceanía", 5), ("Eduardo Molina", 5)],
    "Oceanía": [("Aragón", 5), ("Terminal Aérea", 5)],
    "Terminal Aérea": [("Oceanía", 5), ("Hangares", 5)],
    "Hangares": [("Terminal Aérea", 5), ("Pantitlán", 5)],

    "El Rosario": [("Tezozómoc", 5), ("Aquiles Serdán", 5)],
    "Tezozómoc": [("El Rosario", 5), ("UAM Azcapotzalco", 5)],
    "UAM Azcapotzalco": [("Tezozómoc", 5), ("Ferrería Arena Ciudad de México", 5)],
    "Ferrería Arena Ciudad de México": [("UAM Azcapotzalco", 5), ("Norte 45", 5)],
    "Norte 45": [("Ferrería Arena Ciudad de México", 5), ("Vallejo", 5)],
    "Vallejo": [("Norte 45", 5), ("Instituto del Petróleo", 5)],
    "Lindavista": [("Instituto del Petróleo", 5), ("Deportivo 18 de Marzo", 5)],
    "La Villa": [("Deportivo 18 de Marzo", 5), ("Martín Carrera", 5)],

    "Aquiles Serdán": [("El Rosario", 5), ("Camarones", 5)],
    "Camarones": [("Aquiles Serdán", 5), ("Refinería", 5)],
    "Refinería": [("Camarones", 5), ("Tacuba", 5)],
    "San Joaquín": [("Tacuba", 5), ("Polanco", 5)],
    "Polanco": [("San Joaquín", 5), ("Auditorio", 5)],
    "Auditorio": [("Polanco", 5), ("Constituyentes", 5)],
    "Constituyentes": [("Auditorio", 5), ("Tacubaya", 5)],
    "San Pedro de los Pinos": [("Tacubaya", 5), ("San Antonio", 5)],
    "San Antonio": [("San Pedro de los Pinos", 5), ("Mixcoac", 5)],
    "Mixcoac": [("San Antonio", 5), ("Barranca del Muerto", 5), ("Insurgentes Sur", 5)],
    "Barranca del Muerto": [("Mixcoac", 5)],

    "Garibaldi": [("Guerrero", 5), ("Lagunilla", 5), ("Bellas Artes", 5)],
    "San Juan de Letrán": [("Bellas Artes", 5), ("Salto del Agua", 5)],
    "Doctores": [("Salto del Agua", 5), ("Obrera", 5)],
    "Obrera": [("Doctores", 5), ("Chabacano", 5)],
    "La Viga": [("Chabacano", 5), ("Santa Anita", 5)],
    "Coyuya": [("Santa Anita", 5), ("Iztacalco", 5)],
    "Iztacalco": [("Apatlaco", 5), ("Coyuya", 5)],
    "Apatlaco": [("Iztacalco", 5), ("Aculco", 5)],
    "Aculco": [("Apatlaco", 5), ("Escuadrón 201", 5)],
    "Escuadrón 201": [("Aculco", 5), ("Atlalilco", 5)],
    "Atlalilco": [("Escuadrón 201", 5), ("Iztapalapa", 5), ("Mexicaltzingo", 5), ("Culhuacán", 5)],
    "Iztapalapa": [("Atlalilco", 5), ("Cerro de la Estrella", 5)],
    "Cerro de la Estrella": [("Iztapalapa", 5), ("UAM I", 5)],
    "UAM I": [("Cerro de la Estrella", 5), ("Constitución de 1917", 5)],
    "Constitución de 1917": [("UAM I", 5)],

    "Patriotismo": [("Tacubaya", 5), ("Chilpancingo", 5)],
    "Chilpancingo": [("Patriotismo", 5), ("Centro Médico", 5)],
    "Lázaro Cárdenas": [("Centro Médico", 5), ("Chabacano", 5)],
    "Mixiuhca": [("Jamaica", 5), ("Velódromo", 5)],
    "Velódromo": [("Mixiuhca", 5), ("Ciudad Deportiva", 5)],
    "Ciudad Deportiva": [("Velódromo", 5), ("Puebla", 5)],
    "Puebla": [("Ciudad Deportiva", 5), ("Pantitlán", 5)],

    "Tláhuac": [("Tlaltenco", 5)],
    "Tlaltenco": [("Tláhuac", 5), ("Zapotitlán", 5)],
    "Zapotitlán": [("Tlaltenco", 5), ("Nopalera", 5)],
    "Nopalera": [("Zapotitlán", 5), ("Olivos", 5)],
    "Olivos": [("Nopalera", 5), ("Tezonco", 5)],
    "Tezonco": [("Olivos", 5), ("Periférico Oriente", 5)],
    "Periférico Oriente": [("Tezonco", 5), ("Calle 11", 5)],
    "Calle 11": [("Periférico Oriente", 5), ("Lomas Estrella", 5)],
    "Lomas Estrella": [("Calle 11", 5), ("San Andrés Tomatlán", 5)],
    "San Andrés Tomatlán": [("Lomas Estrella", 5), ("Culhuacán", 5)],
    "Culhuacán": [("San Andrés Tomatlán", 5), ("Atlalilco", 5)],
    "Mexicaltzingo": [("Atlalilco", 5), ("Ermita", 5)],
    "Eje Central": [("Ermita", 5), ("Parque de los Venados", 5)],
    "Parque de los Venados": [("Eje Central", 5), ("Zapata", 5)],
    "Hospital 20 de Noviembre": [("Zapata", 5), ("Insurgentes Sur", 5)],
    "Insurgentes Sur": [("Hospital 20 de Noviembre", 5), ("Mixcoac", 5)],

    "Agrícola Oriental": [("Pantitlán", 5), ("Canal de San Juan", 5)],
    "Canal de San Juan": [("Agrícola Oriental", 5), ("Tepalcates", 5)],
    "Tepalcates": [("Canal de San Juan", 5), ("Guelatao", 5)],
    "Guelatao": [("Tepalcates", 5), ("Peñón Viejo", 5)],
    "Peñón Viejo": [("Guelatao", 5), ("Acatitla", 5)],
    "Acatitla": [("Peñón Viejo", 5), ("Santa Marta", 5)],
    "Santa Marta": [("Acatitla", 5), ("Los Reyes", 5)],
    "Los Reyes": [("Santa Marta", 5), ("La Paz", 5)],
    "La Paz": [("Los Reyes", 5)],

    "Buenavista": [("Guerrero", 5)],
    "Lagunilla": [("Garibaldi", 5), ("Tepito", 5)],
    "Tepito": [("Lagunilla", 5), ("Morelos", 5)],
    "Flores Magón": [("San Lázaro", 5), ("Romero Rubio", 5)],
    "Romero Rubio": [("Flores Magón", 5), ("Oceanía", 5)],
    "Deportivo Oceanía": [("Oceanía", 5), ("Bosque de Aragón", 5)],
    "Bosque de Aragón": [("Deportivo Oceanía", 5), ("Villa de Aragón", 5)],
    "Villa de Aragón": [("Bosque de Aragón", 5), ("Nezahualcóyotl", 5)],
    "Nezahualcóyotl": [("Villa de Aragón", 5), ("Impulsora", 5)],
    "Impulsora": [("Nezahualcóyotl", 5), ("Río de los Remedios", 5)],
    "Río de los Remedios": [("Impulsora", 5), ("Múzquiz", 5)],
    "Múzquiz": [("Río de los Remedios", 5), ("Ecatepec", 5)],
    "Ecatepec": [("Múzquiz", 5), ("Olímpica", 5)],
    "Olímpica": [("Ecatepec", 5), ("Plaza Aragón", 5)],
    "Plaza Aragón": [("Olímpica", 5), ("Ciudad Azteca", 5)],
    "Ciudad Azteca": [("Plaza Aragón", 5)],
    }

    conexiones = ["Tacubaya", "Balderas", "Salto del Agua", "Pino Suárez", "Candelaria", "San Lázaro", "Pantitlán", "Tacuba", "Hidalgo", "Bellas Artes", "Chabacano", "Ermita", "Deportivo 18 de Marzo", "La Raza", "Centro Médico", "Zapata", "Consulado", "Jamaica", "Instituto del Petróleo", "Mixcoac", "Atlalilco", "Garibaldi"]

    l1 = ["Observatorio","Juanacatlan","Chapultepec","Sevilla","Insurgentes","Cuauhtemoc",
        "IsabelLaCatolica","Merced","Moctezuma","Balbuena","BlvdPuertoAereo","GomezFarias",
        "Zaragoza"]

    l2 = ["CuatroCaminos","Panteones","Cuitlahuac","Popotla","ColegioMilitar","Normal","SanCosme",
        "Revolucion","Allende","Zocalo","SanAntonioAbad","Viaducto","Xola","VilladeCortes",
        "Nativitas","Portales","GeneralAnaya","Tasqueña"]

    l3 = ["IndiosVerdes","Potrero","Tlatelolco","Guerrero","Juarez","NinosHeroes","HospitalGeneral",
        "Etiopia","Eugenia","DivisiondelNorte","Coyoacan","Viveros","MiguelangeldeQuevedo",
        "Copilco","Universidad"]

    l4 = ["MartinCarrera","Talisman","Bondojito","CanaldelNorte","Morelos",
        "FrayServando","SantaAnita"]

    l5 = ["Politecnico","AutobusesdelNorte","Misterios","ValleGomez","EduardoMolina",
        "Aragon","Oceania","TerminalAerea","Hangares"]

    l6 = ["ElRosario","Tezozomoc","UAM_Azcapotzalco","Ferreria_ArenaCiudaddeMexico",
        "Norte45","Vallejo","Lindavista","LaVilla"]

    l7 = ["AquilesSerdan","Camarones","Refineria","SanJoaquin","Polanco","Auditorio",
        "Constituyentes","SanPedrodelosPinos","SanAntonio","BarrancadelMuerto"]

    l8 = ["SanJuandeLetran","Doctores","Obrera","LaViga","Coyuya","Iztacalco","Apatlaco",
        "Aculco","Escuadron201","Iztapalapa","CerrodelaEstrella","UAM_I","Constitucionde1917"]

    l9 = ["Patriotismo","Chilpancingo","LazaroCardenas","Mixiuhca",
        "Velodromo","CiudadDeportiva","Puebla"]

    l12 = ["Tlahuac","Tlaltenco","Zapotitlan","Nopalera","Olivos","Tezonco","PerifericoOriente",
        "Calle11","LomasEstrella","SanAndresTomatlan","Culhuacan","Mexicaltzingo",
        "EjeCentral","ParquedelosVenados","Hospital20deNoviembre","InsurgentesSur"]

    lA = ["AgricolaOriental","CanaldeSanJuan","Tepalcates","Guelatao","PenonViejo",
        "Acatitla","SantaMarta","LosReyes","LaPaz"]

    lB = ["Buenavista","Lagunilla","Tepito","FloresMagon","RomeroRubio","DeportivoOceania",
        "BosquedeAragon","VilladeAragon","Nezahualcoyotl","Impulsora","RiodelosRemedios",
        "Muzquiz","Ecatepec","Olimpica","PlazaAragon","CiudadAzteca"]

    

    # Añadir estaciones y conexiones al grafo con pesos específicos
    for estacion, conexiones in estaciones.items():
        for conexion, tiempo in conexiones:
            G.add_edge(estacion, conexion, weight=tiempo)

    """ # Asignar colores a los nodos según la línea
    color_map = []
    for node in G:
        if node in conexiones:
            color_map.append("#FFFFFF")
        elif node in l1:
            color_map.append("#E9468F")
        elif node in l2:
            color_map.append("#00599F")
        elif node in l3:
            color_map.append("#B69C13")
        elif node in l4:
            color_map.append("#6CBCB1")
        elif node in l5:
            color_map.append("#FDD200")
        elif node in l6:
            color_map.append("#DA1715")
        elif node in l7:
            color_map.append("#E97009")
        elif node in l8:
            color_map.append("#008E3D")
        elif node in l9:
            color_map.append("#5B352E")
        elif node in l12:
            color_map.append("#C49355")
        elif node in lA:
            color_map.append("#9E1A81")
        elif node in lB:
            color_map.append("#BBB9B8")
        else:
            color_map.append("#000000")  # Color por defecto si no está en ningún grupo

    # Dibujar el grafo con los colores asignados
    pos = nx.spring_layout(G)  # Disposición del grafo
    plt.figure(figsize=(8, 6))
    nx.draw(
        G, pos, node_color=color_map, with_labels=True, node_size=60, edge_color="lightgray", font_size=5
    )
    plt.title("Grafo del Metro de la CDMX")
    plt.show() """
    
    return G