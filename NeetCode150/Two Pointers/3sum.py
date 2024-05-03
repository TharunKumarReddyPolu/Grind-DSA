'''
Problem Statement: https://leetcode.com/problems/3sum/

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,h = i+1,len(nums)-1
            while l<h:
                curr_sum = nums[i]+nums[l]+nums[h]
                if curr_sum == 0:
                    triplets.append([nums[i],nums[l],nums[h]])
                    l += 1
                    h -= 1
                    while l<h and nums[l]==nums[l-1]:
                        l += 1
                    while l<h and nums[h]==nums[h+1]:
                        h -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    h -= 1
        return triplets

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))