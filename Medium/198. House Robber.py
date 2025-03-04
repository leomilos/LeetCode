# -*- coding: utf-8 -*-
"""
Problem:
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
    
    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Solution:
    - We use two variables, `rob1` and `rob2`, initialized to 0.  
    - `rob1` represents the best amount we could rob **two houses ago**.
    - `rob2` represents the best amount we could rob **one house ago**.
    - For each house, we have two choices:
        1. **Rob this house** → We add `nums[i]` to `rob1` (since we can't rob the previous house).
        2. **Skip this house** → Keep `rob2` as is (carry forward the previous max).
    - We update `rob1 = rob2` and `rob2 = max(rob1 + nums[i], rob2)`, keeping track of the best result
Complexity
O(n)
Space
O(1)
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        for number in nums:
            best_result = max(number+rob1,rob2)
            rob1 = rob2
            rob2 = best_result

        return rob2