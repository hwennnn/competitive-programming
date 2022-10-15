# 1881. Maximum Value after Insertion
# https://leetcode.com/problems/maximum-value-after-insertion/

class Solution:
    def maxValue(self, word: str, x: int) -> str:
        
        if word[0] == '-':
            pos = 0
            for i, c in enumerate(word):
                if c == '-': continue
                    
                if x < int(c):
                    return word[:i] + str(x) + word[i:]
            
            return word + str(x)
        else:
            pos = 0
            for i, c in enumerate(word):
                
                if x > int(c):
                     return word[:i] + str(x) + word[i:]
            
            return word + str(x)
            
        
