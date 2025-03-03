
"""
Problem
Given an array of integers nums and a target value target, 
find two numbers whose sum equals the target. Return their indices.
Solution
This solution solves the problem in O(N) time complexity using a hash map to efficiently track 
previously visited numbers and their corresponding indices, allowing for constant-time lookups.
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        index_dict = {}
        target_missing_dict = {}
        numbers_visited = {}
        for num in nums:
            
            target_missing_dict[num] = target - num
            if num not in index_dict:
                index_dict[num] = index
            if target_missing_dict[num] in target_missing_dict and target_missing_dict[num] in numbers_visited:
                return [index_dict[target_missing_dict[num]],index]
            
            numbers_visited[num] =True
            
            index +=1

            
