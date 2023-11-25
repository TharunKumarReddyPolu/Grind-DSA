'''
Problem Statement: https://leetcode.com/problems/house-robber-ii/

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """if len(nums) == 1:
            return nums[0]"""
        
        return max(nums[0], self.rob1(nums[1:]), self.rob1(nums[:-1])) # python max() fn can take max of 3 elements

    
    def rob1(self, nums):
        r1, r2 = 0,0

        for n in nums:
            curr = max(n+r1, r2)
            r1 = r2
            r2 = curr
        return r2
    