# -*- coding: utf-8 -*-
"""
Problem  
Given a list of directed edges `times` where `times[i] = [u, v, w]` represents a signal  
traveling from node `u` to node `v` in `w` time, determine how long it will take for  
all nodes to receive the signal starting from node `k`.  
If some nodes are unreachable, return `-1`.  

Solution  
This solution implements **Dijkstra’s algorithm** using a **min-heap (priority queue)**  
to find the shortest path from the starting node `k` to all other nodes.  
- The graph is represented as an adjacency list with weighted edges.  
- A priority queue is used to process nodes with the shortest known distance first.  
- The algorithm updates the minimum distance to each node and continues processing  
  until all reachable nodes have been visited.  
- The maximum distance among all reachable nodes is returned as the answer.  
- If any node remains at infinite distance, it means it is unreachable, so `-1` is returned.  

This approach runs in **O(E log N)** time complexity, where `E` is the number of edges  
and `N` is the number of nodes, making it optimal for sparse graphs.  
"""

import heapq
class Graph():
    def __init__(self):
        self.graf  = {}
        self.color = {}
    
    def add_vertice(self,node):
        if node not in self.graf:
            self.graf[node]=[]
            self.color[node]=False
    
    def add_edge(self,node_1,node_2,weight):
        self.graf[node_1].append((node_2,weight))
    
    def dijkstra(self,start):
        self.distance = {node: float('inf') for node in self.graf}
        alredy_visited = set()
        self.distance[start]=0
        queue = [(0,start)]
        while queue:
            actual_distance, actual_node = heapq.heappop(queue)
            if actual_node in alredy_visited:
                continue
            alredy_visited.add(actual_node)
            for node,weight in self.graf[actual_node]:
                new_distance = actual_distance + weight
                if new_distance < self.distance[node]:
                    self.distance[node]=new_distance
                    heapq.heappush(queue, (new_distance, node))
        


    


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graf = Graph()
        for node in range(n):
            graf.add_vertice(node+1)
        
        for node_1,node_2,weight in times:
            graf.add_edge(node_1,node_2,weight)

        graf.dijkstra(k)
        biggest_signal = max(graf.distance.values())
        return biggest_signal if biggest_signal!=float('inf') else -1