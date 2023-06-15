'''
Problem Statement: https://leetcode.com/problems/container-with-most-water/

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l,h = 0, len(height)-1

        while l < h:
            area = (h-l) * min(height[l], height[h])
            max_area = max(max_area, area)

            if height[l] < height[h]:
                l += 1
            else:
                h -= 1
        return max_area

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))