'''
Problem Statement: https://leetcode.com/problems/search-in-rotated-sorted-array/

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1

        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    h = mid - 1
            else:
                if target < nums[mid] or target > nums[h]:
                    h = mid - 1
                else:
                    l = mid + 1
        return -1



s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))