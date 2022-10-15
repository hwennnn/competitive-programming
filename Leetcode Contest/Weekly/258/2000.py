# 2000. Reverse Prefix of Word
# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = -1
        
        for index,x in enumerate(word):
            if x == ch:
                i = index
                break
        
        if i == -1: return word
        
        return word[:i + 1][::-1] + word[i + 1:]
        
