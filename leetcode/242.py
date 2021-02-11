# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str):
        return Counter(s) == Counter(t)