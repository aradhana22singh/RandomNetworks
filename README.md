# RandomNetworks
#Generating random networks, degree fitting
#Generating random networks of various degrees using Erdős–Rényi model
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
nx.draw(G, with_labels = False, node_size=20) #visualizing the network
plt.savefig("filename.png")
Degree = np.zeros(N, int)
max_deg =0;
avg_deg =0;
#in the following calculating the degree of each node
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


