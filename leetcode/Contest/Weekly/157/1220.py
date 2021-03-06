# 1220. Count Vowels Permutation
# https://leetcode.com/problems/count-vowels-permutation/

class Solution:
    def countVowelPermutation(self, n: int):
        M = 10 ** 9 + 7
        a = e = i = o = u = 1
        
        for _ in range(2, n+1):
            a,e,i,o,u = e, a+i, a+e+o+u, i+u, a
        
        return (a+e+i+o+u) % M