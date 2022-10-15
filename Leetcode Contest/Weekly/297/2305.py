# 2305. Fair Distribution of Cookies
# https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        fullMask = (1 << n) - 1
        
        def good(x):
​
            @cache
            def go(child, mask, curr):
                if mask == fullMask:
                    return child == k - 1
​
                if curr > 0 and go(child + 1, mask, 0):
                    return True
                
                for j in range(n):
                    if mask & (1 << j) == 0:
                        if curr + cookies[j] <= x:
                            if go(child, mask ^ (1 << j), curr + cookies[j]):
                                return True
                        else:
                            if cookies[j] <= x and go(child + 1, mask ^ (1 << j), cookies[j]):
                                return True
                
                return False
                
            return go(0, 0, 0)
        
        left, right = 1, 10 ** 18
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
