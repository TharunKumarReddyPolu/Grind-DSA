'''
Problem Statement: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
'''

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r =  0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l+1, r+1]
            elif curr_sum > target:
                r -= 1
            else:
                l += 1
        return 0


    
s = Solution()
print(s.twoSum([2,7,11,15], 9))