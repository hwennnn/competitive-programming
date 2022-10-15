# 2350. Shortest Impossible Sequence of Rolls
# https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        curr = 1
        
        for x in rolls:
            seen.add(x)
            
            if len(seen) == k:
                curr += 1
                seen.clear()
        
        return curr
