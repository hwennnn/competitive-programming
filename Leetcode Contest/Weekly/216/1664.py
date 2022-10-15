# 1664. Ways to Make a Fair Array
# https://leetcode.com/problems/ways-to-make-a-fair-array/

class Solution:
    def waysToMakeFair(self, nums: List[int]):
        ro = re = 0
        for i,x in enumerate(nums):
            if i & 1: ro += x
            else: re += x
        
        lo = le = res = 0
        for i,x in enumerate(nums):
            if i & 1: ro -= x
            else: re -= x
            
            res += (lo + re) == (le + ro)
            
            if i & 1: lo += x
            else: le += x
        
        return res

    def waysToMakeFair(self, nums: List[int]):
        odd = even = 0
        res = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even += num
            else:
                odd += num
        
        co = ce = 0
        for i, num in enumerate(nums):
            e,o = even, odd
            if i % 2 == 0:
                ce += num
                e -= num
            else:
                co += num
                o -= num
                
            e -= (even - ce)
            e += (odd - co)
            o -= (odd - co)
            o += (even - ce)
                
            if (o == e):
                res += 1
        
        return res