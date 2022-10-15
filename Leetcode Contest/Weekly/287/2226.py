# 2226. Maximum Candies Allocated to K Children
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        total = sum(candies)
        
        if total < k: return 0
        
        def good(b):
            count = 0
            
            for x in candies:
                count += x // b
            
            return count >= k
​
        left, right = 1, 10 ** 18
​
        while left < right:
            mid = left + (right - left + 1) // 2
​
            if good(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
            
            
