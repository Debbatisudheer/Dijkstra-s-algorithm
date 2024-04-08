import networkx as nx
import matplotlib.pyplot as plt

def dijkstra_shortest_path(graph, start, end):
    # Calculate shortest paths from start node to all other nodes
    shortest_paths = nx.single_source_dijkstra_path_length(graph, start)

    # Extract the shortest path from start to end node
    path = nx.shortest_path(graph, source=start, target=end, weight='weight')

    # Extract the length of the shortest path
    path_length = shortest_paths[end]

    return path, path_length


def visualize_shortest_path(graph, path):
    # Plot the graph
    pos = nx.spring_layout(graph, k=0.5)  # Adjust the k parameter for increased spacing
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1,
            font_size=15)

    # Highlight the shortest path
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, width=4, alpha=0.5, edge_color='r')

    # Add edge labels (weights)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    # Show the plot
    plt.title('Shortest Path')
    plt.show()


# Create a sample graph with edge weights in kilometers
G = nx.Graph()
G.add_edge('A', 'B', weight=2)  # 2 km
G.add_edge('A', 'C', weight=4)  # 4 km
G.add_edge('B', 'C', weight=3)  # 3 km
G.add_edge('B', 'D', weight=6)  # 6 km
G.add_edge('C', 'D', weight=1)  # 1 km
G.add_edge('C', 'E', weight=5)  # 5 km
G.add_edge('D', 'E', weight=2)  # 2 km


# Find the shortest path from node 'A' to node 'E'
start_node = 'A'
end_node = 'E'
shortest_path, path_length = dijkstra_shortest_path(G, start_node, end_node)

# Visualize the shortest path
print("Shortest Path from", start_node, "to", end_node, ":", shortest_path)
print("Shortest Path Length:", path_length, "km")
visualize_shortest_path(G, shortest_path)