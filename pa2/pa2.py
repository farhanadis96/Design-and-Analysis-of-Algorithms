
import matplotlib.pyplot as plt
import random
import numpy as np
import networkx as nx
import collections
import operator




edge=5
num_nodes=[]
num_edges=[]

t_s=[1000,2500,5000,7500,10000]

p=[60,75,90]

for i in p:

    
    gr = nx.DiGraph()
    gr.add_node(1)
    gr.add_node(2)
    
    gr.add_edge(1, 2)
    gr.add_edge(1, 1)
    
    
    
    



    for x in t_s:
        for j in range(x):



            edge+=1
            
            pr=random.randint(0, 100)
            if pr>i:
                 if j<3:
                     print("Adding more nodes (More death processes taking place)") 
                     
                     gr.add_node(3)
                     gr.add_node(4)
                     gr.add_node(5)
    
    
    
                     
                     gr.add_edge(1, 3)
                     gr.add_edge(2,5)
                     gr.add_edge(2,4)
                     

                     
                    
            if pr <= i: #birth process
                
                
               
                try:

                    degree = np.array(gr.degree())
                except KeyError:
                    break
                
                
                deg = degree[:, 1]
                prob = deg / (2 * gr.number_of_edges())
                
                nodes = degree[:, 0]
                new_node = np.random.choice(nodes, 1, p=prob)
                
                new_node=new_node[0]
                gr.add_node(edge)
                gr.add_edge(new_node,edge)
                
            else: #death process
                
                
                try:

                    degree = np.array(gr.degree())
                except KeyError:
                    break
                
                
                deg = degree[:, 1]

                k=gr.number_of_nodes()
                prob=(abs(k-deg))/((k)**2-(2*gr.number_of_edges()))
                

                prob=np.array(prob)
                prob /= prob.sum()
                
                nodes = degree[:, 0]
                d_node = np.random.choice(nodes, 1, p=prob)
                d_node=d_node[0]
                gr.remove_node(d_node)
        print("Time step completed :",x," for probability :",i)
        num_nodes.append(gr.number_of_nodes())
        num_edges.append(gr.number_of_edges())
    
        
        
d=[]


degree=np.array(gr.degree())


d=degree[:,1]
freq=collections.Counter(d)
print(freq)

y_deg = sorted(freq.items(), key=operator.itemgetter(1))

y_deg=np.array(y_deg)
x_freq=np.array(y_deg[:,0])
print(type(x_freq))

y_deg=np.cumsum(y_deg[:,1])
max=max(y_deg)

y_deg=y_deg/(max)


x_freq=list(x_freq)
x_freq.sort(reverse=True)


plt.loglog(x_freq,y_deg)

plt.xlabel('k')
plt.ylabel('P(k)')
plt.title('Cumulative degree distribution')
plt.show()


y=num_nodes[0:5]
x=[1000,2500,5000,7500,10000]
plt.plot(x,y,'r')

y=num_nodes[5:10]
x=[1000,2500,5000,7500,10000]
plt.plot(x,y,'b')

y=num_nodes[10:15]
x=[1000,2500,5000,7500,10000]
plt.plot(x,y,'y')

plt.xlabel('time step')
plt.ylabel('number of nodes')
plt.title('time step Vs number of nodes')

plt.show()


b=num_edges[0:5]
a=[1000,2500,5000,7500,10000]
plt.plot(a,b,'r')

b=num_edges[5:10]
a=[1000,2500,5000,7500,10000]
plt.plot(a,b,'b')

b=num_edges[10:15]
a=[1000,2500,5000,7500,10000]
plt.plot(a,b,'y')

plt.xlabel('time step')
plt.ylabel('number of edges')
plt.title('time step Vs number of edges')

plt.show()
print("Nodes :",num_nodes)
print("Edges :",num_edges)