# 2271. Maximum White Tiles Covered by a Carpet
# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        res = 0
        tiles.sort()
        
        prefix = [0]
        for x, y in tiles:
            prefix.append(prefix[-1] + y - x + 1)
        
        startPos = [x for x, _ in tiles]
        
        for i, (x, y) in enumerate(tiles):
            if y - x + 1 >= carpetLen:
                return carpetLen
        
            endIndex = bisect.bisect(startPos, x + carpetLen - 1) - 1
            ex, ey = tiles[endIndex]
            
            extra = 0
            
            if ey - x + 1 > carpetLen:
                extra = ey - x - carpetLen + 1
            
            res = max(res, prefix[endIndex + 1] - prefix[i] - extra)
        
        return res
