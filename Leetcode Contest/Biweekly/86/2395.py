# 2395. Find Subarrays With Equal Sum
# https://leetcode.com/problems/find-subarrays-with-equal-sum/

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        
        seen = set()
        
        for i in range(n - 1):
            curr = nums[i] + nums[i + 1]
            
            if curr in seen:
                return True
            
            seen.add(curr)
        
        return False
                
