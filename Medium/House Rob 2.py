# -*- coding: utf-8 -*-
"""
Problem
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Solution
Similar to Rob House 1 but removing first and last value
"""

def house_robb(nums): 
        rob1 = 0
        rob2 = 0
        for house in nums:
            temp = max(rob1+house, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        
        return max(house_robb(nums[1:]),house_robb(nums[:-1]))