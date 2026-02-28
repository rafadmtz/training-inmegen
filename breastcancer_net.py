# A ver mis punks, misión para hoy: 

# Se bajan esta red: 
# https://github.com/guillermodeandajauregui/WorkshopAdvancedBioinformatics2021/blob/main/data/BasalBreastCancer.graphml

# le sacan comunidades (louvain)

# Y para cada comunidad, van a hacer un enriquecimiento 
# (over enrichment analysis, o sea, con la prueba hipergeométrica) para todas las funciones (molecular functions) 
# reportadas en gene ontology.  Para humanos claramente. 

# Have fun!


import networkx as nx
import community as community_louvain
import gseapy as gp
from collections import defaultdict
from networkx.algorithms import community
import numpy as np
import pandas as pd

seed=2 # Para las comunidades de Louvain
np.random.seed(seed)




#Cargar red
G = nx.read_graphml("BasalBreastCancer.graphml")




#Comunidades Louvain
comunidades = community.louvain_communities(G, seed=seed)





#Agrupar genes por comunidad usando su atributo de 'name'
comunidades_genes = defaultdict(list)
for comunidad, nodos in enumerate(comunidades):
    for node in nodos:
        gen_name = G.nodes[node].get('name', node)
        comunidades_genes[comunidad].append(gen_name)




#Lista de todos los genes para usar como background en el enriquecimiento
todos_los_genes = [G.nodes[n].get('name', n) for n in G.nodes()]



#Dataframe para guardar resultados
df=[]




#Diccionario para guardar resultados por comunidad
resultados = {}

#Enriquecimiento por comunidad
for comm_id, genes in comunidades_genes.items():
        enr = gp.enrichr(
            gene_list = genes,
            gene_sets = "GO_Molecular_Function_2023",
            organism  = "human",
            cutoff    = 0.05,
            background= todos_los_genes
        )
        resultados[comm_id] = enr.results
        
        #Para guardar resultados en un dataframe general, agregando una columna con la comunidad
        df.append(enr.results.assign(Comunidad=comm_id))





#Concatenar resultados de todas las comunidades en un solo dataframe,
# ordenarlo por p-valor ajustado, y guardarlo en un csv
todos_resultados = pd.concat(df, ignore_index=True)
todos_resultados = todos_resultados.sort_values("Adjusted P-value")
todos_resultados.to_csv("resultados_enrichment.csv", index=False)
print("Guardado en resultados_enrichment.csv")





#Crear un diccionario con los términos significativos por comunidad, ordenados por p-valor ajustado
sig_por_comunidad = {}
for comm_id, sig_df in resultados.items():
    sig_por_comunidad[comm_id] = sig_df[sig_df["Adjusted P-value"] < 0.05].sort_values("Adjusted P-value")


#Imprimir los términos significativos por comunidad
for comm_id, sig_df in sig_por_comunidad.items():
    if len(sig_df) > 0:
        print(f"\n=== Comunidad {comm_id} ({len(sig_df)} terminos significativos) ===")
        print(sig_df[['Term', 'Adjusted P-value', 'Genes']].head(10).to_string())
    else:
        print(f"\nComunidad {comm_id}: sin terminos significativos")
