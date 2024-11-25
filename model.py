import pandas as pd
from prophet import Prophet

# Cargar los datos del dataset consolidado
file_path = './datasets/afluenciastc_desglosado_10_2024.csv'
afluencia_metro = pd.read_csv(file_path)

# Paso 1: Preparar los datos para Prophet
# Limpiar datos y consolidar afluencia total por fecha
# Asegurarse de que no haya valores nulos en la columna 'mes'
afluencia_metro = afluencia_metro.dropna(subset=['mes'])

# Mapear el mes si está en formato texto
meses_mapeo = {
    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
    "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
    "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
}
afluencia_metro['mes'] = afluencia_metro['mes'].replace(meses_mapeo).astype(int)

# Consolidar afluencia total diaria
afluencia_prophet = afluencia_metro.groupby('fecha').agg({'afluencia': 'sum'}).reset_index()
afluencia_prophet = afluencia_prophet.rename(columns={'fecha': 'ds', 'afluencia': 'y'})

# Asegurarse de que la columna 'ds' sea de tipo datetime
afluencia_prophet['ds'] = pd.to_datetime(afluencia_prophet['ds'])

# Paso 2: Inicializar y entrenar el modelo Prophet
modelo_prophet = Prophet()
modelo_prophet.fit(afluencia_prophet)

# Paso 3: Crear fechas futuras a predecir
future = modelo_prophet.make_future_dataframe(periods=30)  # Predicción para los próximos 30 días

# Paso 4: Realizar las predicciones
forecast = modelo_prophet.predict(future)

# Mostrar los resultados de las predicciones
predicciones = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
print(predicciones)

# Paso 5: Visualizar las predicciones
modelo_prophet.plot(forecast)
modelo_prophet.plot_components(forecast)
