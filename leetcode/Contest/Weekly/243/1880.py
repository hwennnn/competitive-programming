# 1880. Check if Word Equals Summation of Two Words
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def getNum(s):
            res = ""
            
            for char in s:
                c = ord(char) - ord('a')
                res += str(c)
            
            return int(res)
        
        return getNum(firstWord) + getNum(secondWord) == getNum(targetWord)
