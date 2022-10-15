# 2094. Finding 3-Digit Even Numbers
# https://leetcode.com/problems/finding-3-digit-even-numbers/

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        counter = collections.Counter(digits)
        A = []
        
        for k, v in counter.items():
            A += [k] * min(v, 3)
​
        for perm in permutations(A, 3):
            x = int("".join(map(str, perm)))
            if x >= 100 and x % 2 == 0:
                res.add(x)
        
        return sorted(list(res))
        
