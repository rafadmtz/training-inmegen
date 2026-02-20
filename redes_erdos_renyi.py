# A ver mis punks, una misión fácil para irnos de fin de semana;

# 100 redes erdos renyi, reproducibles, y una tabla con el grado mínimo, medio, 
# y máximo de cada una de ellas. Avast!



import networkx as nx
import numpy as np
import pandas as pd


#Lista para guardar los datos de la tabla
tabla=[]

#numero de nodos de la red   
num_nodos=100

#probabilidad de conexion para las redes erdos renyi
probabilidad_conexion=0.05




#For para realizar los calculos para las 100 redes diferentes
for i in range(100):


    
    G=nx.erdos_renyi_graph(n=num_nodos, p=probabilidad_conexion, seed=i)


    #Array de numpy con los grados de cada nodo de la red     
    grados=np.array([(G.degree[node]) for node in G.nodes()])



    #Obtener media de los grados, asi como el maximo y minimo
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


    
#Crea un archivo csv con la tabla
df.to_csv("erdos_renyi_tabla.csv", index=False)


