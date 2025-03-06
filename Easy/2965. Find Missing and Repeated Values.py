# -*- coding: utf-8 -*-
"""
Problem:
You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
Solution:
- We create two sets:
    1. `all_numbers`: A set containing all expected numbers from 1 to n².
    2. `values`: A set to track numbers encountered in the grid.
- As we iterate through `grid`, we:
    - Check if a number is **already in `values`** (meaning it's duplicated).
    - Add each number to `values`.
- The missing number is found using `all_numbers - values`.
- Finally, we return `[duplicate, missing]`.
"""

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        values = set()
        all_numbers = set()
        for i in range(len(grid)*len(grid)):
            all_numbers.add(i+1)
        a=None
        b=None
        for list_in_grid in grid:
            for i in list_in_grid:
                if i in values:
                    a = i
                values.add(i)
                if i not in all_numbers:
                    b = i
        last_number =  all_numbers-values
        return [a,last_number.pop()]