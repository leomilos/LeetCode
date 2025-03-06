# -*- coding: utf-8 -*-
"""
Problems:
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    
    Return the maximum amount of water a container can store.
    
    Notice that you may not slant the container.
Solution
    2 pointers 1 pointed to start and other to the end
    than move the lower to the next step
    and always check the higher volume and save it
    return bigger value
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        width = [0]*len(height)
        left = 0
        right = len(height)-1
        bigger_value = 0
        top_height = 0
        for i in range(len(height)):
            minimum_value = min(height[left],height[right])
            actual_volume = minimum_value*(right - left)
            if actual_volume > bigger_value:
                top_height=minimum_value
                bigger_value=actual_volume
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return bigger_value