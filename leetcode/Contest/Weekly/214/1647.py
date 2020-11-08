# 1647. Minimum Deletions to Make Character Frequencies Unique
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

from heapq import heappop, heappush

class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        q = []
        
        for v in c.values():
            heappush(q, (-v, v))
        
        res = 0
        while q:
            _, freq = heappop(q)
            
            if not q:
                return res
            
            if freq == q[0][1]:
                if freq > 1:
                    v = freq - 1
                    heappush(q, (-v, v))
                res += 1
        
        return res
                