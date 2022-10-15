# 2195. Append K Integers With Minimal Sum
# https://leetcode.com/problems/append-k-integers-with-minimal-sum/

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        res = 0
        nums.sort()
        prev = 0
        
        for i, x in enumerate(nums):
            if (i == 0 and x == 1) or (i > 0 and x == nums[i - 1]): 
                prev = x
                continue
            
            xx = x - 1
            currentDelta = min(k, xx - prev)
            if k <= currentDelta:
                for j in range(prev + 1, prev + k + 1):
                    res += j
                
                return res
            else:
                delta = xx
                
            if currentDelta == 0: 
                prev = x
                continue
                
            upper = delta * (delta + 1) // 2
            lower = prev * (prev + 1) // 2
            
            res += upper - lower
            
            if currentDelta >= k:
                return res
            k -= currentDelta
            prev = x
​
        if k > 0:
            delta = prev + k
            upper = delta * (delta + 1) // 2
            lower = prev * (prev + 1) // 2
            res += upper - lower
        
        return res
