# -*- coding: utf-8 -*-
"""
Problem  
Given two non-empty linked lists representing two non-negative integers,  
where each node contains a single digit, add the two numbers and return the sum as a linked list.  
The digits are stored in reverse order, meaning that the 1’s digit is at the head of the list.  
You must return the sum in the same reversed order.  

Solution  
This solution iterates through both linked lists, summing corresponding digits along with a carry value.  
If the sum of two digits is greater than or equal to 10, the carry is passed to the next iteration.  
A new linked list is constructed node by node to represent the resulting sum.  
The process continues until both lists are fully traversed, and there is no remaining carry.  
This approach runs in **O(max(N, M))** time complexity, where `N` and `M` are the lengths of the input lists,  
and **O(max(N, M))** space complexity, as we create a new linked list to store the result.  
"""



def add_values(num_1,num_2):
    value = num_1+num_2
    carry = 0
    if value >=10:
        carry +=1
        value -=10
    return value,carry
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start_node= ListNode()
        list_node = start_node

        carry = 0

        while l1 or l2 or carry!= 0:
            value_1 = l1.val if l1 else 0
            value_2 = l2.val if l2 else 0
            value_1 += carry

            new_value,carry = add_values(value_1,value_2) 
            

            list_node.next = ListNode(new_value)
            list_node = list_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return start_node.next