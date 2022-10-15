# 1013. Partition Array Into Three Parts With Equal Sum
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        total = sum(arr)
        if total % 3 != 0: return False
        target = total // 3
        count = s = 0
        
        for i, x in enumerate(arr):
            s += x
            
            if s == target:
                s = 0
                count += 1
        
        return count >= 3
