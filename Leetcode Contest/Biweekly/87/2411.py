# 2411. Smallest Subarrays With Maximum Bitwise OR
# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N
        last = [0] * 32
        
        for i in range(N - 1, -1, -1):
            for k in range(32, -1, -1):
                if (nums[i] >> k) & 1 > 0:
                    last[k] = i
            
            res[i] = max(1, max(last) - i + 1)
        
        return res
