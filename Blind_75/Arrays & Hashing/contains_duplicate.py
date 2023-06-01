'''
Problem Statement: https://leetcode.com/problems/contains-duplicate/

Input: [1,2,3,1,2]
Output: True
'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for n in nums:
            if n in unique_nums:
                return True
            unique_nums.add(n)
        return False
    
s = Solution()
print(s.containsDuplicate([1,2,3,1,2]))
    
