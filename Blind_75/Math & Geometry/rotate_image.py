'''
Problem Statement: https://leetcode.com/problems/rotate-image/

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
'''

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(l, r):
                top, bottom = l, r
                topLeft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft

            l += 1; r -= 1         


sol = Solution()
print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))
