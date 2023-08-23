'''
Problem Statement: https://leetcode.com/problems/binary-tree-level-order-traversal/

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        q = collections.deque()
        res = []
        q.append(root)

        while q:
            val = []
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    val.append(node.val)
                    q.append(node.left)
                    q.append(node.right) 
            if val:
                res.append(val)
        return res


    
