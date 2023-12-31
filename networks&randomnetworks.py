# -*- coding: utf-8 -*-
"""Networks&RandomNetworks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SzXOfXnpyU2nNgvh8iVtglbMvPHBtjhv
"""

class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=False):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed

        # Different representations of a graph
        self.m_list_of_edges = []

    # Add edge to a graph
    def add_edge(self, node1, node2, weight=1):
        # Add the edge from node1 to node2
        self.m_list_of_edges.append([node1, node2, weight])

        # If a graph is undirected, add the same edge,
        # but also in the opposite direction
        if not self.m_directed:
            self.m_list_of_edges.append([node2, node1, weight])

	# Print a graph representation
    def print_edge_list(self):
        num_of_edges = len(self.m_list_of_edges)
        for i in range(num_of_edges):
            print("edge ", i+1, ": ", self.m_list_of_edges[i])

graph = Graph(5)

graph.add_edge(0, 5, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_edge_list()

"""Note: If you wanted to make this graph undirected, you should the constructor in the following way: graph = Graph(5, directed=True).

#How to Implement an Adjacency Matrix in Python
"""

class Graph:
    def __init__(self, num_of_nodes, directed=False):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed

        # Initialize the adjacency matrix
        # Create a matrix with `num_of_nodes` rows and columns
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                            for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight):
        self.m_adj_matrix[node1][node2] = weight

        if not self.m_directed:
            self.m_adj_matrix[node2][node1] = weight

    def print_adj_matrix(self):
        print(self.m_adj_matrix)

graph = Graph(5)

graph.add_edge(0, 4, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_adj_matrix()

class RandomGraph:
    def __init__(self, num_of_nodes, avgdeg, directed=False):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed
        p = avgdeg/(num_of_nodes-1) #probability of the existance of the connection

        # Initialize the adjacency matrix
        # Create a matrix with `num_of_nodes` rows and columns
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                            for row in range(num_of_nodes)]
        import random #import library to generate random numbers
        for i in range(num_of_nodes):
          for j in range(i+1, num_of_nodes):
            a = random.uniform(0, 1)  #generate uniformly distributed number between 0 and 1

            if(a<p):
              self.m_adj_matrix[i][j] = 1
              if not self.m_directed:
                self.m_adj_matrix[j][i] = 1

    def print_adj_matrix(self):
        print(self.m_adj_matrix)

G = RandomGraph(10, 2)
G.print_adj_matrix()

#Generating random networks of various degrees
import numpy as np
import random
import matplotlib.pyplot as plt
N = 50 #number of nodes in the network
avgdeg = 6 #average degree of the network
p = avgdeg/(N-1) #probability of the existance of the connection
A = np.zeros((N,N), float) #initializing the adjacency matrix
for i in range(N):
  for j in range(i+1, N):
    a = random.uniform(0, 1)  #generate uniformly distributed number between 0 and 1
    if(a<p):
      A[i][j] = 1
      A[j][i] = 1
import networkx as nx
G = nx.from_numpy_array(A)
nx.draw(G, with_labels = False, node_size=20)
plt.savefig("filename.png")

Degree = np.zeros(N, int)
max_deg =0;
avg_deg =0;
for i in range(N):
  d =0
  for j in range(N):
    if(A[i][j]>0):
      d = d +1
  Degree[i]=d;
  if(d>max_deg):
    max_deg = d
  avg_deg = d+avg_deg
avg_deg = int(avg_deg/N)
n_bins=10
Prob, binedge = np.histogram(Degree, n_bins, density=True)
plt.hist(Degree, n_bins, density=True)
print(Prob, binedge)
from scipy.stats import binom
from scipy.stats import poisson
print(avgdeg, N)
Binom_pmf = np.zeros(max_deg+5, float)
Poisson_pmf = np.zeros(max_deg+5, float)
for i in range(max_deg+5):
  k=i
  p = avgdeg/(N-1)
  res1 = binom.pmf(k, N, p)
  Binom_pmf[i]= float(res1)
  res2 = poisson.pmf(i, avgdeg)
  Poisson_pmf[i] = float(res2)
plt.plot(Binom_pmf, '-*', color='y')
plt.plot(Poisson_pmf, '-.', color='r')