# 1657. Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = collections.Counter(word1)
        c2 = collections.Counter(word2)
        
        return sorted(c1.keys()) == sorted(c2.keys()) and sorted(c1.values()) == sorted(c2.values())
        
