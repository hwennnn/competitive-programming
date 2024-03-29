# 2379. Minimum Recolors to Get K Consecutive Black Blocks
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        b = 0
        res = inf
        
        for i, x in enumerate(blocks):
            if i >= k:
                if blocks[i - k] == "B":
                    b -= 1
                    
            if x == "B":
                b += 1
            
            if i + 1 >= k:
                res = min(res, k - b)
        
        return res
