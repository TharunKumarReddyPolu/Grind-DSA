'''
Problem Statement: https://leetcode.com/problems/valid-palindrome/

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_converted = ''

        for i in s:
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57):
                s_converted += i
        # print(s_converted)
        return s_converted == s_converted[::-1]

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))