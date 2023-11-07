'''
Problem Statement: https://leetcode.com/problems/word-search-ii/

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
'''

import collections
from typing import List, Optional

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = None
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r<0 or c<0 or r==rows or c==cols or board[r][c] not in node.children or (r,c) in visit):
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            # visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs( r, c, root, "")
        return list(res)
    





    
