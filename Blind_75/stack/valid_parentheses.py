'''
Problem Statement: https://leetcode.com/problems/valid-parentheses/

Input: s = "()[]{}"
Output: true
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
'''

from typing import List

class Solution:
    def valid_parentheses(self, s: str) -> bool:
        stack = []
        parentheses = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        for p in s:
            if p in parentheses:
                if stack and stack[-1] == parentheses[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return True if not stack else False

s = Solution()
print(s.valid_parentheses("()[]{}"))