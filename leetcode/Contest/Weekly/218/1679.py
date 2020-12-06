# 1679. Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        mp = collections.defaultdict(int)
        res = 0
        
        for i,x in enumerate(nums):
            if k - x in mp:
                res += 1
                mp[k-x] -= 1
                
                if mp[k-x] == 0:
                    del mp[k-x]
            else:
                mp[x] += 1
        
        return res