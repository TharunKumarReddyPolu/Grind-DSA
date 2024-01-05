'''
Problem Statement: https://leetcode.com/problems/longest-increasing-subsequence/

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n

        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # print(LIS)
        return max(LIS)
    
sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
