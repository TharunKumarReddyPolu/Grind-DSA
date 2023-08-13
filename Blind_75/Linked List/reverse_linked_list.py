'''
Problem Statement: https://leetcode.com/problems/reverse-linked-list/

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev