'''
Problem Statement: https://leetcode.com/problems/jump-game/

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1

        for i in range(n-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False


sol = Solution()
print(sol.canJump([2,3,1,1,4]))
