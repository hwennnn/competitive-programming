# 1859. Sorting the Sentence
# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, S: str) -> str:
        s = S.split()
        n = len(s)
        res = [""] * n
        
        for c in s:
            i = int(c[-1])
            res[i - 1] = c[:-1]
        
        return " ".join(res)
