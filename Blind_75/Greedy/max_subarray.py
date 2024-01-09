'''
Problem Statement: https://leetcode.com/problems/maximum-subarray/

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        CurSum = 0

        for n in nums:
            if CurSum < 0:
                CurSum = 0
            CurSum += n
            maxSub = max(maxSub, CurSum)
        
        return maxSub


sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
