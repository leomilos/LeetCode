# -*- coding: utf-8 -*-
"""
Problem  
Given a string `s`, find the length of the longest substring without repeating characters.  

Solution  
This solution uses a **sliding window** approach to efficiently track the longest substring  
without duplicate characters. A dynamic substring (`big_substring`) is maintained,  
removing characters from the start whenever a duplicate is encountered.  
The algorithm iterates through `s`, updating the maximum substring length.  
This approach runs in **O(N)** time complexity, as each character is processed at most twice,  
and **O(N)** space complexity due to storing the substring dynamically.  
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        big_substring_size = 0
        big_substring = ''
        substring_size = 0
        for i in s:
            while i in big_substring:
                big_substring = big_substring[1:]
                substring_size-=1
            big_substring +=i
            substring_size+=1
            if substring_size> big_substring_size:
                big_substring_size=substring_size
        return big_substring_size