# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, S: str, t: str) -> str:
        
        mp = collections.Counter(t)
        A = [(i,x) for i,x in enumerate(S) if x in mp]
        
        n, start, end, required = len(A), 0, 0, len(t)
        res = (float('inf'), 0)
        
        while end < n:
            if mp[A[end][1]] > 0:
                required -= 1
            
            mp[A[end][1]] -= 1
            
            while required == 0:
                s = A[start][0]
                e = A[end][0]
                l = e - s + 1
                
                if l < res[0]:
                    res = (l, s)
                
                mp[A[start][1]] += 1
                if mp[A[start][1]] > 0:
                    required += 1
                
                start += 1
            
            end += 1
​
        return "" if res[0] == float('inf') else S[res[1]: res[0] + res[1]]
