# 2048. Next Greater Numerically Balanced Number
# https://leetcode.com/problems/next-greater-numerically-balanced-number

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        length = len(str(n))
        
        def getPairs(x):
            if x == 1: return [[1]]
            if x == 2: return [[2]]
            if x == 3: return [[3], [1, 2]]
            if x == 4: return [[4], [1, 3]]
            if x == 5: return [[5], [1, 4], [2, 3]]
            if x == 6: return [[6], [1, 5], [1, 2, 3], [2, 4]]
            if x == 7: return [[7], [1, 6], [2, 5], [3, 4], [1, 2, 4]]
            if x == 8: return [[8], [1, 7], [2, 6], [3, 5], [1, 3, 4], [1, 2, 5]]
            
​
        while True:
            left, right = 0, length
            
            perms = set()
            for pairs in getPairs(length):
                
                s = ''
                for i in range(len(pairs)):
                    pair = pairs[i]
                    s += str(pair) * pair
                
                for p in permutations(s):
                    perms.add(int("".join(p)))
​
            perms = sorted(list(perms))
            for p in perms:
                if p > n:
                    return p
            
            length += 1
