# 2063. Vowels of All Substrings
# https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        res = 0
​
        for i, s in enumerate(word):
            if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
                res += ((n - i) * (i + 1))           
​
        return res
