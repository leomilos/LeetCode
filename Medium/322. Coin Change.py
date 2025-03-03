# -*- coding: utf-8 -*-
"""
Problem  
Given an integer array `coins` representing different denominations and an integer `amount`,  
return the **fewest number of coins** needed to make up the given amount.  
If it is not possible to form the amount, return `-1`.  

Solution  
This solution uses **Dynamic Programming (DP)** to find the minimum number of coins required.  
- A DP array `dp` is initialized with size `amount + 1`, where `dp[i]` stores  
  the minimum number of coins needed to make `i`.  
- The base case `dp[0] = 0` is set since zero coins are needed for amount `0`.  
- The algorithm iterates through each amount and each coin denomination,  
  updating the DP table with the minimum coins required.  
- The final result is stored in `dp[amount]`.  

This approach runs in **O(N * M)** time complexity,  
where `N` is the `amount` and `M` is the number of coin denominations.  
The space complexity is **O(N)** due to the DP table.  
This method ensures an **optimal solution** for the **minimum coin change problem**.  
"""
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0:
            return 0
        if amount in coins:
            return 1
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for actual_amount in range(1,amount+1):
            for coin in coins:
                if coin>amount:
                    continue
                dp[actual_amount] = min(dp[actual_amount], dp[actual_amount-coin]+1)
        return dp[amount] if dp[amount]!= float('inf') else -1

