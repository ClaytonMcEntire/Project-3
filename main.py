"""
Project 3
Clayton McEntire, Andrew Farmer, Cameron Burdine
"""

import networkx as nx ##This will be what we will use for the graph; https://networkx.org/documentation/stable/tutorial.html
import dfs_path as dfs
import bfs_paths as bfs
from networkx.algorithms import tree
import matplotlib.pyplot as plt



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
v = dfs.dfs_path(A, "A", "H")
print("DFS PATH: " + str(v))

# BFS
paths = nx.bfs_edges(A, "A")
paths= list(paths)
print("BFS: ")
print(paths)

# Draw Visual Graph
plt.figure(1)
nx.draw(A, with_labels=True, font_weight='bold')
#nx.draw_shell(A, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')


# DIRECTED GRAPH 
DG = nx.DiGraph()
DG.add_edge("4","2")
DG.add_edge("4","12")
DG.add_edge("4","1")
DG.add_edge('1','3')
DG.add_edge('2','1')
DG.add_edge('3','2')
DG.add_edge('3','5')
DG.add_edge('5','6')
DG.add_edge('5','8')
DG.add_edge('6','8')
DG.add_edge('6','7')
DG.add_edge('6','10')
DG.add_edge('7','10')
DG.add_edge('10','9')
DG.add_edge('10','11')
DG.add_edge('9','11')
DG.add_edge('9','5')
DG.add_edge('8','10')
DG.add_edge('8','9')
DG.add_edge('11','12')

plt.figure(2)
nx.draw(DG, with_labels=True, font_weight='bold')

## a) Use an application to find the strongly connected components of the digraph;

## Finds the strongly connected components
scc=list(nx.strongly_connected_components(DG))
## Finds the strongly connected components using Kosaraju's algorithm
scc2 = list(nx.kosaraju_strongly_connected_components(DG))

print("\nThe Strongly Connected components are")
print(str(scc))
print("\nThe Strongly Connected components using Kosaraju's algorithm are")
print(str(scc2))


## b) Draw the digraph as a ‘meta graph’ of its strongly connected components in your project
##    report; and then

##Meta Graph of strongly connected components 
MG = nx.DiGraph()
MG.add_edge('11','12')
MG.add_edge('4','12')
MG.add_edge('4','2,3,1')
MG.add_edge('2,3,1','10,7,5,6,8,9')
MG.add_edge('10,7,5,6,8,9','11')

plt.figure(3)
nx.draw(MG, with_labels = True, font_weight='bold')


## c) Represent the ‘meta graph’ as a DAG and linearize it in its topological order. 

li = list(reversed(list(nx.topological_sort(MG))))
print("\nlist2"+str(li))


## Check to see if Graph is a DAG True/False
isDAG = nx.is_directed_acyclic_graph(MG)
print("\nIs Graph a DAG: "+str(isDAG))


topsort = list(nx.topological_sort(nx.line_graph(MG)))

print("\nTopilogical Sort"+str(topsort))


# WEIGHTED UNDIRECTED GRAPH 
WG = nx.Graph()
WG.add_node("A")
WG.add_node("B")
WG.add_node("C")
WG.add_node("D")
WG.add_node("E")
WG.add_node("F")
WG.add_node("G")
WG.add_node("H")
WG.add_node("I")

WG.add_edge("A", "B", weight=22)
WG.add_edge("A", "C", weight=9)
WG.add_edge("A", "D", weight=12)
WG.add_edge("B", "C", weight=35)
WG.add_edge("B", "F", weight=36)
WG.add_edge("B", "H", weight=34)
WG.add_edge("C", "F", weight=42)
WG.add_edge("C", "E", weight=65)
WG.add_edge("C", "D", weight=4)
WG.add_edge("D", "E", weight=33)
WG.add_edge("D", "I", weight=30)
WG.add_edge("E", "F", weight=18)
WG.add_edge("E", "G", weight=23)
WG.add_edge("F", "H", weight=24)
WG.add_edge("F", "G", weight=39)
WG.add_edge("G", "H", weight=25)
WG.add_edge("G", "I", weight=21)
WG.add_edge("H", "I", weight=19)

plt.figure(4)
nx.draw(WG, with_labels=True, font_weight='bold')
## a) Write an application that applies Dijkstra’s algorithm to produce the shortest path tree for
##    a weighted graph with a given starting node. Test and verify your program with the given
##    graph starting with node A;
x = nx.dijkstra_path(WG, "A", "G")
x = list(x)
print(x)

## b) Write a program that produces a minimum spanning tree for a connected weighted graph.
##    Test your program with the given graph above; 
mst = tree.minimum_spanning_edges(WG, algorithm="kruskal", data=False)
edgelist=list(mst)
print(edgelist)

## c) Are a shortest path tree and a minimum spanning tree usually the same?

## d) If the graph has an edge with a negative weight, can you apply Dijkstra’s algorithm to
##    find a shortest path tree? 
