# 2209. Minimum White Tiles After Covering With Carpets
# https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
​
        @cache
        def go(index, carpets):
            if index >= n: return 0
            
            res = go(index + 1, carpets) + int(floor[index] == "1")
            if carpets > 0:
                res = min(res, go(index + carpetLen, carpets - 1))
            
            return res
        
        return go(0, numCarpets)
