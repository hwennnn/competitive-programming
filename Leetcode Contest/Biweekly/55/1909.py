# 1909. Remove One Element to Make the Array Strictly Increasing
# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

class Solution:
    def canBeIncreasing(self, arr: List[int]) -> bool:
        count = 0
        n = len(arr)
        
        for i in range(n):
            valid = True
            last = 0
            for j in range(n):
                if j == i: continue
                if arr[j] <= last:
                    valid = False
                    break
                
                last = arr[j]
            
            if valid: count += 1
                    
        return count != 0
