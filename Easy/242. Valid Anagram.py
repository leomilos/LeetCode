
"""
Problem  
Given two strings `s` and `t`, determine if `t` is an anagram of `s`.  
An anagram is a word or phrase formed by rearranging the letters of another,  
using all original letters exactly once.  

Solution  
This solution uses a hash map (dictionary) to count the frequency of characters in `s`  
and then decrement the counts while iterating through `t`.  
If any character count becomes negative or a character is missing, the function returns `False`.  
Finally, if all counts are zero, `t` is an anagram of `s`.  
This approach runs in O(N) time complexity, where N is the length of `s` or `t`,  
and uses O(1) space complexity, as the dictionary stores at most 26 characters (for lowercase English letters).  
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicionario = {}
        for i in s:
            if i in dicionario:
                dicionario[i]+=1
            else:
                dicionario[i]=1
        for j in t:
            if j in dicionario:
                dicionario[j]-=1
                if dicionario[j]<0:
                    return False
            else:
                return False
        for i in dicionario:
            if dicionario[i]>0:
                return False
        return True

