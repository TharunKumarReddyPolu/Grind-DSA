'''
Problem Statement: https://leetcode.com/problems/maximum-product-subarray/

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
'''

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            tmp = currMax * n
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * tmp, n * currMin, n)
            res = max(res, currMax)
        
        return res
    
sol = Solution()
print(sol.maxProduct([2,3,-2,4]))
