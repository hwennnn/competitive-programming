# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = j = res = zeroes = 0
        
        while i < n:
                
            while j < n and (nums[j] == 1 or zeroes < k):
                if nums[j] == 0:
                    zeroes += 1
                j += 1
            
            res = max(res, j - i)
            
            if zeroes < k: return res
            
            while i < n and zeroes >= k:
                if nums[i] == 0:
                    zeroes -= 1
                i += 1
            
        return res
