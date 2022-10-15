# 2305. Fair Distribution of Cookies
# https://leetcode.com/problems/fair-distribution-of-cookies

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        res = float('inf')
        A = [0] * k
        
        def go(index):
            nonlocal res, A
            
            if index == n:
                res = min(res, max(A))
                return
            
            seen = set()
            
            for j in range(k):
                if A[j] in seen: continue
                if A[j] + cookies[index] >= res: continue
                
                seen.add(A[j])
                A[j] += cookies[index]
                go(index + 1)
                A[j] -= cookies[index]
        
        go(0)
        
        return res
