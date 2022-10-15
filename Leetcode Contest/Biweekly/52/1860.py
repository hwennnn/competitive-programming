# 1860. Incremental Memory Leak
# https://leetcode.com/problems/incremental-memory-leak/

class Solution:
    def memLeak(self, m1: int, m2: int) -> List[int]:
        t = 1
        
        while m1 > 0 or m2 > 0:
            if m1 >= m2:
                if m1 >= t:
                    m1 -= t
                else:
                    break
            else:
                if m2 >= t:
                    m2 -= t
                else:
                    break
                    
            t += 1
        
        return [t, m1, m2]
            
