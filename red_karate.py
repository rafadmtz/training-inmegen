#Misión uno: hacer una visualización de la red de karate de Zachary con los 
#nodos coloreados por su comunidad de Louvain, y con el tamaño del nodo representando el grado, y el 
#grueso de los enlaces representando el edge betweenness.



import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms import community



# Fijar semilla
seed=2 # Para las comunidades de Louvain
np.random.seed(seed) # Para graficar



# Cargar la red de karate de Zachary
G = nx.karate_club_graph()



# Detectar comunidades usando el algoritmo de Louvain
comunidades = community.louvain_communities(G, seed= seed)





# Crear un diccionario para asignar a cada nodo su comunidad
comunidad_nodo = {}



# Asignar a cada nodo su comunidad en el diccionario

for i in range(len(comunidades)):
    for node in comunidades[i]:
        comunidad_nodo[node] = i
        

#Colores para cada comunidad
colores_comunidades = ["red", "blue", "green", "purple"]



#Listas para almacenar el tamaño de los nodos y sus colores  
size=[(G.degree[node])*100 for node in G.nodes()]
colores = [colores_comunidades[comunidad_nodo[node]] for node in G.nodes()]
   
        

# Calcular edge betweenness
edge_bet = nx.edge_betweenness_centrality(G)


#Lista para almacenar el grosor de las aristas basado en el edge betweenness
aristas=[(edge_bet[edge])*50 for edge in G.edges()]



#Visuazlizar la red
nx.draw(G, node_color=colores, node_size=size, with_labels=True, width=aristas)




#Agregar leyenda para las comunidades
for i in range(len(comunidades)):
    plt.scatter([], [], c=colores_comunidades[i], label=f"Comunidad {i+1}")

plt.legend()


plt.show()