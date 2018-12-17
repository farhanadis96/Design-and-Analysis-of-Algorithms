import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
from random import randint
from operator import itemgetter
import time

#n=list(random.sample(range(100,1000),10))
#n=[4,5,6,7,8,9,10,100,300,500,700,900,1000]
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

    tree1 = nx.minimum_spanning_tree(graph)
    # a=[]
    # for edge in tree1.edges():
    #     a.append(tree1.edges[edge]["weight"])
    
    # c1=sum(a)
    #print("MST 1 COST",c1)
    # print("MST 1 edges",tree1.edges(data=True))

    # x=graph.edges()
    # y=list(x)

    graph.add_edge(1,graph.size()-1,weight=1)

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
        

    cyc=list(nx.find_cycle(tree_upd, orientation='ignore'))
   
    

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
    #print("UPDATED MST")
    #print(nx.info(tree_upd))
    d=[]
    for edge in tree_upd.edges():
        d.append(tree_upd.edges[edge]["weight"])
    # print(a)
    # print(tree1.edges[edge]["weight"])
    #print(b)
    c3=sum(d)
    print("Execution time=", time.time() - start_time)
    print("MST UPDATED cost",c3)

    #print("MST 2 edges",tree_upd.edges(data=True))

    # if c2==c3:
    #     print("MST costs MATCHED for n=",i)
    # else:
    #     print("MST costs DO NOT MATCH for n=",i)

y=[0.004987478256225586,0.011969566345214844,0.030914306640625,0.05585122108459473,0.072936582565307617,0.09086541175842285]
x=[100, 300, 500, 700, 900, 1000]

# plotting the points 
plt.plot(x,y)

# naming the x axis
plt.xlabel('number of nodes (vertices)')

# naming the y axis
plt.ylabel('Execution time')

# giving a title to my graph
plt.title('Time complexity to update MST')

# function to show the plot
plt.show()





    