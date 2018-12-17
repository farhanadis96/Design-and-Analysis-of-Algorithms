import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
from random import randint
from operator import itemgetter
import time

#n=list(random.sample(range(100,1000),10))
n=[100,300,500,700,900,1000]
print(n)
for i in n:
    start_time = time.time()

    graph=nx.cycle_graph(i)
    # print("Original Graph")
    # print(nx.info(graph))

    # nx.draw(graph, with_labels=True)
    # plt.show()

    for edge in graph.edges():
        graph.edges[edge]["weight"] = int(np.random.uniform(2, 100))
    
    # for edge in graph.edges():
    #     print(graph.edges[edge]["weight"])
    # print("Edges of original graph")
    # print(graph.edges(data=True))

    graph.add_edge(1,graph.size()-1,weight=1)

    y=graph.edges()
    for edge in y:
        #a.append(tree1.edges[edge]["weight"])
        if graph[1][graph.size()-2]['weight'] < y[edge]["weight"]:
            x=False
    if x==True:
        print("Execution time=", time.time() - start_time)
        print("MST NOT CHANGED")
    elif x==False:
        print("Execution time=", time.time() - start_time)
        print("MST CHANGED")
    
    print("-------------------------------------------------------------------------------------------------------------")

y=[0.002991914749145508,0.028924942016601562,0.09673857688903809,0.18051671981811523,0.307175874710083,0.36302661895751953]
x=[100, 300, 500, 700, 900, 1000]

# plotting the points 
plt.plot(x,y)

# naming the x axis
plt.xlabel('number of nodes (vertices)')

# naming the y axis
plt.ylabel('Execution time')

# giving a title to my graph
plt.title('Time complexity to check if current MST has been updated after adding a new edge to graph G')

# function to show the plot
plt.show()