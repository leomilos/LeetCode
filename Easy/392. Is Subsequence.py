# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 07:20:23 2025

@author: Leonardo Milos
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub_1_index = 0
        size_string_1 = len(s)
        if size_string_1==0:
            return True

        for letter in t:
            if letter == s[sub_1_index]:
                sub_1_index+=1
            if size_string_1==sub_1_index:
                return True
        
        return False
        