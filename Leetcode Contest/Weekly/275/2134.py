# 2134. Minimum Swaps to Group All 1's Together II
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        
        nums = nums + nums
        maxCount = 0
        
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
        
        for i in range(n):
            maxCount = max(maxCount, prefix[i + ones] - prefix[i])
        
        return ones - maxCount
