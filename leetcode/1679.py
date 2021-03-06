# 1679. Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int):
        mp = Counter(nums)
        res = 0
        
        for key in mp:
            if key * 2 == k:
                res += mp[key] // 2
            else:
                t = k - key
                if t < key:
                    res += min(mp[t], mp[key])

        return res