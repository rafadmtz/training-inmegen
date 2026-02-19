#Bueno, en lo que leo sus códigos, ahí les va la siguiente misión:

#Ustedes detectaron las comunidades, que se definen informalmente como grupos de 
#nodos más conectados entre ellos, que a nodos de otros tipos. Sin embargo, no todos los 
#nodos necesariamente van a estar igual de conectados a su comunidad, que a otros lados.

#La misión: generar una tabla donde cada renglón es un nodo, y tengamos una columna que nos diga el 
#número de vecinos de SU comunidad, y una columna con el número de vecinos que NO SON DE SU comunidad.
#Luego, otras dos columnas con eso como porcentaje de su número total de vecinos 
#(o sea, si tengo cinco vecinos, y 3 son de mi comunidad, tendría 60% de vecinos intracomunitarios y 
# 40% de vecinos intercomunitarios)

#Se entendió? Están listxs? Código en github y a darle!




import networkx as nx
import numpy as np
from networkx.algorithms import community
import random
import pandas as pd


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
    
    

 
 
#Lista para guardar los datos de la tabla
tabla=[]   





#Recorrer nodos para obtener el numero de vecinos
for node in G.nodes():
    
    
    #Vecinos del nodo
    vecinos=list(G.neighbors(node))
    
    
    total_x_nodo=len(vecinos)
    
    
    
    #Variables de conteo
    total_dentro=0
    total_fuera=0    




    #Contar vecinos dentro/fuera de la comunidad
    for vecino in vecinos:
        if (comunidad_nodo[vecino]==comunidad_nodo[node]):
            total_dentro+=1
        else:
            total_fuera+=1
    
    
    #Calculos porcentuales
    if total_x_nodo > 0:
        porcentaje_dentro = total_dentro / total_x_nodo * 100
        porcentaje_fuera = total_fuera / total_x_nodo * 100
    else:
        porcentaje_dentro = 0
        porcentaje_fuera = 0
    
    
    
    #Actualizar la lista tabla con los datos
    tabla.append([
        node,
        total_dentro,
        total_fuera,
        porcentaje_dentro,
        porcentaje_fuera
    ])
    


#Tabla con pandas  
df = pd.DataFrame(
    tabla,
    columns=[
        "nodo",
        "vecinos_intracomunitarios",
        "vecinos_intercomunitarios",
        "%_dentro",
        "%_fuera"
    ]
)

print(df)
    
    

