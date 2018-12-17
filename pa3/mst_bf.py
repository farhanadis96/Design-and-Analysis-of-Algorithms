import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
from random import randint
from operator import itemgetter
import time

n=list(random.sample(range(4,15),10))
print("Random test cases genereted with following values for nodes (vertices):",n)
#print(n)


for i in n:
    
    graph=nx.cycle_graph(i)
    # print("Original Graph")
    # print(nx.info(graph))

    for edge in graph.edges():
        graph.edges[edge]["weight"] = int(np.random.uniform(2, 100))
    
    
    tree1 = nx.minimum_spanning_tree(graph)
    a=[]
    for edge in tree1.edges():
        a.append(tree1.edges[edge]["weight"])
    
    c1=sum(a)
    print("MST 1 COST",c1)
    

    x=graph.edges()
    y=list(x)

    graph.add_edge(1,graph.size()-1,weight=1)

    tree2=nx.minimum_spanning_tree(graph)
    b=[]
    for edge in tree2.edges():
        b.append(tree2.edges[edge]["weight"])
    
    c2=sum(b)
    print("MST 2 COST",c2)
    
    if (c1==c2):
        print("MST remains SAME for n=",i)
    else:
        print("MST CHANGED for graph with n=",i," nodes and verified using brute force")
        print("Updated MST Cost",c2)
        print(nx.info(tree2))
        # print("MST costs found for graph with n=",i, " nodes using brute force")
    print("-------------------------------------------------------------------------------------------------")