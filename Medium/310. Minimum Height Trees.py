# -*- coding: utf-8 -*-
"""
Problem  
Given a tree with `n` nodes labeled from `0` to `n - 1` and an array `edges` representing  
the edges of the tree, return all the **roots** that form **Minimum Height Trees (MHTs)**.  
A **Minimum Height Tree** is a tree where the longest path from the root to any leaf is minimized.  

Solution  
This solution simulates the **pruning of leaves** iteratively until only one or two nodes remain,  
which will be the roots of the **Minimum Height Trees**.  
- The graph is represented as an adjacency list.  
- Nodes with only one connection (leaves) are removed iteratively.  
- The process continues until at most two nodes remain, as they are the **centers** of the tree.  
- The final nodes are returned as the possible MHT roots.  

This approach runs in **O(N)** time complexity, as each node and edge is processed once,  
and **O(N)** space complexity due to storing the graph structure.
"""
from typing import List

class Graph:
    def __init__(self):
        self.graf = {}
        self.graf_size = {}
    
    def add_node(self,node):
        if node not in self.graf:
            self.graf[node]=[]
            self.graf_size[node]=0
    
    def add_edge(self,node_1,node_2):
        self.graf[node_1].append(node_2)
        self.graf_size[node_1]+=1
        self.graf[node_2].append(node_1)
        self.graf_size[node_2]+=1
    
    def remove_node(self,node,node_removed):
        self.graf[node].remove(node_removed)
        self.graf_size[node]-=1
    
    def find_all_nodes_to_remove(self):
        
        if len(self.graf)<=2:
            return True
        node_to_remove = []
        for node in self.graf_size:
            if self.graf_size[node]==1:
                node_to_remove.append(node)
        for node in node_to_remove:
            self.remove_node(self.graf[node][0],node)
            del self.graf[node],self.graf_size[node]
        if len(self.graf)>2:
            self.find_all_nodes_to_remove()

                
    



class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graf = Graph()
        for node in range(n):
            graf.add_node(node)
        for node_1,node_2 in edges:
            graf.add_edge(node_1,node_2)

        graf.find_all_nodes_to_remove()
        return list(graf.graf.keys())
