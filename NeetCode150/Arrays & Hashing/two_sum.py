'''
Problem Statement: https://leetcode.com/problems/two-sum/

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in prev:
                return [prev[diff], i]
            prev[num] = i 
    
s = Solution()
print(s.twoSum([3,2,4], 6))