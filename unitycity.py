import geopandas as gpd
import osmnx as ox
import matplotlib.pyplot as plt

# Geocode e projeta as cidades
places = ox.geocode_to_gdf(['Parnamirim, RN', 'Natal, RN','Macaiba, RN','são gonçalo do amarante, RN'])
places = ox.project_gdf(places)

# Cores diferentes para Parnamirim e Natal
colors = ['blue', 'green','red','purple']

# Rótulos para cada cidade
labels = ['Parnamirim', 'Natal','Macaiba','são gonçalo do amarante']

# Plotagem
fig, ax = plt.subplots(figsize=(10, 10))
for i, (color, label) in enumerate(zip(colors, labels)):
    places.iloc[i:i+1].plot(ax=ax, color=color, label=label)

# Adiciona rótulos aos pontos centrais das cidades
for i, txt in enumerate(labels):
    ax.annotate(txt, (places['geometry'].iloc[i].centroid.x, places['geometry'].iloc[i].centroid.y),
                fontsize=8, ha='center', va='center')

# Configurações adicionais
ax.axis('off')
plt.legend()
plt.show()
