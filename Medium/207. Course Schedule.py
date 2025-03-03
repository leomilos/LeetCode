# -*- coding: utf-8 -*-
"""
Problem  
Given `numCourses` representing the number of courses and a list of prerequisite pairs,  
determine if it is possible to finish all courses.  
Each prerequisite pair `[a, b]` means that course `a` depends on course `b`,  
forming a directed graph.  
If there is a cycle in the graph, it is impossible to finish all courses.  

Solution  
This solution uses **Depth-First Search (DFS)** to detect cycles in the directed graph.  
A graph is built using an adjacency list, and each node is checked for cycles.  
If a cycle is found, the function returns `False`.  
The algorithm tracks visited nodes and a "current recursion stack" to detect cycles.  
This approach runs in **O(N + E)** time complexity, where `N` is the number of courses  
and `E` is the number of prerequisite pairs,  
with **O(N + E)** space complexity due to storing the graph structure.  
"""
from typing import List

class GraphDfs:
    def __init__(self):
        self.graf = {}
        self.visited = {}
        self.current = set()
    def add_node(self,node):
        if node not in self.graf:
            self.graf[node] = []
            self.visited[node] = False
    def add_edge(self,node_1,node_2):
        self.graf[node_1].append(node_2)

    def dfs(self,node):
        if node in self.current:
            return False
        if self.visited[node]==True:
            return True
        self.current.add(node)
        answer = True
        self.visited[node]=True
        for node_sun in self.graf[node]:
            answer = self.dfs(node_sun)
            if answer == False:
                return answer 
        self.current.remove(node)
        return answer


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graf = GraphDfs()
        for node in range(numCourses):
            graf.add_node(node)
        for node_1,node_2 in prerequisites:
            if node_1==node_2:
                return False
            graf.add_edge(node_1,node_2)

        for node in range(numCourses):
            if graf.visited[node]==False:
                if graf.dfs(node) ==False:
                    return False



        return True