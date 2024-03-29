# 2342. Max Sum of a Pair With Equal Sum of Digits
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(list)
        
        for x in nums:
            cnt[sum(int(k) for k in str(x))].append(x)
        
        res = -1
        
        for values in cnt.values():
            if len(values) >= 2:
                values.sort()
                res = max(res, values[-1] + values[-2])
            
        
        return res
