# 1248. Count Number of Nice Subarrays
# https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]
        start = float('inf')
        mp = collections.defaultdict(int)
        mp[0] = 1
        
        for num in nums:
            prefix.append(prefix[-1] + int(num % 2 == 1))
            if prefix[-1] >= k:
                start = min(start, len(prefix)-1)
            mp[prefix[-1]] += 1
            
        if start == float('inf'): return 0

        res = 0
        for i in range(start, len(prefix)):
            if prefix[i] - k in mp:
                res += mp[prefix[i]-k]
            
        
        return res