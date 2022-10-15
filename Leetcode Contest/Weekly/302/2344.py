# 2344. Minimum Deletions to Make Array Divisible
# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        
        d = numsDivide[0]
        
        for x in numsDivide:
            d = gcd(d, x)
            
        for i, x in enumerate(nums):
            if d % x == 0:
                return i
        
        return -1
