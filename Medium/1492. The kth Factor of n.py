# -*- coding: utf-8 -*-
"""
Problem  
Given two integers `n` and `k`, find the `k`-th smallest factor of `n`.  
If `n` has fewer than `k` factors, return `-1`.  

Solution  
This solution optimizes factor computation using **square root decomposition**.  
Instead of iterating through all numbers up to `n` (**O(N)**),  
it only iterates up to `sqrt(n)`, adding both `i` and `n // i` as factors.  
This reduces the time complexity to **O(sqrt(N))**.  
After collecting the factors in a set, they are sorted,  
and the `k`-th smallest factor is returned if it exists.  
Otherwise, `-1` is returned.  

This approach significantly improves efficiency for large values of `n`.  
"""

import math
def factor_otimized(number: int)-> list:
    factor = set()
    for i in range(1, int(math.sqrt(number))+1):
        if number %i ==0:
            factor.add(i)
            factor.add(number//i)
    return sorted(factor)
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        #factor = [i for i in range(1,n+1) if n%i ==0] #->solution O(n)
        factor = factor_otimized(n)
        if len(factor)>= k:
            return factor[k-1]
        return -1