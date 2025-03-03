
"""
Problem  
Given an integer `x`, determine whether it is a palindrome.  
An integer is a palindrome when it reads the same forward and backward.  

Solution  
This solution checks if the number is a palindrome by reversing it and comparing it to the original value.  
Since negative numbers cannot be palindromes, they are immediately returned as `False`.  
The reversal process is performed using modulo and integer division, ensuring an O(log N) time complexity,  
where N is the number of digits in `x`.  
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        start_num = x
        reversed_number = 0

        while x > 0:
            last_number = x%10
            reversed_number = (reversed_number*10) + last_number
            x //=10
        return reversed_number==start_num
    
