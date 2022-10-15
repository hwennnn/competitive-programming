# 2094. Finding 3-Digit Even Numbers
# https://leetcode.com/problems/finding-3-digit-even-numbers/

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n = len(digits)
        
        for i in range(n):
            if digits[i] == 0: continue
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k and digits[k] % 2 == 0:
                        res.add(digits[i] * 100 + digits[j] * 10 + digits[k])
​
        return sorted(list(res))
                    
