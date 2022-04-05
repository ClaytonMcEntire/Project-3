"""
Project 3
Clayton McEntire, Andrew Farmer, Cameron Burdine
"""

import networkx as nx ##This will be what we will use for the graph

###The following code will need to be deleted, its purpose is to figure out how
###networkx works

G = nx.Graph() ##creates a new graph
H = nx.Graph()
H.add_node(10)
G.add_node(2)
G.add_node(1)##adds the node 1 to graph G
H.add_nodes_from(G)##This should add all the nodes from G to H
H.add_edge(10,1)
H.add_edge(10,2)
H.add_edge(1,2)

print(H)##prints the number of nodes and edges

print(list(H.nodes))##prints the nodes in a list
print(list(H.edges))##prints the edges in a list of sets

H.remove_node(1)

print(list(H.nodes))
print(list(H.edges))

###The Following code should set up the graph for question1
A = nx.Graph()
A.add_node("A")
A.add_node("B")
A.add_node("C")
A.add_node("D")
A.add_node("E")
A.add_node("F")
A.add_node("G")
A.add_node("I")
A.add_node("J")
A.add_node("M")
A.add_node("N")
A.add_node("H")
A.add_node("K")
A.add_node("L")
A.add_node("O")
A.add_node("P")

A.add_edge("A", "B")
A.add_edge("A", "E")
A.add_edge("A", "F")
A.add_edge("B", "C")
A.add_edge("B","F")
A.add_edge("C", "D")
A.add_edge("C","G")
A.add_edge("D", "G")
A.add_edge("E", "F")
A.add_edge("E", "I")
A.add_edge("I", "J")
A.add_edge("J", "G")
A.add_edge("I", "M")
A.add_edge("M", "N")
A.add_edge("H", "K")
A.add_edge("H", "L")
A.add_edge("K", "O")
A.add_edge("K", "L")
A.add_edge("L", "P")


print(list(A.nodes))
print(list(A.edges))