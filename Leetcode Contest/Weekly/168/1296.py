# 1296. Divide Array in Sets of K Consecutive Numbers
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0: return False
        
        c = collections.Counter(nums)

        cs = sorted(c.keys())
        
        def findStart():
            for key in cs:
                if c[key] > 0: return key

        for t in range(n//k):
            start = findStart()
            for i in range(start, start+k):
                if c[i] > 0:
                    c[i] -= 1
                else:
                    return False
            
        return True

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0: return False
        
        count = collections.Counter(nums)
        keys = sorted(count)
        
        for key in keys:
            if count[key] > 0:
                c = count[key]
                for i in range(key, key+k):
                    if count[i] < c: return False
                    
                    count[i] -= c
            
        return True