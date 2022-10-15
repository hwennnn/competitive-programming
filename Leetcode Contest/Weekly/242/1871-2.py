# 1871. Jump Game VII
# https://leetcode.com/problems/jump-game-vii

from sortedcontainers import SortedList
​
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        sl = SortedList([0])
        
        for i in range(1, n):
            if s[i] == "0":
                index = sl.bisect_left(i - maxJump)
                
                if 0 <= index < len(sl) and sl[index] + minJump <= i:
                    sl.add(i)
        
        return n - 1 in sl
