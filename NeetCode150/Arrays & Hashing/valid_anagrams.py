'''
Problem Statement: https://leetcode.com/problems/valid-anagram/

Input: s = "anagram", t = "nagaram"
Output: true
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS,countT={},{}
        for i in s:
            if i in countS:
                countS[i]+=1
            else:
                countS[i]=1
        for i in t:
            if i in countT:
                countT[i]+=1
            else:
                countT[i]=1
        if countS == countT:
            return True
        else:
            return False
    
s = Solution()
print(s.isAnagram("anagram", "nagaram"))