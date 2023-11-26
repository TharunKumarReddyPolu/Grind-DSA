'''
Problem Statement: https://leetcode.com/problems/climbing-stairs/

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''

from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        prev, prev1 = 1,1

        for i in range(2, n+1):
            curr = prev + prev1
            prev1 = prev
            prev = curr
        
        return prev