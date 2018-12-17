import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
from random import randint
from operator import itemgetter
import time

n=list(random.sample(range(100,1000),10))
print("Random test cases genereted with following values for nodes (vertices):",n)


for i in n:
    graph=nx.cycle_graph(i)
    # print("Original Graph")
    # print(nx.info(graph))

    # nx.draw(graph, with_labels=True)
    # plt.show()

    for edge in graph.edges():
        graph.edges[edge]["weight"] = int(np.random.uniform(2, 100))
    
    

    tree1 = nx.minimum_spanning_tree(graph)
    a=[]
    for edge in tree1.edges():
        a.append(tree1.edges[edge]["weight"])
    
    c1=sum(a)
    print("MST 1 COST :",c1)
    # print("MST 1 edges",tree1.edges(data=True))

    x=graph.edges()
    y=list(x)

    graph.add_edge(1,graph.size()-1,weight=1)

    tree2=nx.minimum_spanning_tree(graph)
    b=[]
    for edge in tree2.edges():
        b.append(tree2.edges[edge]["weight"])
    
    c2=sum(b)
    #print("MST 2 cost",c2)
    #print("MST 2 edges",tree2.edges(data=True))

    y=graph.edges()
    for edge in y:
        #a.append(tree1.edges[edge]["weight"])
        if graph[1][graph.size()-2]['weight'] < y[edge]["weight"]:
            x=False
    if x==True:
        print("MST NOT CHANGED")
    elif x==False:
        print("MST CHANGED because of new edge added")

        tree_upd=tree1

        x=list(graph.edges(data=True))
        #print(x)

        w=[]
        for u,v,q in x:
            w.append(graph[u][v]['weight'])
    
        y=w.index(min(w))
        a=x[y]
    
        tree_upd.add_edge(a[0],a[1],weight=min(w))

        cyc=list(nx.find_cycle(tree_upd, orientation='ignore'))
        #print(cyc)

    

        arr_1=[]
        arr_2=[]
        for u,v,q in cyc:
            #print(u,v)
            arr_1.append(u)
            arr_2.append(v)
        #     arr.append(u,v)
        # print(arr)
        #zipped_list = zip(list_a, list_b)
        zlist = zip(arr_1,arr_2)
        cyc_edges=list(zlist)
        #print("Cycle edges",cyc_edges)
        # print(arr_1)
        # print(arr_2)
        arr_3=[]
        for edge in cyc_edges:
            #print(tree_upd.edges[edge]["weight"])
            arr_3.append(tree_upd.edges[edge]["weight"])
            maximum=max(arr_3)
        #print("weights of cycle",arr_3)
        #print("maximum weight in cycle",maximum)
        # print(arr_3)
        #     x=list(tree_upd.edges(data=True))
        # print(x)
        #print(max(x['weight']))
        cyc_edges_weights=zip(cyc_edges,arr_3)
        #print(list(cyc_edges_weights))
        y=arr_3.index(max(arr_3))
        #print("position number",y)
        #print("edge to be removed",cyc_edges[y])
        tree_upd.remove_edge(cyc_edges[y][0],cyc_edges[y][1])
        print("UPDATED MST")
        print(nx.info(tree_upd))
        d=[]
        for edge in tree_upd.edges():
            d.append(tree_upd.edges[edge]["weight"])
        # print(a)
        # print(tree1.edges[edge]["weight"])
        #print(b)
        c3=sum(d)
        print("MST UPDATED cost :",c3)

        #print("MST 2 edges",tree_upd.edges(data=True))
    # checing solution via brute force technique
    
        print("MST costs found for graph with n=",i, " nodes")
    
    print("-------------------------------------------------------------------------------------------------------------")
    

    



    

    

