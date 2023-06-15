'''
Problem Statement: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l = prices[0]
        for price in prices:
            if price < l:
                l = price
            max_profit = max(max_profit, price - l)
        return max_profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))