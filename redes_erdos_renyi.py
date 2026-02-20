# A ver mis punks, una misión fácil para irnos de fin de semana;

# 100 redes erdos renyi, reproducibles, y una tabla con el grado mínimo, medio, 
# y máximo de cada una de ellas. Avast!






from platform import node

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


i=np.random.randint(0,1000)
G=nx.erdos_renyi_graph(n=100, p=0.05, seed=i)




#Lista para guardar los datos de la tabla
tabla=[]   
num_nodos=100
probabilidad_conexion=0.05

for i in range(100):
    
    G=nx.erdos_renyi_graph(n=num_nodos, p=probabilidad_conexion, seed=i)
     
    grados=np.array([(G.degree[node]) for node in G.nodes()])
    
    grado_max=np.max(grados)
    grado_min=np.min(grados)
    
    media=np.mean(grados)
    
    
    #Actualizar la lista tabla con los datos
    tabla.append([
        i,
        grado_max,
        grado_min,
        media
    ])
    


#Tabla con pandas  
df = pd.DataFrame(
    tabla,
    columns=[
        "Red",
        "Grado_maximo",
        "Grado_minimo",
        "Media"
    ]
)

print(df)
    

df.to_csv("erdos_renyi_tabla.csv", index=False)


