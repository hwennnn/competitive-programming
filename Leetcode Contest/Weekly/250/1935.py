# 1935. Maximum Number of Words You Can Type
# https://leetcode.com/problems/maximum-number-of-words-you-can-type

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ss = set(brokenLetters)
        text = text.split(" ")
        res = len(text)
        
        for t in text:
            if set(t) & ss: res -= 1
        
        return res
