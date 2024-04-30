'''
Problem Statement: https://leetcode.com/problems/longest-consecutive-sequence/

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in num_set:
                l = 0
                while n+l in num_set:
                    l += 1
                longest = max(l, longest)
        return longest

s = Solution()
print(s.longestConsecutive([100,4,200,5,1,3,2]))