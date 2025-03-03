# -*- coding: utf-8 -*-
"""
Problem  
Given a string `s`, find the longest palindromic substring in `s`.  
A palindrome is a string that reads the same forward and backward.  

Solution  
This solution iterates through all possible substrings, checking if each one is palindromic.  
It determines whether a substring is a palindrome using two helper functions:  
one for odd-length substrings and another for even-length substrings.  
The algorithm ensures that once a larger palindrome is found,  
smaller substrings with insufficient length are skipped to optimize performance.  
This approach has a **O(N²)** time complexity due to nested iteration over possible substrings,  
and an **O(1)** space complexity since only a few auxiliary variables are used.  
"""

def is_a_palindromic_odd(string):
    middle = int(-.5+len(string)/2)
    for i in range(middle):
        if string[middle+(i+1)]!=string[middle-(i+1)]:
            return False
    return True
def is_a_palindromic_even(string):
    middle_right = int(len(string)/2)
    middle_left = middle_right-1
    for i in range(middle_right):
        if string[middle_right+i]!=string[middle_left-i]:
            return False
    return True
class Solution:
    def longestPalindrome(self, s: str) -> str:
        biggest_palindromic=''
        biggest_palindromic_size = 0
        string_size = len(s)
        sized_substrings = {}
        for i in range(string_size):
            sub_size = len(s[i:])
            if biggest_palindromic_size>=sub_size:
                break
            for j in range(sub_size):
                if biggest_palindromic_size>string_size-j-i:
                    break
                actual_substring = s[i:string_size-j]
                if (string_size-j-i)%2 == 0:
                    palindromic=is_a_palindromic_even(actual_substring)
                else:
                    palindromic=is_a_palindromic_odd(actual_substring)
                if palindromic and biggest_palindromic_size < string_size-j-i:
                    biggest_palindromic_size = string_size-j-i
                    biggest_palindromic = actual_substring
                    break
        return biggest_palindromic
                


        return biggest_palindromic