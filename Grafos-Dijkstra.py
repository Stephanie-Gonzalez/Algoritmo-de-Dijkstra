# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# numero de conexiones que desea
nf = int(input("Cuantas conexiones requieres: "))

conexiones = np.empty((nf, 3), dtype='object') # array con tipo de datos 'object'

# valores para cada elemento del array
for i in range(nf):
    conexiones[i][0] = input("Donde quieres que empiece?: ")
    conexiones[i][1] = input("Ingresa el Destino: ")
    conexiones[i][2] = input("Ingresa el Peso: ")


grafo = nx.Graph() # grafo no dirigido vacío

subgrafo = nx.DiGraph() # grafo dirigido para dijkstra

# nodos al grafo
stars = set([fila[0] for fila in conexiones])
destinos = set([fila[1] for fila in conexiones])
nodos = stars.union(destinos)
grafo.add_nodes_from(nodos)


# conexiones al grafo
for fila in conexiones:
    origen = fila[0]
    final = fila[1]
    load = int(fila[2])
    grafo.add_edge(origen, final, load=load)


totales = nx.get_edge_attributes(grafo, 'load') # peso de conexiones

# dibuja el grafo con pesos de las conexiones
nx.draw(grafo, pos=nx.spectral_layout(grafo), with_labels=True, node_size=500, font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(grafo, pos=nx.spectral_layout(grafo), edge_labels=totales)

# algoritmo de Dijkstra

origen = input("¿Cuál es el nodo origenal?")
final = input("¿Cuál es el nodo de destino?")
dij = list(nx.dijkstra_path(grafo, source=origen, target=final, weight='load'))
print(f"La ruta más corta desde {origen} hasta {final} es: {dij}")

# ruta más corta
subgrafo.add_nodes_from(dij)
pares_nodos = [(dij[i], dij[i+1]) for i in range(len(dij)-1)]
pos = {pares_nodos[i]:[1,i] for i in range(len(pares_nodos)-1)}


subgrafo.add_edges_from(pares_nodos)
fig, ax = plt.subplots(figsize=(8,2))
nx.draw(subgrafo, with_labels=True, ax=ax)