# 1641. Count Sorted Vowel Strings
# https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution:
    def countVowelStrings(self, n: int):
        a = e = i = o = u = 1
        
        for _ in range(2, n+1):
            a,e,i,o,u = a+e+i+o+u, e+i+o+u, i+o+u, o+u, u
        
        return a + e + i + o + u