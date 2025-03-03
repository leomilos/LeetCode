# -*- coding: utf-8 -*-
"""
Problem  
Given `n` cities connected by flights represented as `flights[i] = [from, to, price]`,  
find the **cheapest price** from `src` to `dst` with at most `k` stops.  
If no such route exists, return `-1`.  

Solution  
This solution uses a **modified Dijkstra’s algorithm** with an additional constraint  
on the number of stops.  
- A graph is represented using an adjacency list.  
- A priority queue (min-heap) is used to always process the cheapest path first.  
- A `price` dictionary tracks the minimum cost to reach each city  
  with a given number of stops.  
- The algorithm runs a **BFS-like traversal** using the heap,  
  expanding paths only if they do not exceed `k` stops.  
- The minimum cost to reach the destination is extracted from the tracking table.  

This approach runs in **O(E log N)** time complexity,  
where `E` is the number of flights and `N` is the number of cities,  
ensuring an efficient solution for the **cheapest flight with at most K stops** problem.  

"""

import heapq
class Graph():
    def __init__(self):
        self.graf = {}
        self.price= {}
    def add_vertice(self,node,total_flight):
        if node not in self.graf:
            self.graf[node]=[]
            self.price[node]={}
            for flight in range(total_flight+2):
                self.price[node][flight]=float('inf')


    def add_edge(self,node_1,node_2,price):
        self.graf[node_1].append((node_2,price))
    
    def dijkstra(self,start,max_distance,final):
        
        queue = [(0,start,0)]
        while queue:
            actual_price, actual, distance =  heapq.heappop(queue)
            if distance>=max_distance:
                continue
            for node,price in self.graf[actual]:
                new_price = actual_price+price
                if new_price < self.price[node][distance+1]:
                    self.price[node][distance+1] = new_price
                    if distance+1<max_distance:
                        heapq.heappush(queue,(new_price,node,distance+1))

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = Graph()
        for vertice in range(n):
            graph.add_vertice(vertice,k)
        for node_1,node_2,price in flights:
            graph.add_edge(node_1,node_2,price)
        graph.dijkstra(src,k+1,dst)
        answer = min(graph.price[dst].values())
        return answer if answer!=float('inf') else -1