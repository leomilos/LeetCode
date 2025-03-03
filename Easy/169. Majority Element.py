# -*- coding: utf-8 -*-
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

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bigger_value = 0
        bigger_value_count = 0
        for i in nums:
            if bigger_value!= i and bigger_value_count ==0:
                bigger_value=i
            if bigger_value ==i:
                bigger_value_count+=1
            elif bigger_value !=i:
                bigger_value_count-=1
        return bigger_value

