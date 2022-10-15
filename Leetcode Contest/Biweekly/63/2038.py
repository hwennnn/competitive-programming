# 2038. Remove Colored Pieces if Both Neighbors are the Same Color
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        if n <= 2: return False
        
        a = b = 0
        for i in range(1, n - 1):
            if colors[i - 1] == colors[i] == colors[i + 1] == 'A':
                a += 1
            elif colors[i - 1] == colors[i] == colors[i + 1] == 'B':
                b += 1
        
        return a > b
