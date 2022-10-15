# 2064. Minimized Maximum of Products Distributed to Any Store
# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        total = sum(quantities)
        
        def good(x):
            return sum(ceil(quantity / x) for quantity in quantities) <= n
        
        left, right = 1, max(quantities)
        
        while left < right:
            mid = left + (right - left) // 2
            x = good(mid)
​
            if x:
                right = mid
            else:
                left = mid + 1
        
        return left
