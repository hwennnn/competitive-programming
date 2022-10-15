import sys
import math
import random
from functools import lru_cache
import itertools
import collections
from heapq import heappush, heappop, heappushpop, heapify
import bisect
from collections import Counter, defaultdict, deque

sys.setrecursionlimit(10**8)

possible = "POSSIBLE"
impossible = "IMPOSSIBLE"

class Solution():
    def solve(self):
        N = int(input())
        s = list(input().strip())
        
        @lru_cache(None)
        def go(index, curr):
            if index == N:
                return True
            
            if s[index] != "?":
                if len(curr) < 4:
                    if go(index + 1, curr + s[index]):
                        return True
                elif len(curr) == 4:
                    ss = curr + s[index]
                    
                    if ss != ss[::-1] and go(index + 1, ss):
                        return True
                else:
                    t = curr[1:]
                    p = curr
                    
                    temp = t + s[index]
                    remp = p + s[index]
                    
                    if temp != temp[::-1] and remp != remp[::-1] and go(index + 1, temp):
                        return True
                
                return False
            else:
                if len(curr) < 4:
                    if go(index + 1, curr + "0") or go(index + 1, curr + "1"):
                        return True
                elif len(curr) == 4:
                    if curr + "0" != "0" + curr[::-1] and go(index + 1, curr + "0"):
                        return True
                    elif curr + "1" != "1" + curr[::-1] and go(index + 1, curr + "1"):
                        return True
                else:
                    t = curr[1:]
                    p = curr
                    
                    for ch in "01":
                        temp = t + ch
                        remp = p + ch
                    
                        if temp != temp[::-1] and remp != remp[::-1] and go(index + 1, temp):
                            return True
                
                return False
        
        if go(0, ""):
            return possible
        else:
            return impossible
            

if __name__ == "__main__":
    solution = Solution()
    N = int(input())
    for i in range(1, N + 1):
        print(f"Case #{i}: {solution.solve()}")
