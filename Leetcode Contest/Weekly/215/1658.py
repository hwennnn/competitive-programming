# 1658. Minimum Operations to Reduce X to Zero
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        if total == x: return len(nums)
        
        res = float('-inf')
        target = total - x
        
        mp = collections.defaultdict(int)
        mp[0] = -1
        c = 0
        
        for i,num in enumerate(nums):
            c += num
            
            if c - target in mp:
                res = max(res, i - mp[c-target])
            
            if c not in mp:
                mp[c] = i

        return len(nums) - res if res != float('-inf') else -1
            