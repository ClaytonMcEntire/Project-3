"""
Project 3
Clayton McEntire, Andrew Farmer, Cameron Burdine
"""

import networkx as nx ##This will be what we will use for the graph
import dfs_path as dfs


###The Following code should set up the graph for question1
### NROMAL GRAPH 
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


##Link to understanding DFS https://www.programiz.com/dsa/graph-dfs


## a) Starting from any vertex, can DFS and BFS find all connected components of an
##undirected graph? 

## b) Can both BFS and DFS determine if there is a path between two given nodes?

## c)There is a path between two vertices x and y. If started from x, do DFS and BFS always
## find exactly the same path? 

# DFS 
v = dfs.dfs_path(A, "A", "J")
print("DFS PATH: " + str(v))

# BFS

# Draw Visual Graph
nx.draw(A, with_labels=True, font_weight='bold')
#nx.draw_shell(A, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')


# DIRECTED GRAPH 






## a) Use an application to find the strongly connected components of the digraph;
## b) Draw the digraph as a ‘meta graph’ of its strongly connected components in your project
##    report; and then
## c) Represent the ‘meta graph’ as a DAG and linearize it in its topological order. 


# WEIGHTED UNDIRECTED GRAPH 





## a) Write an application that applies Dijkstra’s algorithm to produce the shortest path tree for
##    a weighted graph with a given starting node. Test and verify your program with the given
##    graph starting with node A;

## b) Write a program that produces a minimum spanning tree for a connected weighted graph.
##    Test your program with the given graph above; 

## c) Are a shortest path tree and a minimum spanning tree usually the same?

## d) If the graph has an edge with a negative weight, can you apply Dijkstra’s algorithm to
##    find a shortest path tree? 
