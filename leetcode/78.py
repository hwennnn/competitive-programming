# 78. Subsets
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []
        
        for i in range(1<<n):
            c = []
            for j in range(n):
                if i>>j&1:
                    c.append(nums[j])
            
            res.append(c)
        
        return res