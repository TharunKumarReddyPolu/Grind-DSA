'''
Problem Statement: https://leetcode.com/problems/house-robber/

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0,0

        for n in nums:
            temp = max(n+r1, r2)
            r1 = r2
            r2 = temp

        return r2
    