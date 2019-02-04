import json
import networkx as nx

with open('dataName.json', 'r') as dataJson:  # Open the file
    dataName = json.load(dataJson)

node_names = [n['id'] for n in dataName['nodes']]
edges = [(e["source"], e["target"],) for e in dataName["links"]]

G = nx.Graph()
G.add_nodes_from(node_names)
G.add_edges_from(edges)

density = nx.density(G)
degree_dict = dict(G.degree(G.nodes()))
nx.set_node_attributes(G, degree_dict, 'degree')
eigenvector_dict = nx.eigenvector_centrality(G)  # Run eigenvector centrality
nx.set_node_attributes(G, eigenvector_dict, 'eigenvector')

to_send_to_d3 = nx.node_link_data(G)

for n in to_send_to_d3['nodes']:
    if n['eigenvector'] > 0.3 or n['degree'] > 20:
        n.update({'color': 'black', 'size': 600})
    elif n['eigenvector'] > 0.2 or n['degree'] > 6:
        n.update({'color': 'darkred', 'size': 300})
    elif n['eigenvector'] > 0.1 or n['degree'] > 2:
        n.update({'color': 'orange', "size": 200})
    else:
        n.update({'color': 'lightblue', "size": 20})

to_send_to_d3['nodes'] = sorted(to_send_to_d3['nodes'], key=lambda l: (l['eigenvector'], l['degree']), reverse=True)

with open('networkx_data_json.json', 'w') as json_file:
    json_file.write(json.dumps(to_send_to_d3))
