# 1779. Find Nearest Point That Has the Same X or Y Coordinate
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist, idx = float('inf'), -1
        
        for i, (a,b) in enumerate(points):
            if a == x or b == y:
                d = abs(a - x) + abs(b - y)
                if d < dist:
                    idx = i
                    dist = d
​
        return idx
