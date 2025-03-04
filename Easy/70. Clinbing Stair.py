# -*- coding: utf-8 -*-
"""
Problem:
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Solution: fibonachi
O(n)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        stair_cache = [float('inf')]*(n+1)
        stair_cache[n]=1
        older_step = 0
        for stair_step in range(len(stair_cache)-1,-1,-1):
            if stair_step<=0:
                break
            stair_cache[stair_step-1]=stair_cache[stair_step]+older_step
            older_step=stair_cache[stair_step]

        
        return stair_cache[0]