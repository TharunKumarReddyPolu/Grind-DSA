'''
Problem Statement: https://leetcode.com/problems/longest-repeating-character-replacement/

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Intution: (length of window - max char freq) <= k, gives a valid window and get max result. 
If the window is not valid, shrink the window(remove count of char at l, increment l) and repeat the above process.
'''

from typing import List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq, res, char_count = 0, 0, {}

        l =0
        for r in range(len(s)):
            char_count[s[r]] = 1 + char_count.get(s[r], 0)
            max_freq = max(max_freq, char_count[s[r]]) #calculate max freq while adding new char to the dict.
            while (r-l+1) - max_freq > k: # main condition/logic
                char_count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res



s = Solution()
print(s.characterReplacement("AABABBA", 1))