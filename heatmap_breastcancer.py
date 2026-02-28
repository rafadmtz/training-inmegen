
# Misión tranquila: Qué opinan de un heatmap, comunidades en el eje x, 
# funciones en el eje y, y el color del heatmap proporcional al -log(Pvalueajustado) ?

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('resultados_enrichment.csv')

# Filtrar solo terminos significativos
df = df[df['Adjusted P-value'] < 0.05]

# Calcular -log10 del p-value ajustado
df['-log10(p-value)'] = -np.log10(df['Adjusted P-value'])

# Pivotar: filas = Term, columnas = Comunidad
df_pivot = df.pivot_table(
    index='Term',
    columns='Comunidad',
    values='-log10(p-value)',
).fillna(0)
#Llenar con 0 los valores no significativos para que aparezcan en el heatmap como color claro




# Heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(
    df_pivot,
    cmap='YlGnBu',
    linewidths=0.3,
    linecolor='black',
    annot=False,
    cbar_kws={'label': '-log10(P-value ajustado)'}
)

plt.title('Enriquecimiento funcional por comunidad')
plt.xlabel('Comunidad')
plt.ylabel('Función biológica (Term)')
plt.yticks(fontsize=7)
plt.tight_layout()
plt.show()