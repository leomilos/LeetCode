# -*- coding: utf-8 -*-
"""
Problem  
Given a 2D list `edges` representing an undirected star graph,  
find the center node.  
A star graph consists of one central node connected to all other nodes,  
with no additional connections.  

Solution  
This solution iterates through the edges and maintains a count of  
the number of connections for each node using a dictionary.  
The node with the highest count is identified as the center node.  
Since a star graph always has one central node connected to all others,  
it will have the maximum number of edges (n-1 for an n-node graph).  
This approach runs in O(N) time complexity, where N is the number of edges,  
and O(N) space complexity due to the dictionary used for counting occurrences.  
"""

from typing import List
class Star_graph:
    def __init__(self):
        self.graph = {}
        self.max_count = {}
        self.actual_max = 0
        self.max_node = 0

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node]=[]
            self.max_count[node] = 0
    
    def add_edge(self,node_1,node_2):
        self.graph[node_1].append(node_2)
        self.graph[node_2].append(node_1)
        self.max_count[node_1] +=1
        self.max_count[node_2] +=1
        if self.max_count[node_1]>self.actual_max:
            self.actual_max = self.max_count[node_1]
            self.max_node = node_1
        if self.max_count[node_2]>self.actual_max:
            self.actual_max = self.max_count[node_2]
            self.max_node = node_2
    
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        actual_max = 0
        max_node = 0
        range_edge = len(edges)
        count_of_values = {}
        for i in range(range_edge+1):
            count_of_values[i+1] = 0
        for node_1,node_2 in edges:
            count_of_values[node_1]+=1
            count_of_values[node_2]+=1
            if count_of_values[node_1]>actual_max:
                actual_max = count_of_values[node_1]
                max_node = node_1
            if count_of_values[node_2]>actual_max:
                actual_max = count_of_values[node_2]
                max_node = node_2
        return max_node