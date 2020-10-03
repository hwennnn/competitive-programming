# 78. Subsets
# https://leetcode.com/problems/subsets/

# bitmasking
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

# iteratively
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = [[]]
        
        for i in range(n):
            tmp = []
            for num in ans:
                c = num + [nums[i]]
                tmp.append(c)
            
            ans += tmp
        
        return ans
                
        