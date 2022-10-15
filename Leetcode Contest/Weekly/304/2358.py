# 2358. Maximum Number of Groups Entering a Competition
# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        res = 1
        currSize = 0
        size = 2
        
        for i in range(1, n):
            currSize += 1
            
            if currSize == size:
                res = currSize
                size += 1
                currSize = 0
        
        return res
