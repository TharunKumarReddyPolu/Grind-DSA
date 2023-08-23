'''
Problem Statement: https://leetcode.com/problems/validate-binary-search-tree/

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return ((valid(node.left, left, node.val)) and (valid(node.right, node.val, right)))
        
        return valid(root, float("-inf"), float("inf"))



    
