import osmnx as ox
import matplotlib.pyplot as plt

# Defina os locais de interesse
parnamirim = "Parnamirim, RN"
natal_base_aerea = "Base Aérea de Natal, RN"

# Obtenha o grafo da rede viária para Parnamirim
G_parnamirim = ox.graph_from_place(parnamirim, network_type='drive')

# Obtenha geometrias de construções na Base Aérea de Natal
base_aerea = ox.geometries_from_place(natal_base_aerea, tags={'building': True})

# Projete o grafo e as geometrias
G_parnamirim_projected = ox.project_graph(G_parnamirim)
base_aerea_projected = ox.project_gdf(base_aerea)

# Plote o mapa de nós da cidade de Parnamirim
fig, ax = ox.plot_graph(G_parnamirim_projected, bgcolor='k', node_size=5, node_color='#999999', node_edgecolor='none', node_zorder=2,
                        edge_color='#555555', edge_linewidth=1.5, edge_alpha=1)

# Plote a Base Aérea de Natal em destaque
base_aerea_projected.plot(ax=ax, color='red', alpha=0.7)

# Adicione rótulo para identificar a Base Aérea
ax.annotate("Base Aérea de Natal", (base_aerea_projected.geometry.centroid.x.values[0], base_aerea_projected.geometry.centroid.y.values[0]),
            fontsize=8, ha='center', va='center', color='white')

plt.show()
