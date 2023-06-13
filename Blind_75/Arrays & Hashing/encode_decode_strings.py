'''
Problem Statement: https://www.lintcode.com/problem/659/

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
'''

from typing import List


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + ";" + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != ';':
                j+=1
            l = int(str[i:j])
            wstart = j+1
            wend = j+1+l
            res.append(str[wstart : wend])
            i = wend
        return res 

s = Solution()
encoded_string = s.encode(["lint","code","love","you"])
print(encoded_string)
print(s.decode(encoded_string))