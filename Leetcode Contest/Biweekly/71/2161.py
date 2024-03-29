# 2161. Partition Array According to Given Pivot
# https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        count = 0
        
        for x in nums:
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                count += 1
        
        return left + [pivot] * count + right
