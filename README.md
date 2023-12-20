# Análise de Mobilidade em Parnamirim, RN

## Introdução

Bem-vindo ao projeto de Análise de Mobilidade na região metropolitana de Natal, Rio Grande do Norte. Em um esforço para compreender melhor os desafios de mobilidade na capital do Estado, decidimos explorar e analisar a infraestrutura viária e a conectividade urbana com Parnamirim e São Gonçalo. O crescimento econômico e populacional acelerado das cidades destaca a importância de abordar questões relacionadas à mobilidade de maneira eficaz.

## Equipe

- PEDRO VITOR BEZERRA CLEMENTE

- PEDRO HENRIQUE BEZERRA FERNANDES

- JOAO PEDRO SILVA ALVES

## Objetivo

Este projeto utiliza as bibliotecas NetworkX e OSMnx para realizar uma análise abrangente da rede de ruas da região metropolitana de Natal. Buscamos identificar e compreender os desafios de mobilidade enfrentados pela cidade, avaliando a eficiência da infraestrutura viária, áreas de congestionamento e propondo soluções para melhorar a mobilidade urbana.

## Metodologia

1. **Coleta de Dados**: Utilizando a biblioteca OSMnx, extraímos dados detalhados da rede de ruas de Parnamirim a partir do OpenStreetMap.

2. **Visualização do Grafo Urbano**: Usando NetworkX e OSMnx, geramos um gráfico representativo da rede de ruas da cidade, proporcionando uma visão visual clara da infraestrutura viária.

3. **Análise de Métricas de Centralidade**: Calculamos métricas de centralidade, incluindo centralidade de grau e proximidade, para identificar áreas críticas e nós importantes na rede urbana.

4. **Identificação de Problemas de Mobilidade**: Com base na análise do grafo, identificamos áreas de congestionamento, falta de conectividade e outros desafios de mobilidade.

5. **Proposta de Soluções**: Desenvolvemos soluções potenciais para os problemas identificados, visando melhorar a eficiência da mobilidade da região que interliga as cidades da metropóle com Natal.

# Coleta de Dados

Este projeto envolve a coleta de dados geoespaciais e a criação de mapas para análise da cidade de Parnamirim, RN. A seguir, são descritas as etapas de extração do mapa inicial, do mapa de calor baseado em nós e do mapa de calor baseado nas arestas.

## 1. Extração do Mapa Inicial

### Descrição:
A biblioteca `osmnx` é utilizada para extrair o mapa inicial da cidade de Parnamirim, RN, e da Ponte de Igapó(Carros e bicicleta) a partir do OpenStreetMap (OSM). Essa biblioteca facilita a obtenção de dados de redes urbanas e permite a manipulação eficiente desses dados para análise posterior.

### Código:

```python
import osmnx as ox

# Definir o local (place_name) como Parnamirim, RN, e o tipo de rede como viária (network_type='drive')
place_name = "Parnamirim, RN"
G = ox.graph_from_place(place_name, network_type='drive')
```
![Mapa](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/2a76b922acd33869e3790c3557e28dc5427dd2cb/graph_original_Parnamirim.png)




## 2. Extração do Mapa de Calor Baseado em Nós

### Descrição:
Nesta etapa, criamos um mapa de calor baseado na centralidade dos nós da rede viária de Parnamirim e da Ponte de Igapó. A centralidade de um nó indica sua importância na rede e pode ser calculada de várias maneiras, como centralidade de grau, proximidade, entre outras.

### Código:

```python
import networkx as nx
import matplotlib.pyplot as plt

# Calcular a centralidade de grau para cada nó
node_centrality = nx.degree_centrality(G)

# Criar um mapa de calor baseado na centralidade dos nós
plt.figure(figsize=(10, 10))
ox.plot_graph(G, bgcolor='k', node_size=[v * 1000 for v in node_centrality.values()], node_color='r', node_edgecolor='none', node_zorder=2)
plt.title("Mapa de Calor Baseado em Nós - Centralidade de Grau")
plt.show()
```
![Mapa](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/2a76b922acd33869e3790c3557e28dc5427dd2cb/graph_nodes_Parnamirim.png)


## 3. Extração do Mapa de Calor Baseado nas Arestas

### Descrição:
Nesta etapa, geramos um mapa de calor baseado na centralidade das arestas do grafo. A centralidade das arestas pode ser calculada considerando a centralidade de proximidade ou outras métricas relevantes.

### Código:

```python
# Calcular a centralidade de proximidade para cada aresta
edge_centrality = nx.closeness_centrality(nx.line_graph(G))

# Criar um mapa de calor baseado na centralidade das arestas
plt.figure(figsize=(10, 10))
ox.plot_graph(G, bgcolor='k', node_size=0, edge_color=edge_centrality.values(), edge_cmap=plt.cm.inferno, edge_linewidth=2, edge_alpha=0.7)
plt.title("Mapa de Calor Baseado em Arestas - Centralidade de Proximidade")
plt.show()
```
![Mapa](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/98dd1d7b89faf8fda44259ab08670537cebaf28e/graph_edges_Parnamirim.png)



Essas etapas representam a coleta inicial de dados e a geração de mapas que serão utilizados para análises mais aprofundadas no projeto. As visualizações fornecem insights sobre a importância relativa de nós e arestas na rede viária de Parnamirim.



# Problemática de Parnamirim/Natal

A cidade de Parnamirim, localizada no estado do Rio Grande do Norte, enfrenta desafios significativos relacionados à mobilidade urbana, agravados por sua posição estratégica em relação à capital, Natal. A problemática envolve diversos fatores que impactam diretamente a fluidez do tráfego e a qualidade de vida dos cidadãos.

## Crescimento Constante e Conexão com Natal

Parnamirim experimenta um crescimento populacional e econômico contínuo. Sua proximidade com Natal resulta em uma complexa rede viária interligando as duas cidades por meio de várias avenidas ao longo da fronteira. Essa conexão intensa cria desafios adicionais para a mobilidade urbana, uma vez que as duas prefeituras precisam colaborar e coordenar esforços para resolver os problemas de tráfego e infraestrutura em conjunto.

## Base Aérea de Natal como Desafio Adicional

Outro ponto crítico é a presença da Base Aérea de Natal, localizada no coração de Parnamirim, ocupando uma extensa área em meio à cidade. Essa situação apresenta um desafio substancial para a mobilidade urbana, pois a cidade cresceu em torno da base militar. A necessidade de conciliar o fluxo diário de tráfego com as operações da base militar demanda uma abordagem cuidadosa e colaborativa entre as autoridades locais e militares. Além disso a base se encontra em meio a cidade, o que dificulta a construção de uma estrada entre regiões importantes que são divisadas pela base, se prestarmos atenção no mapa da cidade de Parnamirim exibido anteriormente, verificamos a existencia de um grande vazio no meio da cidade, e em seu entorno uma via com uma quantidade acentuada de conexões, como o mapa de calor aponta, essa região é justamente a localização da Base Aérea de Natal"

# Natal e Parnamirim

## Conexões Viárias e Desafios de Mobilidade

Natal, como uma grande metrópole, é parte de uma região metropolitana composta por diversas cidades, ampliando a complexidade dos problemas de mobilidade urbana na área. A conectividade entre Natal e Parnamirim, duas cidades significativas nessa região, é vital, mas enfrenta desafios notáveis. Aqui fizemos um plot de toda a região metropolitana de Natal, usando a biblioteca osnmx.
```python
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

```


![Natal Região Metropolitana](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/7fad9f82841a64365d75fface029da161582a3c8/Natal_regi%C3%A3o_metropolitana.png)

Especificamente, a ligação entre os bairros de Nova Parnamirim e Neópolis destaca-se como uma área com problemas críticos de mobilidade. A alta densidade populacional nessa região faz fronteira entre as duas cidades, resultando em congestionamentos frequentes. Uma análise mais aprofundada desses dois bairros, utilizando o código abaixo, revela a importância da Avenida Ayrton Senna. Essa avenida, por sua grande quantidade de conexões entre os dois bairros, enfrenta um elevado volume de veículos diariamente.

```python
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Defina o local como uma lista de bairros ['Nova Parnamirim, RN', 'Neópolis, RN']
bairros = ['Nova Parnamirim, RN', 'Neópolis, RN']

# Obtenha o grafo da rede viária para os dois bairros
G_bairros = ox.graph_from_place(bairros, network_type='drive')

# Projete o grafo
G_bairros_projected = ox.project_graph(G_bairros)

# Plote o grafo
fig, ax = ox.plot_graph(G_bairros_projected, bgcolor='k', node_size=5, node_color='#999999', node_edgecolor='none', node_zorder=2,
                        edge_color='#555555', edge_linewidth=1.5, edge_alpha=1)

# Adicione rótulos para identificar os bairros
for bairro in bairros:
    gdf = ox.geocode_to_gdf([bairro])
    ax.annotate(bairro.split(',')[0], (gdf.geometry.centroid.x.values[0], gdf.geometry.centroid.y.values[0]),
                fontsize=8, ha='center', va='center', color='white')

plt.show()
```

A visualização destaca a relevância da Avenida Ayrton Senna na interconexão entre Nova Parnamirim e Neópolis, evidenciando a necessidade de estratégias específicas para gerenciar e melhorar a mobilidade nessa área crítica, isso só pode ser alcançado através da cooperação entre ambas as prefeituras e o governo do Estado, para melhorar a infraestrutura e o planejamento da Avenida e de suas conexões.
![Nova Parnamirim e Neópolis](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/7fad9f82841a64365d75fface029da161582a3c8/Nova_parnamirim_Ne%C3%B3polis.png)


# Problemática de Natal/Zona Norte/São Gonçalo do Amarante

A problemática da Zona Norte de Natal emerge como um dos principais desafios de mobilidade urbana no Estado do Rio Grande do Norte. A região enfrenta estrangulamentos críticos nas vias, notadamente nas duas pontes que atravessam o Rio Potengi. Esse fenômeno resulta em extensos engarrafamentos, particularmente durante os horários de pico, marcados pelas movimentadas idas ao trabalho pela manhã e o retorno no final da tarde.

A situação é agravada pelo expressivo fluxo de trabalhadores e estudantes que se dirigem à zona central e sul da cidade. Estas áreas, sendo centros comerciais e concentrando grande parte dos empregos da cidade, tornam-se destinos frequentes para a população da Zona Norte. O movimento intenso nesses horários cria não apenas congestionamentos, mas também desafios significativos para a eficiência do transporte público e a qualidade de vida dos residentes.

A necessidade de enfrentar essa problemática exige abordagens inovadoras e soluções estratégicas que visem a melhoria da infraestrutura viária, o reforço dos serviços de transporte público e a promoção de alternativas sustentáveis de deslocamento. A busca por uma mobilidade urbana mais eficiente na Zona Norte de Natal torna-se essencial não apenas para a comodidade dos cidadãos, mas também para o desenvolvimento sustentável e a vitalidade econômica da região.

![Mapa](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/main/PonteVelha.png)

## Estudo sobre as regiões

É viável incorporar ao grafo uma representação visual da importância das pontes e dos pontos críticos de estrangulamento nas vias. Estes são locais frequentemente escolhidos pelos motoristas para realizar a travessia, e tal análise fornece insights valiosos para o estudo sobre a expansão dessas travessias. A capacidade de visualizar de maneira intuitiva o mapa e identificar áreas de calor específicas contribui significativamente para o planejamento estratégico destinado a melhorar a mobilidade urbana.

Esses estudos não apenas evidenciam os gargalos nas pontes e nas rotas de travessia, mas também oferecem uma base sólida para a preparação de iniciativas que visam otimizar a eficiência do sistema viário. Ao entender a dinâmica do tráfego e as áreas críticas de congestionamento, torna-se possível formular propostas informadas sobre a ampliação ou criação de novas travessias, contribuindo assim para a fluidez do trânsito e para a qualidade de vida dos cidadãos.

A visualização da zona de calor no mapa proporciona uma perspectiva clara das áreas mais afetadas, permitindo uma abordagem proativa na implementação de melhorias. Este processo se revela crucial para o desenvolvimento sustentável da mobilidade urbana na Zona Norte de Natal, proporcionando soluções mais eficazes e adaptadas às necessidades específicas da comunidade.

![Mapa](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/main/graph_edges_PonteVelha.png)
![Mapa](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/main/graph_edges_PonteVelhaBike.png)

# Diferença dos gráficos entre carros e bicicletas( bicicleta - carros)

![Mapa](https://github.com/Pedro1p0/StreetMapper-with-OSMnx-and-NetworkX/blob/main/PonteVelha(bike-carros).png)

## Conclusão

O projeto de análise de mobilidade em Parnamirim, Rio Grande do Norte, proporcionou uma visão detalhada dos desafios enfrentados pela cidade, considerando seu crescimento acelerado, a conectividade com Natal e a presença da Base Aérea de Natal. Utilizando ferramentas como as bibliotecas NetworkX e OSMnx, exploramos a infraestrutura viária e identificamos pontos críticos, sendo a região entre os bairros Nova Parnamirim e Neópolis um foco especial devido a problemas recorrentes de congestionamento.

Durante a análise, a Avenida Ayrton Senna emergiu como um eixo vital na interconexão entre as duas cidades, evidenciando a necessidade de estratégias específicas para gerenciar e melhorar a mobilidade nessa área. A alta densidade populacional e o crescimento urbano ao redor da Base Aérea de Natal também representaram desafios singulares, exigindo uma abordagem colaborativa entre as autoridades locais e militares.

Sugerimos diversas estratégias para melhorar a mobilidade em Parnamirim, incluindo aprimoramentos na Avenida Ayrton Senna, gestão de fluxo de tráfego, investimento em transporte público, integração modal, zoneamento urbano planejado e diálogo com a comunidade. A cooperação entre prefeituras, governo estadual e participação ativa da comunidade é crucial para implementar essas estratégias de maneira eficaz. Ressaltamos a importância do monitoramento contínuo para avaliar a eficácia das intervenções ao longo do tempo, garantindo a adaptação às mudanças nas condições de tráfego.

Para os desafios de mobilidade na Zona Norte de Natal, é crucial adotar uma abordagem integrada e inovadora. A expansão e diversificação das travessias, incluindo a avaliação de novas pontes, e a otimização do transporte público são medidas essenciais para aliviar os congestionamentos nas pontes sobre o Rio Potengi. Incentivar o uso de meios sustentáveis, como ciclovias, e promover políticas de flexibilidade de trabalho também contribuirão para a redução do tráfego nos horários de pico. A implementação de soluções tecnológicas inteligentes, campanhas educativas e parcerias público-privadas fortalecerão a eficiência do sistema viário, proporcionando uma mobilidade urbana mais sustentável e melhorando a qualidade de vida na região.


# Vídeo explicando sobre o trabalho desenvolvido

https://drive.google.com/file/d/10Cm1iMwfl7Z5SViadmUY2YnR8Bcd70Uq/view?usp=sharing

## Licença

Este projeto é distribuído sob a licença [MIT](LICENSE). Sinta-se à vontade para usar e adaptar conforme necessário.

Explore, analise e contribua para melhorar a mobilidade em Parnamirim! 🚗🗺️
