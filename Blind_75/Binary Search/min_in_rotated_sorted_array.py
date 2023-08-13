'''
Problem Statement: https://leetcode.com/problems/valid-parentheses/

Input: s = "()[]{}"
Output: true
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
'''

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h, res = 0, len(nums) - 1, nums[0]
        
        while l <= h:
            if nums[l] < nums[h]:
                res = min(res, nums[l])
                break
            
            mid = (l + h) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                h = mid - 1
        return res


s = Solution()
print(s.findMin([4,5,6,7,0,1,2]))