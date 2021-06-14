# 1710. Maximum Units on a Truck
# https://leetcode.com/problems/maximum-units-on-a-truck

class Solution:
    def maximumUnits(self, boxes: List[List[int]], truckSize: int) -> int:
        boxes.sort(key = lambda x: (-x[1]))
        res = 0
        
        for box, unit in boxes:
            m = min(box, truckSize)
            res += m * unit
            truckSize -= m
            
            if truckSize == 0: break
        
        return res
