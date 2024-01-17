'''
Problem Statement: https://leetcode.com/problems/number-of-1-bits/

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
'''

from typing import List

class Solution:
    def hammingWeight(self, n: int) -> int:
        res  = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res 
        


sol = Solution()
print(sol.hammingWeight(0b00000000000000000000000000001011))
