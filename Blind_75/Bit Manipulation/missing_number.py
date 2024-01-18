'''
Problem Statement: https://leetcode.com/problems/missing-number/description/

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
'''

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        n = len(nums)

        for i in range(n):
            res += i - nums[i]
        return res

sol = Solution()
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))
