# -*- coding: utf-8 -*-
"""
Problem  
Given an unsorted array of integers `nums`, find the length of the longest consecutive sequence of numbers.  
The sequence must be formed by consecutive integers appearing in any order,  
but they must be part of the array.  

Solution  
This solution first removes duplicates by converting `nums` into a set and then sorts the numbers.  
It iterates through the sorted list, tracking the length of consecutive sequences.  
Whenever a break in the sequence occurs, the longest sequence length is updated.  
This approach runs in **O(N log N)** time complexity due to sorting,  
and **O(N)** space complexity for storing the unique elements in a set.  
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        numbers = list(set(nums))
        numbers.sort()
        max_sequence_size = 1
        before_number = -float('inf')
        actual_sequence = 1
        for actual_number in numbers:
            if before_number + 1 ==actual_number:
                actual_sequence+=1
            else:
                max_sequence_size = max(max_sequence_size,actual_sequence)
                actual_sequence=1
            before_number= actual_number
        return max(max_sequence_size,actual_sequence)