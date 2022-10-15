# 1217. Minimum Cost to Move Chips to The Same Position
# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution:
    def minCostToMoveChips(self, position: List[int]):
        odd = even = 0
        
        for p in position:
            if p % 2 == 0: even += 1
            else: odd += 1
        
        return min(odd,even)