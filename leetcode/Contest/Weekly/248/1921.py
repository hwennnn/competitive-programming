# 1921. Eliminate Maximum Number of Monsters
# https://leetcode.com/problems/eliminate-maximum-number-of-monsters

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        A = []
        
        for d,s in zip(dist, speed):
            tt = d // s + int(d % s != 0)
            A.append(tt)
        
        A.sort()
        res = t = 0
​
        for tt in A:
            if tt > t:
                res += 1
            else:
                break
            
            t += 1
        
        return res
