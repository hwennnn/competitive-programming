# 2106. Maximum Fruits Harvested After at Most K Steps
# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], start: int, k: int) -> int:
        limits = max(max([x for (x, _) in fruits]), start) + k
        s = [0] * (limits + 1)
        
        for x, count in fruits:
            s[x] += count
​
        for i in range(1, limits + 1):
            s[i] += s[i - 1]
            
        s = [0] + s
        
        res = float('-inf')
        
        for i in range(max(0, start - k), start + k + 1):
            if i <= start:
                leftover = k - (start - i)
                right = max(start, i + leftover)
                res = max(res, s[right + 1] - s[i])
            else:
                leftover = k - (i - start)
                left = min(start, i - leftover)
                res = max(res, s[i + 1] - s[left])
        
        return res
