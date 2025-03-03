# -*- coding: utf-8 -*-
"""
Problem  
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to  
the product of all elements in `nums` except `nums[i]`.  
The solution must be **O(N)** in time complexity and must not use division directly.  

Solution  
This approach first counts the number of zeros in the array:  
- If more than one zero exists, the result is all zeros.  
- If exactly one zero exists, the product of all nonzero numbers is placed at the zero’s index.  
- Otherwise, the total product of all elements is computed, and each index is updated  
  by dividing the total product by `nums[i]`.  
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        number_of_zero = nums.count(0)
        list_multiplication = 1
        if number_of_zero > 1:
            return [0]*len(nums)
        elif number_of_zero==1:
            zero_index = -1
            for index in range(len(nums)):
                if nums[index]==0:
                    zero_index=index
                    continue
                list_multiplication*= nums[index]
                nums[index]=0
            nums[zero_index]=list_multiplication
            return nums
        
        for number in nums:
            list_multiplication*= number

        for index in range(len(nums)):
            nums[index]=int(list_multiplication/nums[index])
        
        return nums
