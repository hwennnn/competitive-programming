# 1324. Print Words Vertically
# https://leetcode.com/problems/print-words-vertically/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        m = len(max(words, key=len))
        n = len(words)
        res = ["" for _ in range(m)]
        
        for i,x in enumerate(words):
            for j in range(m):
                if j >= len(x):
                    res[j] += " "
                else:
                    res[j] += x[j]
        
        for i in range(m):
            res[i] = res[i].rstrip()
                
        
        return res
        