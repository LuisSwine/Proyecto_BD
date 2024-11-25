import networkx as nx
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

from grafo_metro import crear_grafo_metro
from grafo_mb import crear_grafo_metrobus

# Configurar los grafos de metro y metrobús
G_metro = crear_grafo_metro()
G_metrobús = crear_grafo_metrobus()

# Conexiones entre metro y metrobús (transbordos)
transbordos = [
    ("El Rosario", "El Rosario_MB", 5),
    ("Instituto del Petróleo", "Instituto del Petróleo_MB", 5),
    ("Deportivo 18 de Marzo", "Deportivo 18 de Marzo_MB", 5),
    ("Martín Carrera", "Martín Carrera_MB", 5),
    ("La Raza", "La Raza_MB", 5),
    ("Buenavista", "Buenavista_MB", 5),
    ("Indios Verdes", "Indios Verdes_MB", 5),
    ("Potrero", "Potrero_MB", 5),
    ("Guerrero", "Guerrero_MB", 5),
    ("Auditorio", "Auditorio_MB", 5),
    ("Tacubaya", "Tacubaya_MB", 5),
    ("Insurgentes", "Insurgentes_MB", 5),
    ("División del Norte", "División del Norte_MB", 5),
    ("Eugenia", "Eugenia_MB", 5),
    ("Centro Médico", "Centro Médico_MB", 5),
    ("Villa de Aragón", "Villa de Aragón_MB", 5),
    ("Pantitlán", "Pantitlán_MB", 5),
]

# Crear un grafo combinado para metro y metrobús
G_combined = nx.compose(G_metro, G_metrobús)
for t in transbordos:
    G_combined.add_edge(t[0], t[1], weight=t[2])
    G_combined.add_edge(t[1], t[0], weight=t[2])

# Cargar y preparar los datasets
file_path_metro = './datasets/afluenciastc_desglosado_10_2024.csv'
file_path_mb = './datasets/afluenciamb_desglosado_10_2024.csv'

afluencia_metro = pd.read_csv(file_path_metro)
afluencia_mb = pd.read_csv(file_path_mb)

# Asegurarse de que no haya valores nulos en la columna 'mes'
afluencia_metro = afluencia_metro.dropna(subset=['mes'])
afluencia_mb = afluencia_mb.dropna(subset=['mes'])

# Limpiar y preparar los datos
meses_mapeo = {
    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
    "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
    "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
}
afluencia_metro['mes'] = afluencia_metro['mes'].replace(meses_mapeo).astype(int)
afluencia_mb['mes'] = afluencia_mb['mes'].replace(meses_mapeo).astype(int)

# Función para entrenar modelos Prophet por estación
def entrenar_modelos_por_estacion(estaciones, fecha):
    modelos = {}
    for estacion in estaciones:
        datos_estacion = afluencia_metro[afluencia_metro['estacion'] == estacion]
        if not datos_estacion.empty:
            datos_estacion = datos_estacion.groupby('fecha').agg({'afluencia': 'sum'}).reset_index()
            datos_estacion = datos_estacion.rename(columns={'fecha': 'ds', 'afluencia': 'y'})
            datos_estacion['ds'] = pd.to_datetime(datos_estacion['ds'])

            modelo = Prophet()
            modelo.fit(datos_estacion)
            modelos[estacion] = modelo
    return modelos

# Función para predecir afluencia en estaciones específicas
def predecir_afluencia_por_estacion(modelos, fecha, estaciones):
    afluencias = {}
    for estacion in estaciones:
        if estacion in modelos:
            future = modelos[estacion].make_future_dataframe(periods=30)
            forecast = modelos[estacion].predict(future)
            prediccion = forecast[forecast['ds'] == fecha]
            if not prediccion.empty:
                afluencias[estacion] = prediccion[['yhat', 'yhat_lower', 'yhat_upper']].iloc[0]
            else:
                afluencias[estacion] = None
    return afluencias

# Función para predecir afluencia en líneas de metrobús
def predecir_afluencia_mb(fecha, linea):
    datos_linea = afluencia_mb[afluencia_mb['linea'] == linea]
    if not datos_linea.empty:
        datos_linea = datos_linea.groupby('fecha').agg({'afluencia': 'sum'}).reset_index()
        datos_linea = datos_linea.rename(columns={'fecha': 'ds', 'afluencia': 'y'})
        datos_linea['ds'] = pd.to_datetime(datos_linea['ds'])

        modelo = Prophet()
        modelo.fit(datos_linea)
        future = modelo.make_future_dataframe(periods=30)
        forecast = modelo.predict(future)
        prediccion = forecast[forecast['ds'] == fecha]
        if not prediccion.empty:
            return prediccion['yhat'].iloc[0]
    return None

# Programa principal para rutas
def encontrar_ruta_con_afluencia(origen, destino, fecha, umbral_afluencia):
    try:
        # Encontrar la ruta más corta en el metro
        ruta_metro = nx.shortest_path(G_metro, source=origen, target=destino, weight='weight')
        tiempo_metro = nx.shortest_path_length(G_metro, source=origen, target=destino, weight='weight')

        # Entrenar modelos para las estaciones de la ruta
        modelos_estaciones = entrenar_modelos_por_estacion(ruta_metro, fecha)

        # Predecir afluencia para las estaciones de la ruta
        afluencias = predecir_afluencia_por_estacion(modelos_estaciones, fecha, ruta_metro)
        afluencia_total = sum(afluencia['yhat'] for afluencia in afluencias.values() if afluencia is not None)

        if afluencia_total <= umbral_afluencia:
            return {
                "transporte": "metro",
                "ruta": ruta_metro,
                "tiempo": tiempo_metro,
                "afluencia_total": afluencia_total
            }
        else:
            # Calcular ruta alterna usando el metrobús
            ruta_mb = None
            tiempo_mb = float('inf')
            afluencia_mb_total = float('inf')

            for linea in afluencia_mb['linea'].unique():
                afluencia_linea = predecir_afluencia_mb(fecha, linea)
                if afluencia_linea and afluencia_linea < afluencia_mb_total:
                    # Simular búsqueda de ruta alterna (puede ser más complejo según las conexiones reales)
                    try:
                        ruta_mb_temp = nx.shortest_path(G_metrobús, source=f"{origen}_MB", target=f"{destino}_MB", weight='weight')
                        tiempo_mb_temp = nx.shortest_path_length(G_metrobús, source=f"{origen}_MB", target=f"{destino}_MB", weight='weight')
                        if tiempo_mb_temp < tiempo_mb:
                            ruta_mb = ruta_mb_temp
                            tiempo_mb = tiempo_mb_temp
                            afluencia_mb_total = afluencia_linea
                    except nx.NetworkXNoPath:
                        continue

            if ruta_mb:
                return {
                    "transporte": "metrobús",
                    "ruta": ruta_mb,
                    "tiempo": tiempo_mb,
                    "afluencia_total": afluencia_mb_total
                }
            else:
                return "No se encontró una ruta alterna disponible."

    except nx.NetworkXNoPath:
        return "No hay una ruta entre las estaciones seleccionadas."

# Ejemplo de uso
resultado = encontrar_ruta_con_afluencia("Tacubaya", "Pantitlán", "2024-02-03", umbral_afluencia=5000000)
print(resultado)
