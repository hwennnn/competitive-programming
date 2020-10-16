# 1365. How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# Couting bucket
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * 101
        res = [0] * n
        
        for c in nums:
            counts[c] += 1
            
        for i in range(1,101):
            counts[i] += counts[i-1]
            
        for i, num in enumerate(nums):
            if num != 0:
                res[i] = counts[num-1]
        
        return res

# Brute force
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            c = 0
            for j in range(len(nums)):
                if i != j:
                    if nums[j] < nums[i]:
                        c += 1
            res.append(c)
        
        return res