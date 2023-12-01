'''
Problem Statement: https://leetcode.com/problems/longest-palindromic-substring/

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
'''

from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0
        n = len(s)

        for i in range(n):
            # Odd len palindrome
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # Even len palindrome
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res