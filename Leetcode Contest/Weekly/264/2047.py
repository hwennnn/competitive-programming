# 2047. Number of Valid Words in a Sentence
# https://leetcode.com/problems/number-of-valid-words-in-a-sentence

class Solution:
    def countValidWords(self, sentence: str) -> int:
        res = 0
        
        for s in sentence.split():
            if any(i in s for i in '0123456789'):
                continue
            if s.count('-') > 1 or s[0] == '-' or s[-1] == '-':
                continue
            if '-' in s:
                x = s.index('-')
                if not s[x-1].isalpha() or not s[x+1].isalpha():
                    continue
            if sum(i in '!.,' for i in s) > 1:
                continue
            if any(i in '!.,' for i in s[:-1]):
                continue
            res += 1
            
        return res
