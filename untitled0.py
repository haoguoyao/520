#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 02:58:26 2020

@author: apple
"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
#G = nx.Graph()
edges=pd.read_csv('/Users/apple/Desktop/526/cit-Patents_10.txt',sep=',',header=None, names = ["one","two"])
#edges.to_csv('/Users/apple/Desktop/526/cit-Patents_16.csv',header=0,index = 0)
G = nx.from_pandas_dataframe(edges, source = "one", target = "two", edge_attr=None, create_using=None)
#G.add_edges_from(edges.to_dict)
plt.subplot(121)
nx.draw(G, with_labels=False)
plt.show()

#g.hypergraph(source="one",destination="dst").plot(edges)

#g.bind(source="one",destination="dst")


#g.plot(edges)


#print (edge[1:10])