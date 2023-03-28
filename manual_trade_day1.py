import networkx as nx

# create the directed graph
G = nx.DiGraph()
G.add_node('Shells')
G.add_node('Pizza')
G.add_node('Root')
G.add_node('Snowball')

G.add_edge('Pizza', 'Root', weight=0.5)
G.add_edge('Pizza', 'Snowball', weight=1.45)
G.add_edge('Pizza', 'Shells', weight=0.75)

G.add_edge('Root', 'Snowball', weight=3.1)
G.add_edge('Root', 'Shells', weight=1.49)
G.add_edge('Root', 'Pizza',weight=1.95)

G.add_edge('Snowball', 'Shells', weight=0.48)
G.add_edge('Snowball', 'Pizza', weight=0.67)
G.add_edge('Snowball', 'Root', weight=0.31)

G.add_edge('Shells', 'Pizza', weight=1.34)
G.add_edge('Shells', 'Root', weight=0.64)
G.add_edge('Shells', 'Snowball', weight=1.98)

# find the best path to take to get the maximum value
max_depth = 5
start_node = 'Shells' #also end_node
max_value = -float('inf')
max_path = []

for path in nx.all_simple_paths(G, start_node, start_node, cutoff=max_depth):
    value = 1
    for i in range(len(path)-1):
        node1 = path[i]
        node2 = path[i+1]
        weight = G.edges[(node1, node2)]['weight']
        value *= weight
    if value > max_value:
        max_value = value
        max_path = path

    print(f"Value after visiting {path[-1]}: {value:.2f}")

print(f"\nMaximum value found: {max_value:.2f}")
print(f"Path to obtain maximum value: {max_path}")
