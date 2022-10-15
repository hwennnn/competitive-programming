# 1711. Count Good Meals
# https://leetcode.com/problems/count-good-meals/

class Solution:
    def countPairs(self, arr: List[int]):
        
        M = 10 ** 9 + 7     
        mp = Counter(arr)
        res = 0

        for i in range(22):

            p = 1 << i
            
            for k in mp:
                target = p - k
                if k == target:
                    res += ((mp[k]) * (mp[k]-1)) // 2
                elif k < target:
                    res += mp[k] * mp[target]

                res %= M
            
        return res % M

    def countPairs(self, A: List[int]):
        
        M = 10 ** 9 + 7     
        mp = Counter()
        res = 0

        for num in A:
            
            for i in range(22):
                target = (1 << i) - num
                
                if target in mp:
                    res += mp[target]
            
            mp[num] += 1
            
        return res % M


