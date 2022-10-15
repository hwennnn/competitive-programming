# 1079. Letter Tile Possibilities
# https://leetcode.com/problems/letter-tile-possibilities/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
​
        def dfs(curr, word):
            if curr not in res:
                if curr:
                    res.add(curr)
​
                for i in range(len(word)):
                    dfs(curr + word[i], word[:i] + word[i + 1:])
        
        dfs('', tiles)
        
        return len(res)
