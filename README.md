# Mobility Analysis in Parnamirim, RN

## Introduction

Welcome to the Mobility Analysis project in the metropolitan region of Natal, Rio Grande do Norte. In an effort to better understand the mobility challenges in the state capital, we decided to explore and analyze the road infrastructure and urban connectivity with Parnamirim and São Gonçalo. The accelerated economic and population growth of cities highlights the importance of addressing mobility-related issues effectively.

## Team

- PEDRO VITOR BEZERRA CLEMENTE

- PEDRO HENRIQUE BEZERRA FERNANDES

- JOAO PEDRO SILVA ALVES

## Goal

This project uses the NetworkX and OSMnx libraries to perform a comprehensive analysis of the street network in the metropolitan region of Natal. We seek to identify and understand the mobility challenges faced by the city, evaluating the efficiency of road infrastructure, congestion areas and proposing solutions to improve urban mobility.

## Methodology

1. **Data Collection**: Using the OSMnx library, we extracted detailed data from Parnamirim's street network from OpenStreetMap.

2. **Urban Graph Visualization**: Using NetworkX and OSMnx, we generate a representative graph of the city's street network, providing a clear visual view of the road infrastructure.

3. **Centrality Metrics Analysis**: We calculate centrality metrics, including degree and proximity centrality, to identify critical areas and important nodes in the urban network.

4. **Identification of Mobility Issues**: Based on graph analysis, we identify areas of congestion, lack of connectivity and other mobility challenges.

5. **Proposed Solutions**: We develop potential solutions for the problems identified, aiming to improve the efficiency of mobility in the region that connects the metropolitan cities with Natal.

# Data collect

This project involves collecting geospatial data and creating maps for analysis of the city of Parnamirim, RN. Next, the steps for extracting the initial map, the node-based heatmap and the edge-based heatmap are described.

## 1. Extraction of the Initial Map

### Description:
The `osmnx` library is used to extract the initial map of the city of Parnamirim, RN, and the Igapó Bridge (Cars and bicycles) from OpenStreetMap (OSM). This library facilitates obtaining data from urban networks and allows efficient manipulation of this data for later analysis.

### Code:

```python
import osmnx as ox

# Define the location (place_name) as Parnamirim, RN, and the network type as road (network_type='drive')
place_name = "Parnamirim, RN"
G = ox.graph_from_place(place_name, network_type='drive')
```
![Map](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/2a76b922acd33869e3790c3557e28dc5427dd2cb/graph_original_Parnamirim.png)




## 2. Node-Based Heatmap Extraction

### Description:
In this step, we created a heat map based on the centrality of the nodes in the Parnamirim and Ponte de Igapó road network. The centrality of a node indicates its importance in the network and can be calculated in several ways, such as degree centrality, proximity, among others.

### Code:

```python
import networkx as nx
import matplotlib.pyplot as plt

# Calculate degree centrality for each node
node_centrality = nx.degree_centrality(G)

# Create a heatmap based on node centrality
plt.figure(figsize=(10, 10))
ox.plot_graph(G, bgcolor='k', node_size=[v * 1000 for v in node_centrality.values()], node_color='r', node_edgecolor='none', node_zorder=2)
plt.title("Node-Based Heatmap - Degree Centrality")
plt.show()
```
![Map](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/2a76b922acd33869e3790c3557e28dc5427dd2cb/graph_nodes_Parnamirim.png)


## 3. Edge-Based Heatmap Extraction

### Description:
In this step, we generate a heat map based on the centrality of the edges of the graph. Edge centrality can be calculated considering proximity centrality or other relevant metrics.

### Code:

```python
# Calculate proximity centrality for each edge
edge_centrality = nx.closeness_centrality(nx.line_graph(G))

# Create a heatmap based on edge centrality
plt.figure(figsize=(10, 10))
ox.plot_graph(G, bgcolor='k', node_size=0, edge_color=edge_centrality.values(), edge_cmap=plt.cm.inferno, edge_linewidth=2, edge_alpha=0.7)
plt.title("Edge-Based Heatmap - Proximity Centrality")
plt.show()
```
![Map](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/98dd1d7b89faf8fda44259ab08670537cebaf28e/graph_edges_Parnamirim.png)



These steps represent the initial data collection and generation of maps that will be used for more in-depth analysis in the project. The visualizations provide insights into the relative importance of nodes and edges in Parnamirim's road network.



# Problems of Parnamirim/Natal

The city of Parnamirim, located in the state of Rio Grande do Norte, faces significant challenges related to urban mobility, aggravated by its strategic position in relation to the capital, Natal. The problem involves several factors that directly impact the flow of traffic and the quality of life of citizens.

## Constant Growth and Connection with Natal

Parnamirim experiences continuous population and economic growth. Its proximity to Natal results in a complex road network connecting the two cities through several avenues along the border. This intense connection creates additional challenges for urban mobility, as the two city halls need to collaborate and coordinate efforts to solve traffic and infrastructure problems together.

## Natal Air Base as an Additional Challenge

Another critical point is the presence of the Natal Air Base, located in the heart of Parnamirim, occupying an extensive area in the middle of the city. This situation presents a substantial challenge to urban mobility, as the city grew around the military base. The need to reconcile daily traffic flow with military base operations demands a careful and collaborative approach between local authorities and the military. Furthermore, the base is located in the middle of the city, which makes it difficult to build a road between important regions that are bordered by the base. If we pay attention to the map of the city of Parnamirim shown previously, we see the existence of a large void in the middle of the city. city, and in its surroundings a road with a large number of connections, as the heat map points out, this region is precisely the location of the Natal Air Base"

# Natal and Parnamirim

## Road Connections and Mobility Challenges

Natal, as a large metropolis, is part of a metropolitan region made up of several cities, increasing the complexity of urban mobility problems in the area. Connectivity between Natal and Parnamirim, two significant cities in this region, is vital, but faces notable challenges. Here we plotted the entire metropolitan region of Natal, using the osnmx library.
```python
# Geocode and design the cities
places = ox.geocode_to_gdf(['Parnamirim, RN', 'Natal, RN','Macaiba, RN','são gonçalo do amarante, RN'])
places = ox.project_gdf(places)

# Different colors for Parnamirim and Natal
colors = ['blue', 'green','red','purple']

# Labels for each city
labels = ['Parnamirim', 'Natal','Macaiba','são gonçalo do amarante']

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
for i, (color, label) in enumerate(zip(colors, labels)):
     places.iloc[i:i+1].plot(ax=ax, color=color, label=label)

# Add labels to city center points
for i, txt in enumerate(labels):
     ax.annotate(txt, (places['geometry'].iloc[i].centroid.x, places['geometry'].iloc[i].centroid.y),
                 fontsize=8, ha='center', va='center')

# Additional settings
ax.axis('off')
plt.legend()
plt.show()

```


![Natal Região Metropolitana](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/7fad9f82841a64365d75fface029da161582a3c8/Natal_regi%C3%A3o_metropolitana.png)

Specifically, the connection between the neighborhoods of Nova Parnamirim and Neópolis stands out as an area with critical mobility problems. The high population density in this region forms the border between the two cities, resulting in frequent traffic jams. A more in-depth analysis of these two neighborhoods, using the code below, reveals the importance of Avenida Ayrton Senna. This avenue, due to its large number of connections between the two neighborhoods, faces a high volume of vehicles daily.

```python
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Define the location as a list of neighborhoods ['Nova Parnamirim, RN', 'Neópolis, RN']
neighborhoods = ['Nova Parnamirim, RN', 'Neópolis, RN']

# Get the road network graph for the two neighborhoods
G_neighborhoods = ox.graph_from_place(neighborhoods, network_type='drive')

# Design the graph
G_bairros_projected = ox.project_graph(G_bairros)

# Plot the graph
fig, ax = ox.plot_graph(G_bairros_projected, bgcolor='k', node_size=5, node_color='#999999', node_edgecolor='none', node_zorder=2,
                         edge_color='#555555', edge_linewidth=1.5, edge_alpha=1)

# Add labels to identify neighborhoods
for neighborhood in neighborhoods:
     gdf = ox.geocode_to_gdf([neighborhood])
     ax.annotate(neighborhood.split(',')[0], (gdf.geometry.centroid.x.values[0], gdf.geometry.centroid.y.values[0]),
                 fontsize=8, ha='center', va='center', color='white')

plt.show()
```

The visualization highlights the relevance of Avenida Ayrton Senna in the interconnection between Nova Parnamirim and Neópolis, highlighting the need for specific strategies to manage and improve mobility in this critical area, this can only be achieved through cooperation between both city halls and the State government , to improve the infrastructure and planning of the Avenue and its connections.
![Nova Parnamirim and Neópolis](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/7fad9f82841a64365d75fface029da161582a3c8/Nova_parnamirim_Ne%C3%B3polis.png)


# Problems of Natal/North Zone/São Gonçalo do Amarante

The problem of the North Zone of Natal emerges as one of the main urban mobility challenges in the State of Rio Grande do Norte. The region faces critical bottlenecks on the roads, notably on the two bridges that cross the Potengi River. This phenomenon results in extensive traffic jams, particularly during peak hours, marked by busy trips to work in the morning and return in the late afternoon.

The situation is worsened by the significant flow of workers and students heading to the central and southern areas of the city. These areas, being commercial centers and concentrating a large part of the city's jobs, become frequent destinations for the population of the North Zone. The intense movement at these times creates not only congestion, but also significant challenges to the efficiency of public transport and the quality of life of residents.

The need to address this problem requires innovative approaches and strategic solutions that aim to improve road infrastructure, reinforce public transport services and promote sustainable travel alternatives. The search for more efficient urban mobility in the North Zone of Natal becomes essential not only for the convenience of citizens, but also for the sustainable development and economic vitality of the region.

![Map](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/main/PonteVelha.png)

## Study on regions

It is feasible to incorporate a visual representation of the importance of bridges and critical bottlenecks on the roads into the graph. These are locations frequently chosen by drivers to cross, and such analysis provides valuable insights for the study of the expansion of these crossings. The ability to intuitively view the map and identify specific hot spots contributes significantly to strategic planning aimed at improving urban mobility.

These studies not only highlight bottlenecks on bridges and crossing routes, but also offer a solid basis for preparing initiatives that aim to optimize the efficiency of the road system. By understanding traffic dynamics and critical congestion areas, it becomes possible to formulate informed proposals on the expansion or creation of new crossings, thus contributing to the fluidity of traffic and the quality of life of citizens.

Visualizing the heat zone on the map provides a clear perspective of the most affected areas, allowing a proactive approach to implementing improvements. This process proves to be crucial for the sustainable development of urban mobility in the North Zone of Natal, providing more effective solutions adapted to the specific needs of the community.

![Map](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/main/graph_edges_PonteVelha.png)
![Map](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/main/graph_edges_PonteVelhaBike.png)

# Difference in graphics between cars and bicycles (bike - cars)

![Map](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/main/PonteVelha(bike-carros).png)

## Conclusion

The mobility analysis project in Parnamirim, Rio Grande do Norte, provided a detailed view of the challenges faced by the city, considering its accelerated growth, connectivity with Natal and the presence of the Natal Air Base. Using tools such as the NetworkX and OSMnx libraries, we explored the road infrastructure and identified critical points, with the region between the Nova Parnamirim and Neópolis neighborhoods being a special focus due to recurring congestion problems.

During the analysis, Avenida Ayrton Senna emerged as a vital axis in the interconnection between the two cities, highlighting the need for specific strategies to manage and improve mobility in this area. The high population density and urban growth around Natal Air Base also presented unique challenges, requiring a collaborative approach between local authorities and the military.

We suggest several strategies to improve mobility in Parnamirim, including improvements to Avenida Ayrton Senna, traffic flow management, investment in public transport, modal integration, planned urban zoning and dialogue with the community. Cooperation between city halls, state government and active community participation is crucial to implementing these strategies effectively. We emphasize the importance of continuous monitoring to assess the effectiveness of interventions over time, ensuring adaptation to changes in traffic conditions.

For mobility challenges in the North Zone of Natal, it is crucial to adopt an integrated and innovative approach. The expansion and diversification of crossings, including the evaluation of new bridges, and the optimization of public transport are essential measures to alleviate congestion on bridges over the Potengi River. Encouraging the use of sustainable means, such as cycle paths, and promoting work flexibility policies will also contribute to reducing traffic during peak hours. The implementation of smart technological solutions, educational campaigns and public-private partnerships will strengthen the efficiency of the road system, providing more sustainable urban mobility and improving the quality of life in the region.


# Video explaining the work developed

https://drive.google.com/file/d/10Cm1iMwfl7Z5SViadmUY2YnR8Bcd70Uq/view?usp=sharing

## License

This project is distributed under the [MIT] license (LICENSE). Feel free to use and adapt as needed.

Explore, analyze and contribute to improving mobility in Parnamirim! 🚗🗺️
