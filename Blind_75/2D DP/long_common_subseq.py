'''
Problem Statement: https://leetcode.com/problems/longest-common-subsequence/

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
'''

from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2) 
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]


sol = Solution()
print(sol.longestCommonSubsequence("abcde", "ace"))
