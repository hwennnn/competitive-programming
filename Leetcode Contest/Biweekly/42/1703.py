# 1703. Minimum Adjacent Swaps for K Consecutive Ones
# https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ones = [i for i,x in enumerate(nums) if x]
        n = len(ones)
        
        prefix = [0]
        for p in ones:
            prefix.append(prefix[-1] + p)
            
        res = float('inf')
        
        # k is odd
        if k & 1:
            radius = (k-1) // 2
            
            for i in range(radius, n - radius):
                left = prefix[i] - prefix[i-radius]
                right = prefix[i+radius+1] - prefix[i+1]
                
                res = min(res, right - left)
                
            return res - (radius+1)*radius
        
        # k is even
        else:
            radius = (k-2) // 2
            
            for i in range(radius, n - radius - 1):
                left = prefix[i] - prefix[i-radius]
                right = prefix[i+radius+2] - prefix[i+1]
                
                res = min(res, right - left - ones[i])
            
            return res - (radius+1)*radius - (radius+1)
        
    def minMoves(self, nums: List[int], k: int) -> int:
        ones = [i for i,x in enumerate(nums) if x]
        n = len(ones)
        
        prefix = [0]
        for p in ones:
            prefix.append(prefix[-1] + p)
            
        res = float('inf')

        for i in range(n - k + 1):
            right = prefix[i+k] - prefix[k//2 + i]
            left = prefix[(k+1)//2 + i] - prefix[i]
            res = min(res, right - left)
        
        res -= (k//2)*((k+1)//2)
        
        return res