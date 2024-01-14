'''
Problem Statement: https://www.lintcode.com/problem/919/

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
'''

from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        
        return res


sol = Solution()
print(sol.min_meeting_rooms([(0,30),(5,10),(15,20)]))
