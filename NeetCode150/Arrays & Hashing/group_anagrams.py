'''
Problem Statement: https://leetcode.com/problems/group-anagrams/

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in d:
                d[sorted_s] = [s]
            else:
                d[sorted_s].append(s)
        return d.values()
    
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))