# -*- coding: utf-8 -*-
"""
Problem  
Given two words `word1` and `word2`, return the **minimum number of operations**  
required to convert `word1` into `word2`.  
Allowed operations:  
- **Insertion** of a character  
- **Deletion** of a character  
- **Replacement** of a character

Solution 
- build a word Cache (matrix) where len is word1 +1 and word2 +1
- the plus 1 is to put the base cases that mean if i had to replace all letters how many i will spend
- than with the base case i get start calculate the rest of the cases getting the opperation needed 
- add got the right side, remove get the bottom element, equal get the diagonal (down/right)
- repeat thist till get to 0 0 and return it

This approach runs in **O(M × N)** time complexity
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        letter_1_index = 0
        letter_2_index = 0
        # for the indert i should add in letter_2_index+1 and letter_1_index 
        # for the delete i should add in letter_2_index and letter_1_index+1 
        # for the update i should add in letter_2_index+1 and letter_1_index+1 
        word_cache = [[float('inf')]*(len(word2)+1) for i in range(len(word1)+1)]
        for letter2_index in range(len(word2)+1):
            word_cache[len(word1)][letter2_index] = len(word2)-letter2_index
        for letter1_index in range(len(word1)+1):
            word_cache[letter1_index][len(word2)] = len(word1)-letter1_index
            
        for letter1_index in range(len(word1)-1,-1,-1):
            for letter2_index in range(len(word2)-1,-1,-1):
                if word1[letter1_index]==word2[letter2_index]:
                    word_cache[letter1_index][letter2_index] = word_cache[letter1_index+1][letter2_index+1]
                else:
                    word_cache[letter1_index][letter2_index] = 1+min(word_cache[letter1_index][letter2_index+1],word_cache[letter1_index+1][letter2_index],word_cache[letter1_index+1][letter2_index+1])
        return word_cache[0][0]