# 1744. Can You Eat Your Favorite Candy on Your Favorite Day?
# https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        
        res = []
        prefix = [0] + list(accumulate(candiesCount))
            
        for favType, day, cap in queries:
            if (day+1) * cap > prefix[favType] and prefix[favType+1] >= (day+1) * 1:
                res.append(True)
            else:
                res.append(False)
            
        return res
