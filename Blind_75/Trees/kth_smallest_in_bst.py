'''
Problem Statement: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Input: root = [3,1,4,null,2], k = 1
Output: 1
'''

import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root

        while curr and stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1

            if n == k:
                return curr.val
            curr = curr.right



    
