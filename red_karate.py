#Misión uno: hacer una visualización de la red de karate de Zachary con los 
#nodos coloreados por su comunidad de Louvain, y con el tamaño del nodo representando el grado, y el 
#grueso de los enlaces representando el edge betweenness.



import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms import community
import random


# Fijar semilla
seed=2
random.seed(seed)
np.random.seed(seed)



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
size=[]
colores = []




for node in G.nodes():
    size.append((G.degree[node])*100)
 
    colores.append(colores_comunidades[comunidad_nodo[node]])
   
        


# Calcular edge betweenness
edge_bet = nx.edge_betweenness_centrality(G)


#Lista para almacenar el grosor de las aristas basado en el edge betweenness
aristas=[]


for edge in G.edges():
    aristas.append((edge_bet[edge])*50)



#Visuazlizar la red
nx.draw(G, node_color=colores, node_size=size, with_labels=True, width=aristas)




#Agregar leyenda para las comunidades
for i in range(len(comunidades)):
    plt.scatter([], [], c=colores_comunidades[i], label=f"Comunidad {i+1}")

plt.legend()


plt.show()