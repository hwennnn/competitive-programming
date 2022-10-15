# 2079. Watering Plants
# https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        res = 0
        curr = capacity
        
        for i, x in enumerate(plants):
            res += 1
            curr -= x
            
            if i + 1 < n and curr < plants[i + 1]:
                res += i + 1 # go back to fill
                res += i + 1 # go back to curr pos
                curr = capacity
        
        return res
