# 2044. Count Number of Maximum Bitwise-OR Subsets
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        mp = collections.defaultdict(int)
        mmax = float('-inf')
        
        for mask in range(1, 1 << n):
            s = 0
            for j in range(n):
                if (mask >> j) & 1:
                    s |= nums[j]
​
            mp[s] += 1
            mmax = max(mmax, s)
​
        return mp[mmax]
