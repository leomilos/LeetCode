# -*- coding: utf-8 -*-
"""
Problem  
Given `numCourses` representing the number of courses and a list of prerequisite pairs,  
determine a valid order to take all courses.  
Each prerequisite pair `[a, b]` means that course `a` depends on course `b`,  
forming a directed graph.  
If there is a cycle in the graph, return an empty list.  
Otherwise, return a valid ordering of courses.  

Solution  
This solution uses **Depth-First Search (DFS)** to detect cycles and perform **topological sorting**  
to determine the correct order of courses.  
The algorithm tracks visited nodes and assigns a depth counter to each course,  
which helps determine the order of completion.  
After running DFS on all nodes, the order is derived by sorting based on depth counters.  
The time complexity is **O(N + E log N)** due to sorting,  
where `N` is the number of courses and `E` is the number of prerequisite pairs,  
while the space complexity is **O(N + E)** for storing the graph structure.  
"""

class GraphDfs:
    def __init__(self):
        self.graf = {}
        self.visited = {}
        self.current = set()
        self.correct_order = []
        self.visited_counter = {}
    def add_node(self,node):
        if node not in self.graf:
            self.graf[node] = []
            self.visited[node] = False
            self.visited_counter[node]=0
    def add_edge(self,node_1,node_2):
        self.graf[node_1].append(node_2)

    def dfs(self,node):
        
        if node in self.current:
            return -999
        if self.visited[node]==True:
            return self.visited_counter[node]
        self.visited_counter[node]+=1
        self.correct_order.append(node)
        self.current.add(node)
        answer = True
        self.visited[node]=True
        for node_sun in self.graf[node]:
            answer = self.dfs(node_sun)
            self.visited_counter[node]+= answer
            if answer == -1:
                return -999
        self.current.remove(node)
        return self.visited_counter[node]


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graf = GraphDfs()
        for node in range(numCourses):
            graf.add_node(node)
        for node_1,node_2 in prerequisites:
            if node_1==node_2:
                return False
            graf.add_edge(node_1,node_2)

        for node in range(numCourses):
            if graf.visited[node]==False:
                graf.dfs(node)
                pass
        order_list = []
        print(graf.visited_counter)
        for order in sorted(graf.visited_counter , key = graf.visited_counter.get,reverse = False):
            #if graf.visited_counter[order]>=0:
            order_list.append(order)
            if graf.visited_counter[order]<0:
                return []





        return order_list