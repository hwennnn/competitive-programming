# 1760. Minimum Limit of Balls in a Bag
# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        left, right = 1, max(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if sum((x-1) // mid for x in nums) > maxOperations:
                left = mid + 1
            else:
                right = mid
        
        return left
