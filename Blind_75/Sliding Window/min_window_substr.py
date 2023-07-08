'''
Problem Statement: https://leetcode.com/problems/minimum-window-substring/

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
'''

from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        # maintain current window dict and count of T dict
        countT, window = {}, {}

        #form dict with string t values
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have and need to check whether we have enough values in our window
        # which are in string T
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("inf")

        l=0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # expanding the window to the right
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # while our window is valid
            while have ==  need:
                # update the result if current result length is min that previous
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1

                # shrink the window from the left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""

s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))