import networkx as nx
from grafo_metro import crear_grafo_metro
from grafo_mb import crear_grafo_metrobus

def obtener_ruta(G, origen, destino):
    try:
        # Calcula la ruta más corta usando Dijkstra
        ruta = nx.shortest_path(G, source=origen, target=destino, weight='weight')
        tiempo = nx.shortest_path_length(G, source=origen, target=destino, weight='weight')
        return ruta, tiempo
    except nx.NetworkXNoPath:
        return None, None

def main():
    print("Bienvenido al sistema de rutas de CDMX")
    print("1. Metro")
    print("2. Metrobús")
    opcion = input("Seleccione el transporte (1 o 2): ")
    
    if opcion == "1":
        G = crear_grafo_metro()
        transporte = "Metro"
    elif opcion == "2":
        G = crear_grafo_metrobus()
        transporte = "Metrobús"
    else:
        print("Opción inválida. Intente nuevamente.")
        return

    origen = input(f"Ingrese la estación de origen ({transporte}): ")
    destino = input(f"Ingrese la estación de destino ({transporte}): ")
    
    ruta, tiempo = obtener_ruta(G, origen, destino)
    
    if ruta:
        print(f"Ruta más corta en el {transporte}: {' -> '.join(ruta)}")
        print(f"Tiempo estimado: {tiempo} minutos")
    else:
        print("No se encontró una ruta entre las estaciones especificadas.")

if __name__ == "__main__":
    main()
