'''
Problem Statement: https://leetcode.com/problems/coin-change/

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
'''

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if (a - c) >= 0:
                    x, y = dp[a], dp[a - c]
                    dp[a] = min(x, 1 + y)

        return dp[amount] if dp[amount] != amount + 1 else -1
    
sol = Solution()
print(sol.coinChange([1,3,4,5], 7))
