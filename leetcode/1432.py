# 1423. Maximum Points You Can Obtain from Cards
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

# Approach: find minimum subarray with length of len(arr) - k
class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        size = n-k
        c = j = 0
        res = float('inf')
        
        for i,v in enumerate(arr):
            c += v
            
            if i - j >= size:
                c -= arr[j]
                j += 1
            
            if i - j + 1 == size:
                res = min(res, c)
        
        return sum(arr) - res