# 1007. Minimum Domino Rotations For Equal Row
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        a = collections.Counter(A)
        b = collections.Counter(B)
        mp = collections.defaultdict(int)
        
        for x,y in zip(A,B):
            if x == y:
                mp[x] += 1
                
        res = float("inf")
        for x in a:
            if (a[x] + b[x] - mp[x]) == n:
                res = min(res, min(a[x], b[x]) - mp[x])
    
        return res if res != float("inf") else -1
            
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
    
        def match(x, a, b):
            c = 0
            
            for i, j in zip(a,b):
                if i == x:
                    continue
                elif j == x:
                    c += 1
                else:
                    return float("inf")
            
            return c
        
        res = min(match(A[0], A, B), match(A[0], B, A),
                 match(B[0], A, B), match(B[0], B, A))
        
        return -1 if res == float("inf") else res