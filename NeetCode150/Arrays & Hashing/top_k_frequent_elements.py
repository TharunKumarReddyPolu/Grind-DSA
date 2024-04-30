'''
Problem Statement: https://leetcode.com/problems/top-k-frequent-elements/

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            # can use count[i] = 1 + count.get(i,0) or below
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i, c in count.items():
            freq[c].append(i)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
    
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))