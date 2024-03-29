# 2302. Count Subarrays With Score Less Than K
# https://leetcode.com/problems/count-subarrays-with-score-less-than-k

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        i = 0
        s = 0
        
        for j, x in enumerate(nums):
            s += x
            
            while s * (j - i + 1) >= k:
                s -= nums[i]
                i += 1
            
            res += (j - i + 1)
​
        return res
