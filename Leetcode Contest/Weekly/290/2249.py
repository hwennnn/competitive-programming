# 2249. Count Lattice Points Inside a Circle
# https://leetcode.com/problems/count-lattice-points-inside-a-circle/

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        s = set()
        
        for x, y, r in circles:
            s.add((x, y))
            for dy in range(y - r, y + r + 1):
                for dx in range(x - r, x + r + 1):
                    dist = (dx - x) ** 2 + (dy - y) ** 2
                    if dist <= r ** 2:
                        s.add((dx, dy))
        
        return len(s)
