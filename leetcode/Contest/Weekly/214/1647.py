# 1647. Minimum Deletions to Make Character Frequencies Unique
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

from heapq import heappop, heappush

class Solution:
    # max heap
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        q = []
        
        for v in c.values():
            heappush(q, -v)
        
        res = 0
        while q:
            freq = heappop(q)
            freq = -freq
            
            if not q:
                return res
            
            if freq == -q[0]:
                if freq > 1:
                    v = freq - 1
                    heappush(q, -v)
                res += 1
        
        return res
    
    # greedy
    def minDeletions(self, S: str) -> int:
        c = Counter(S)
        s = set()
        res = 0
        
        for v in c.values():
            t = v
            
            while t in s:
                res += 1
                t -= 1
            
            if t != 0:
                s.add(t)
            
        return res