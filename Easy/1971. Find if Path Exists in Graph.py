# -*- coding: utf-8 -*-
"""
Problem  
Given an undirected graph represented as an integer `n` (the number of nodes),  
a list of `edges`, a `source` node, and a `destination` node,  
determine whether there exists a valid path between `source` and `destination`.  

Solution  
This solution uses **Breadth-First Search (BFS)** to explore all possible paths from the source node.  
A queue is used to traverse the graph level by level while marking visited nodes to avoid cycles.  
If the destination node is reached during the traversal, the function returns `True`;  
otherwise, it returns `False`.  
The graph is implemented as an adjacency list, and BFS ensures an efficient search in **O(N + E)** time complexity,  
where `N` is the number of nodes and `E` is the number of edges.  
The space complexity is also **O(N + E)** due to the adjacency list representation and the visited set.  
"""

class bfs_graph:
    def __init__(self):
        self.graph = {}
        self.color_graph = {}
    
    def add_node(self,node):
        if node not in self.graph:  
            self.graph[node] = []
            self.color_graph[node]=False
    def add_edge(self,node_1,node_2):
        self.graph[node_1].append(node_2)
        self.graph[node_2].append(node_1)

    def bfs(self,start,final_point):
        queue = [start]
        self.color_graph[start]=True
        while queue:
            actual = queue.pop()
            for next_node in self.graph[actual]:
                if next_node == final_point:
                    return True
                if self.color_graph[next_node]==False:
                    queue.append(next_node)
                    self.color_graph[next_node]=True
        return False



class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n ==1:
            return True
        graph = bfs_graph()
        for i in range(n):
            graph.add_node(i)
        for node_1,node_2 in edges:
            graph.add_edge(node_1,node_2)
        return graph.bfs(source,destination)
        