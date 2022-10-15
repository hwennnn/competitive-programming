# 1859. Sorting the Sentence
# https://leetcode.com/problems/sorting-the-sentence

class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key = lambda x:x[-1])
        
        return " ".join(c[:-1] for c in s)
