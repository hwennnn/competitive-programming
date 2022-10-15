# 1710. Maximum Units on a Truck
# https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : -x[1])
        
        res = size = 0
        for num, units in boxTypes:
            required = min(truckSize - size, num)
            res += required * units
            size += required

        return res