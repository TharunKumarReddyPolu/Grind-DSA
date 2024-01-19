'''
Problem Statement: https://leetcode.com/problems/reverse-bits/description/

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
'''

from typing import List

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res =  res | (bit << (31 - i))

        return res    


sol = Solution()
print(sol.reverseBits(0b11111111111111111111111111111101))
