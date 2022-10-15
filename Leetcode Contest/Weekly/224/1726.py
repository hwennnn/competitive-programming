# 1726. Tuple with Same Product
# https://leetcode.com/problems/tuple-with-same-product/

class Solution:
    def tupleSameProduct(self, nums: List[int]):
        res = 0
        n = len(nums)
        s = Counter()
        
        for a in range(n):
            for b in range(a+1,n):
                t = nums[a] * nums[b]
                res += s[t]
                s[t] += 1

        return 8 * res