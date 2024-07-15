#importing libraries
import networkx as nx
import matplotlib.pyplot as plt

#creating undirected graph
G = nx.Graph()

#nodes added
nodes = ["A", "B", "C", "D", "E"]
G.add_nodes_from(nodes)

#adding edges
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
G.add_edges_from(edges)

#to visualize the graph
def visualize_graph(G, title):
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold")
    plt.title(title)
    plt.show()

visualize_graph(G, "Simple Undirected Graph")

#BFS Traversal
print("BFS Traversal starting from 'A':")
bfs_traversal = list(nx.bfs_tree(G, source="A"))
print(bfs_traversal)

#DFS Traversal
print("\nDFS Traversal starting from 'A':")
dfs_traversal = list(nx.dfs_tree(G, source="A"))
print(dfs_traversal)

#shortest path w BFS
print("\nShortest path from 'A' to 'E':")
shortest_path = nx.shortest_path(G, source="A", target="E")
print(shortest_path)

#visualizing shortest path
path_edges = list(zip(shortest_path, shortest_path[1:]))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold")
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
plt.title("Shortest Path from 'A' to 'E'")
plt.show()
