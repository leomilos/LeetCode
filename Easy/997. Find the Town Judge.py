
"""
Problem  
Given an array `nums` of size `n`, return the majority element.  
The majority element is the element that appears more than ⌊n / 2⌋ times.  
You may assume that the majority element always exists in the array.  

Solution  
This solution implements **Boyer-Moore’s Voting Algorithm**, which efficiently finds  
the majority element in O(N) time complexity and O(1) space complexity.  
The algorithm maintains a **candidate element** and a **count**.  
If the count reaches zero, the candidate is updated.  
Since the majority element appears more than ⌊n / 2⌋ times, it will always be the final candidate.  
"""
from typing import List

class Graf:
    def __init__(self)->None:
        self.graph = {}
        self.people_count = {}
    
    def add_node(self,node):
        if node not in self.graph:
            self.graph[node]=[]
            self.people_count[node]=[]
    def add_edge(self,node_1,node_2):
        self.graph[node_1].append(node_2)
        self.people_count[node_2].append(node_1)
    
    def find_the_town_judge(self):
        for person in self.graph:
            if len(self.graph[person])==0 and len(self.people_count[person])== (len(self.people_count)-1):
                return person
        return -1

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graf = Graf()
        for i in range(n):
            graf.add_node(i+1)
        
        for node_1,node_2 in trust:
            graf.add_edge(node_1,node_2)
        
        return graf.find_the_town_judge()

        

        