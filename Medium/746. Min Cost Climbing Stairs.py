# -*- coding: utf-8 -*-
"""
Problem

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Solution :
    build a array of steps and set base cases that is the number 1 and number 2
    than calculate whitch step is the cheapest to actual house if is the 2 steps before or the last step
    than repeat this till the end
    the last value of the array is the minimum value

Complexity
O(n)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step_array = [0]*(len(cost)+1)
        step_array[0] = cost[0]
        step_array[1] = cost[1]
        cost.append(0)
        for cost_index in range(2,len(cost)):
            step_array[cost_index]= min(step_array[cost_index-1]+cost[cost_index],step_array[cost_index-2]+cost[cost_index])
        return step_array[-1]
        