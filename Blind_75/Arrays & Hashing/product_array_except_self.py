'''
Problem Statement: https://leetcode.com/problems/product-of-array-except-self/

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix,postfix = 1, 1
        
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]
            res[n-i-1] *= postfix
            postfix *= nums[n-i-1]

        return res

s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))