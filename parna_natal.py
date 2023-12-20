import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

# Defina o local como uma lista de cidades ['Parnamirim, RN', 'Natal, RN']
places = ['Nova Parnamirim,Parnamirim, RN', 'Neópolis,Natal, RN']

# Obtenha o grafo da rede viária para ambas as cidades
G = ox.graph_from_place(places, network_type='drive')

# Projete o grafo
G_projected = ox.project_graph(G)

# Calcule a centralidade de proximidade para as arestas
edge_centrality = nx.closeness_centrality(nx.line_graph(G_projected))

# Lista de valores de centralidade para as arestas do grafo original
ev = [edge_centrality[edge + (0,)] for edge in G_projected.edges()]

# Crie uma escala de cores convertida para uma lista de cores para as arestas do grafo
norm = colors.Normalize(vmin=min(ev)*0.8, vmax=max(ev))
cmap = cm.ScalarMappable(norm=norm, cmap=cm.inferno)
ec = [cmap.to_rgba(cl) for cl in ev]

# Plote o grafo com o mapa de calor baseado na centralidade das arestas
fig, ax = ox.plot_graph(G_projected, bgcolor='k', node_size=0, edge_color=ec, edge_linewidth=1.5, edge_alpha=1)

# Adicione rótulos para identificar as cidades
for place in places:
    gdf = ox.geocode_to_gdf([place])
    ax.annotate(place.split(',')[0], (gdf.geometry.centroid.x.values[0], gdf.geometry.centroid.y.values[0]),
                fontsize=8, ha='center', va='center', color='white')

plt.show()
