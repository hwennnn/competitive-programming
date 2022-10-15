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
    
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        c = collections.Counter(nums)
        res = 0
        
        for x in nums:
            if c[x] > 0 and c[k-x] > 0:
                c[x] -= 1
                c[k-x] -= 1
                res += 1
                
                if c[x] < 0:
                    res -= 1
        
        return res
    
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        res = 0
        mp = collections.Counter(nums)
        
        for key in mp.keys():
            if key * 2 == k:
                res += mp[key] // 2
            
            elif k - key in mp:
                mmin = min(mp[key], mp[k-key])
                res += mmin
                mp[key] -= mmin
                mp[k-key] -= mmin
        
        return res
        