# 1539. Kth Missing Positive Number
# https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int):
        n = len(arr)
        res = [False for _ in range(1001)]
        
        for i in arr:
            if i <= n+k:
                res[i-1] = True

        i = 0
        while k > 0 and i <= 1000:
            if not res[i]: k -= 1
            
            i += 1
        
        return i if k == 0 else i + k
        