'''
Problem Statement: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r-l+1)
        return res


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))