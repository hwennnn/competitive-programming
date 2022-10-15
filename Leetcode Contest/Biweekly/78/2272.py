# 2272. Substring With Largest Variance
# https://leetcode.com/problems/substring-with-largest-variance

class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        res = 0
        
        for a, b in permutations(set(s), 2):
            cnt = 0
            hasB = firstB = False
            
            for x in s:
                if x == a:
                    cnt += 1
                    
                if x == b:
                    hasB = True
                    
                    if firstB and cnt >= 0:
                        firstB = False
                    else:
                        cnt -= 1
                        
                        if cnt < 0:
                            firstB = True
                            cnt = -1
                
                if hasB and cnt > res:
                    res = cnt
​
        return res
