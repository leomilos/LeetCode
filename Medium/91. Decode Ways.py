# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 20:25:42 2025

@author: Leonardo Milos
"""


def calculate_two_letter(letter_1,letter_2):
    if letter_1=='0' or letter_2=='0':
        return 0
    elif int(letter_1+letter_2)<=26:
        return 2
    else:
        return 1

class Solution:
    def numDecodings(self, s: str) -> int:
        if s==[] or s[0]=='0':
            return 0
        if len(s)==1:
            return 1
        strings_solution = [0]*(len(s)+1)
        strings_solution[0]=1
        if s[0]=='0':
            strings_solution[1]=0
        else:
            strings_solution[1]=1
            
        for letter_index in range(2, len(s) + 1):
            if s[letter_index - 1] != '0':
                strings_solution[letter_index] += strings_solution[letter_index - 1]

            int_strings = int(s[letter_index - 2:letter_index])
            if 10 <= int_strings <= 26:
                strings_solution[letter_index] += strings_solution[letter_index - 2]

        return strings_solution[-1]